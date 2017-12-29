import os, time, csv
import coin_price_api


def get_assets(filename, tokens):

    for token in tokens:
        token['Date'] = time.strftime("%Y-%m-%d", time.localtime())
        token['Time'] = time.strftime("%H:%M:%S", time.localtime())
        token['Price'] = coin_price_api.usd_rate_of_token(token['Symbol'])
        token['Sub Total'] = token['Price'] * token['Volume']

    headers = ['Symbol', 'Price', 'Date', 'Time', 'Volume', 'Sub Total']

    if os.path.exists(filename):
        print("csv file already exists...")
        with open(filename, 'a', newline='') as f:
            f_csv = csv.DictWriter(f, headers)
            f_csv.writerows(tokens)
            print("Update complete.")
    else:
        print("csv file does not exists...")
        with open(filename, 'w', newline='') as f:
            f_csv = csv.DictWriter(f, headers)
            f_csv.writeheader()
            f_csv.writerows(tokens)
            print("Create file and update complete.")

    return tokens
