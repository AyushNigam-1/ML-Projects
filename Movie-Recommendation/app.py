import streamlit as st # type: ignore
import pickle 
import pandas as pd # type: ignore
import requests # type: ignore

def fetch_poster(movie):
    st.spinner('Fetching poster...')
    response = requests.get('https://www.omdbapi.com/?t={}&apikey=fdd039ff'.format(movie))
    data = response.json()
    return data['Poster']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    print(movies_list)
    recommend_movies = []
    recommend_movies_poster = []
    for i in movies_list:
        movie_title = movies.iloc[i[0]].title
        recommend_movies.append(movie_title)
        recommend_movies_poster.append(fetch_poster(movie_title))
        print(recommend_movies ,recommend_movies_poster)
    return recommend_movies ,recommend_movies_poster

movies_dict = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')

selected_movie = st.selectbox("Choose Movie" , movies['title'].values)

if st.button('Recommend'):

    with st.spinner('Wait for it...'):
       recommended_movies, recommended_posters = recommend(selected_movie)

    st.success("Done!")
    num_columns = min(len(recommended_movies), 5)  # Limit to 5 columns for better layout

    # Create columns dynamically
    columns = st.columns(num_columns)

    
    for i, (movie_title, movie_poster) in enumerate(zip(recommended_movies, recommended_posters)):
          with columns[i % num_columns]: 
            if movie_poster:
                st.image(movie_poster)  
            else:
                st.text('Poster unavailable') 
            st.text(movie_title, anchor="middle")
    




