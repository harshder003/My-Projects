import requests

city = input("Enter a city: ")

url = f"https://forecast9.p.rapidapi.com/rapidapi/forecast/{city}/summary/"

headers = {
	"X-RapidAPI-Key": "cc8568bfb6msha5290aa33512be0p1368aejsn9fb75399fa8d",
	"X-RapidAPI-Host": "forecast9.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
dict = response.json()

print(dict['location']["name"])
print('date:',dict["forecast"]['items'][0]['date'])
print('Minimum temperature:',dict["forecast"]['items'][0]['temperature']['min'])
print('Maximum temperature:',dict["forecast"]['items'][0]['temperature']['max'])