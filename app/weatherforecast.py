import pyowm

owm = pyowm.OWM('f7d3136786b15c2e1a3fb486b5df296a')

# current wind and temp in milnerton
obs = owm.weather_at_place('Milnerton,South Africa')
w = obs.get_weather()
print w.get_wind(), w.get_temperature('celsius')
obs2 = owm.weather_at_coords(18.5003, -33.871)
x = obs2.get_weather()
print x.get_wind(), x.get_temperature('celsius')
