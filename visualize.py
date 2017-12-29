# -*- coding": utf-8 -*-
import csv
from pyecharts import ThemeRiver


def get_csv_data(filename):
    data = []
    with open(filename, 'r') as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            d = []
            d.append(row['Date'])
            sub_total = float(row['Sub Total'])
            d.append(sub_total)
            d.append(row['Symbol'])
            data.append(d)
        return data


def generate_html(filename):
    data = get_csv_data(filename)
    legend = []
    for i in data:
        legend.append(i[2])

    tr = ThemeRiver("Crypto Currency")
    tr.add(legend, data, is_label_show=True)
    tr.render()
    print("plot generated.")