# -*- coding: utf-8 -*-
import sys, time
from send_email import send_email
from coin_price import get_assets


"""
after excute coin_price.py, the final version will be at this form:
['Symbol', 'Price', 'Date', 'Time', 'Volume', 'Sub Total']
"""
tokens = [{'Symbol': 'btc', 'Volume': 2.34641},
          {'Symbol': 'bcx', 'Volume': 19824.096},
          {'Symbol': 'sbtc', 'Volume': 2.6041},
          {'Symbol': 'eth', 'Volume': 24.2696},
          {'Symbol': 'eos', 'Volume': 2635.9394},
          {'Symbol': 'qtum', 'Volume': 400.9},
          {'Symbol': 'bch', 'Volume': 0.724},
          {'Symbol': 'bcd', 'Volume': 19.74},]


if __name__ == '__main__':

    # basic email heads
    from_addr = 'bifrost_xin@163.com'
    to_addr_list = ['bifrost_xin@163.com', ]
    subject = "资产报告"

    while True:
        total = 0
        current_assets = get_assets('test.csv', tokens)
        for token in tokens:
            total += token['Sub Total']
        content = '''你目前的总资产为：{0}美元。'''.format(total)

        for i in range(0, 100):
            send_email(from_addr, to_addr_list, subject, content)
            print("Waiting for sending the next email tomorrow.")
            sys.stdout.write('#')
            sys.stdout.flush()
            time.sleep(24 * 36)     # every (24 hours * 3600 seconds/hour / 100) seconds print one #

