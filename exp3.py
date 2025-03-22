import requests as req
api_code = "345557482a87102a24642cc74a94f472"
city = "giddalur"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_code}&units=metric"
res = req.get(url)
if res.status_code == 200:
    weather = res.json()
    celcius=weather['main']['temp']
    print(f"Temperature: {celcius}C")
    print(f"Weather: {weather['weather'][0]['description']}")
else:
    print(f"Failed to fetch data. Status code: {res.status_code}")

