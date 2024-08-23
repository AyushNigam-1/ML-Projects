from flask import Flask , request , jsonify
import requests
app = Flask(__name__)

@app.route("/" , methods=['GET','POST'])
def index():
    if request.method == 'POST':
       data = request.get_json()
       source_currency = data['queryResult']['parameters']['unit-currency'][0]['currency']
       amount = data['queryResult']['parameters']['unit-currency'][0]['amount']
       target_currency = data['queryResult']['parameters']['currency-name'][0]

# curl -H "Content-Type: application/json; charset=utf-8"  -H "Authorization: Bearer ya29.a0AcM612xhzC6rJAPkdc_0sh7QvL6af51mljBnTXUFB2eScGIYwib1ZH-WMz5Ttjan_e_o7w3FntGPZtSUy-Z_wOz6LDPIqHeiWGzfG6zOoV75sU3p1nLRf0CqrnVHV1H9gpB_cCcxkMnsf0vdSFeJE2HKoUWid2SXIiCO0obJ5J3XbdtlmpbjyQGFlpWNYsE5A8I7wPKUT_YD2BQPdmLJC477m_1UKH6n8phvoRhRt9sdfaaVTaIKiLj5jlm49t9uvtizXHngZnDQmeTmofsBi2thPioK076FJU2uM9ucPF9ubXNQ8Gd4VvxhNjBqt42Ei9742aEwsgy3fCS9paU-swI5XRodEKDWDrI5r-UZcLy8SfvZKIN_lKIFyVTaOsHO9BMjLG80ma91jHC1PFgh1stQUnxa82-2pIr8jTtQaCgYKARASARISFQHGX2MiNKTBM6SQeCbCEZA8ilGOqw0431"  -d "{\"queryInput\":{\"text\":{\"text\":\"how much is 100ruble in india rupee\",\"languageCode\":\"en\"}},\"queryParams\":{\"source\":\"DIALOGFLOW_CONSOLE\",\"timeZone\":\"Asia/Calcutta\"}}" "https://dialogflow.googleapis.com/v2/projects/support-agent-mnxc/agent/sessions/53b55321-ed53-eb4d-f645-a303b6cada8a:detectIntent"

       url = f"https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_0qMJCf12cAVYzoA5jEJzabn7MvX5wwxtXAObGCQT&currencies={target_currency}&base_currency={source_currency}"
       conversion_factor = requests.get(url)
       conversion_factor = conversion_factor.json()
       print(conversion_factor['data'][target_currency]*amount)
       final_amount = conversion_factor['data'][target_currency]*amount
       response = {
           'fulfillmentText':f"{amount} {source_currency} is {final_amount} {target_currency}"
       }
       return jsonify(response)
       
    
    return "Hello"

if __name__ == '__main__':
    app.run(debug=True)

