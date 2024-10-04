
from langchain.vectorstores.cassandra import Cassandra
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
import cassio

from PyPDF2 import PdfReader
from os import getenv
from dotenv import load_dotenv
load_dotenv()
ASTRA_DB_APPLICATION_TOKEN = getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_ID = getenv("ASTRA_DB_ID")
OPEN_AI_KEY = ""

pdfreader = PdfReader('budget_speech.pdf')

from typing_extensions import Concatenate
raw_text = ''
for i, page in enumerate(pdfreader.pages):
    text = page.extract_text()
    if text:
        raw_text += text

cassio.init(token=ASTRA_DB_APPLICATION_TOKEN,database_id=ASTRA_DB_ID)

llm = OpenAI(openai_api_key=OPEN_AI_KEY)
embedding = OpenAIEmbeddings(openai_api_key=OPEN_AI_KEY)

astra_vector_store = Cassandra(
    embedding=embedding,
    session=None,
    keyspace=None,
    table_name="budget_speech",
)

from langchain.text_splitter import CharacterTextSplitter
text_splitter = CharacterTextSplitter(separator='\n',chunk_size=1000, chunk_overlap=0,len_function=len)
texts = text_splitter.split_text(raw_text)

astra_vector_store.add_texts(texts[:50])

# print("INserted %i headlines",%%len(texts))

astra_vector_index = VectorStoreIndexWrapper(vectorstore=astra_vector_store)

first_question = True
while True:
  if first_question:
    query_text = input("Enter a question").strip()
  else:
    query_text = input("What's you next question").strip()

  if query_text == "":
    break
  else:
     continue

  first_question = False
  response = astra_vector_index.query(query_text,llm=llm)
  print("Answer",response)

  for doc,score in astra_vector_store.similarity_search_with_score(query_text,k=5):
    print("[%0.4f] \"%s ...\"" % (score,doc.page_content[:30]))