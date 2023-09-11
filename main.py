from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        api_key = 'fa68f14f42d681222056dfba47104a45'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        response = requests.get(url)
        weather_data = response.json()

        if weather_data['cod'] == 200:
            temperature = weather_data['main']['temp']
            description = weather_data['weather'][0]['description']
            return render_template('weather.html', city=city, temperature=temperature - 273.15, description=description)
        else:
            error_message = 'Город не найден'
            return render_template('index.html', error_message=error_message)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
