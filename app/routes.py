import pyowm
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)

owm = pyowm.OWM('f7d3136786b15c2e1a3fb486b5df296a')

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/weather', methods=['GET', 'POST'])
def weather():
    longitude = float(request.args.get('long', [18.5003])[0])
    latitude = float(request.args.get('lat', [-33.871])[0])
    observation = owm.weather_at_coords(longitude, latitude)
    results = observation.get_weather()
    return jsonify(results.get_temperature('celsius'))

if __name__ == '__main__':
  app.run(debug=True)
