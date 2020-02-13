# py-weather-music

written in python `version 3.7.0`

Generates midi files (songs) based on weather forecast for given city.

Using [OpenWeatherMap API](https://openweathermap.org/forecast5) to pull weather forecast for next 5 days (3 hour) for specified location.
This gives 5 days x 8 points = 40 weather data points, on which the midi file generation is based.


To generate a song, run python script with specified city name and country code being [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1) compliant, example:
```
python main.py los+angeles us
```

