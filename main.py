from time import sleep

import requests

from datetime import datetime

from fast_bitrix24 import Bitrix


webhook = 'https://b24-xlxcp4.bitrix24.ru/rest/1/tscp6l1psv3emwmq/'
b = Bitrix(webhook)

root = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
curr = root.json()


def get_currency(currency):
    para = curr['Valute'][currency]
    return {
        'CURRENCY': para['CharCode'],
        'AMOUNT': para['Value'],
        'AMOUNT_CNT': para['Nominal'],
    }


dict_curr = ['USD', 'EUR', 'PLN', 'BYN']


def main():
    b.call(
        'crm.currency.update',
        [{'ID': x,
          'fields':
              get_currency(x),
          }for x in dict_curr]
    )
    return 'Ok'


def add_currency_by_key(data):
    b.call(
        'crm.currency.add',
        [{
            # 'ID': x,
            'fields': get_currency(data)
        } for x in data]
    )


def add_currency_by_keys(data):
    b.call(
        'crm.currency.add',
        [{'ID': x,
          'fields':
              get_currency(x),
          } for x in data["currencies"]]
    )


def update_currency_by_key(data):
    b.call(
        'crm.currency.update',
        {
            'ID': data,
            'fields': get_currency(data)
        }
    )


def update_currency_by_keys(data):
    b.call(
        'crm.currency.update',
        [{'ID': x,
          'fields':
              get_currency(x),
          } for x in data["currencies"]]
    )


def add_currency(currency):
    para = curr['Valute'][currency]
    b.call(
        'crm.currency.add',
        {
            'fields': {
                "CURRENCY": para['CharCode'],
                'AMOUNT': para['Value'],
                'AMOUNT_CNT': para['Nominal'],
            }
        }
    )
    return 'Ok'


# def get_currency_by_key(data):
#     b.call(
#         'crm.currency.get',
#         {
#             'ID': data['currency'],
#             'fields': get_currency(data['currency'])
#         }
#     )

def get_currency_by_key(data):
    b.call(
        'crm.currency.get',
        {
            'ID': data['currency'],
            'fields': get_currency(data)
        }
    )

def get_currency_list():
    x = b.call(
        'crm.currency.list',
        {}
    )
    return x


def valid(x, y):
    return x in y


if __name__ == '__main__':
    while True:
        now = datetime.now()
        print(now.hour)
        if now.hour == 6 or now.hour == 22:
            main()
        sleep(1)
