#Azul23
import requests
import json

url = "https://api.imagga.com/v2/tags"

querystring = {"image_url":"https://th.bing.com/th/id/OIP.eLRPJx7w3bvn2aFnuyYGcwHaJe?pid=ImgDet&rs=1"}

headers = {
    'accept': "application/json",
    'authorization': "Basic ur api key"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
data = json.loads(response.text.encode("ascii"))

for i in range(6):
    tag = data["result"]["tags"][i]["tag"]["en"]
    print(tag)
