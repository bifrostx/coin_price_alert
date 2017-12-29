# -*- coding: utf-8 -*-
import sys, time
from send_email import send_email
from coin_price import get_assets
from visualize import generate_html

"""
after excute coin_price.py, the final version will be at this form:
['Symbol', 'Price', 'Date', 'Time', 'Volume', 'Sub Total']
"""
tokens = [{'Symbol': 'btc', 'Volume': 2.34641},
          {'Symbol': 'eth', 'Volume': 24.2696},
          {'Symbol': 'eos', 'Volume': 2635.9394},
          {'Symbol': 'qtum', 'Volume': 400.9},
          {'Symbol': 'bch', 'Volume': 0.724},]


if __name__ == '__main__':
    csv_file_name = 'assets.csv'

    # basic email heads
    from_addr = 'bifrost_xin@163.com'
    to_addr_list = ['bifrost_xin@163.com', 'cindy881216@126.com']
    subject = "资产报告"
    files = ['render.html',]

    while True:
        total = 0
        current_assets = get_assets(csv_file_name, tokens)
        generate_html(csv_file_name)
        for token in tokens:
            total += token['Sub Total']
        content = '''你目前的总资产为：{0}美元。'''.format(total)
        send_email(from_addr, to_addr_list, subject, content, files)
        print("Waiting for sending the next email tomorrow.")
        for i in range(0, 100):
            sys.stdout.write('#')
            sys.stdout.flush()
            time.sleep(24 * 36)     # every (24 hours * 3600 seconds/hour / 100) seconds print one '#'


