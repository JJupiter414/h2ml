import requests

def get_weather_data(city):
    api_key = 'dac00f2c725c9bcdc0d462f746a32964'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    
    return {
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'description': data['weather'][0]['description']
    }
 
