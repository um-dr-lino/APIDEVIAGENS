import http.client
import json
import datetime


cidade = "Sao Paulo"
conn = http.client.HTTPSConnection("sky-scrapper.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "2357b19b61msh74ab90a94f75bc5p1bea28jsn7dc204953838",
    'x-rapidapi-host': "sky-scrapper.p.rapidapi.com"
}

conn.request("GET", f"/api/v1/flights/searchAirport?query={cidade}&locale=pt-BR", headers=headers)

res = conn.getresponse()
data = res.read()

search_airport = json.loads(data.decode("utf-8"))

#print(json.dumps(search_airport, indent =4))
search = search_airport['data'][0]
search_title = search['presentation']
timestamp = search_airport['timestamp']

timestamp_s = timestamp / 1000
data_hora = datetime.datetime.fromtimestamp(timestamp_s)
extracao = data_hora.strftime('%d-%m-%Y %H:%M:%S')

entityId = search['entityId']
title = search_title['title']

print("O identificador do aeroporto é: ",entityId)
print("O nome do aeroporto e: ",title)
print("A hora da extração foi: ",extracao)