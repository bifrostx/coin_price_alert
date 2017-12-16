import coin_price_api

cny_rate = coin_price_api.get_cny_rate()


def get_total():
    tokens = {'btc': 2.34641,
                 'bcx': 19824.096,
                 'sbtc': 2.6041,
                 'eth': 24.2696,
                 'eos': 2635.9394,
                 'qtum': 400.9,
                 'bch': 0.724,
                 'bcd': 19.74}
    total = 0

    for token, amount in tokens.items():
        total += coin_price_api.usd_rate_of_token(token) * amount * cny_rate

    print("You now have %f CNY. " % total)
    return total