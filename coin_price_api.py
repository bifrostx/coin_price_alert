import requests
import json
from decimal import *

API_BASE = "https://api.coinmarketcap.com/v1/ticker/"


def get_coin_data(id):
    r = requests.get(API_BASE + id)
    d = json.loads(r.text)[0]
    print("Succeeded in getting Coin data.")
    return d
	

def usd_rate_of_token(id):
	d = get_coin_data(id)

	print("Succeeded in getting usd price of %s." % id)
	return float(d['price_usd'])
	
	
if __name__ == "__main__":
	d = usd_rate_of_token("eos")
	print(d)