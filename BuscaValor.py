import http.client
import json
from datetime import datetime

#Definição de variaveis para conn.request
originEntityId = 27539772 #Origem do embarque
destinationEntityId = 104120223 #Destino da viagem
boarding = '2025-07-21' #Data do embarque
turn = '2025-07-26' #data do retorno

conn = http.client.HTTPSConnection("sky-scrapper.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "2357b19b61msh74ab90a94f75bc5p1bea28jsn7dc204953838",
    'x-rapidapi-host': "sky-scrapper.p.rapidapi.com"
}

conn.request("GET", f"/api/v2/flights/searchFlightsWebComplete?originSkyId=BRL&destinationSkyId=SCA&originEntityId={originEntityId}&destinationEntityId={destinationEntityId}&date={boarding}&returnDate={turn}&cabinClass=economy&adults=2&sortBy=price_high&currency=BRL&market=pt-BR&countryCode=BR", headers=headers)
res = conn.getresponse()
data = res.read()

# Converte a resposta para JSON
flight_data = json.loads(data.decode("utf-8"))
# Verifica se existe um timestamp
if 'itineraries' in flight_data['data']:
    # Extrair todos os itinerários
    itineraries = flight_data['data']['itineraries']   
    # Ordenar os itinerários pelo preço mais barato (chave 'raw')
    sorted_itineraries = sorted(itineraries, key=lambda x: x['price']['raw'])  
    # Limitar para os 10 voos mais baratos
    cheapest_itineraries = sorted_itineraries[:1]  
        

    for idx, itinerary in enumerate(cheapest_itineraries, start=1):
        price = itinerary['price']
        first_leg = itinerary['legs'][0]
        first_segment = first_leg['segments'][0]
        marketing_carrier = first_leg['carriers']['marketing'][0]['name']
        departure_time = first_segment['departure']
        arrival_time = first_segment['arrival']

        print(f"Voo {idx}:")
        print("Preço raw:", price['raw'])
        print("Preço formatado:", price['formatted'])
        print("Origem:", first_segment['origin']['name'])
        print("Destino:", first_segment['destination']['name'])
        print("Companhia aérea:", marketing_carrier)
        print("Horario de saída",departure_time)
        print("Horario de chegada:",arrival_time)
        print("-" * 30)
else:
    print("Nenhum itinerário encontrado.")