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
        'AMOUNT': para['Value'],
        'AMOUNT_CNT': para['Nominal'],
    }


dict_curr = ['USD', 'EUR', 'PLN', 'BYN']  # TODO add new curruncy KZT


def main():
    a = b.call(
        'crm.currency.update',
        [{'ID': x,
         'fields':
             get_currency(x),
         } for x in dict_curr]
    )


if __name__ == '__main__':
    while True:
        now = datetime.now()
        print(now.hour)
        if now.hour == 6 or now.hour == 22:
            #функция для проверки
            main()
        sleep(1)
