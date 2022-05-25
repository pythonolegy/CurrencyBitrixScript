from bottle import post, run, request

from main import *


# @post('/currency')
# def valid_post_currency():
#     if not valid('currency', request.json):
#         return 'ValidError'
#     try:
#         update_currency_by_key(request.json['currency'])
#         return 'Updated'
#     except RuntimeError:
#         add_currency(request.json['currency'])
#         return 'Added'


@post('/currencies')
def valid_post_currencies():
    if not valid('currencies', request.json):
        return 'ValidError'
    for elem in request.json['currencies']:
        try:
            update_currency_by_key(elem)
        except RuntimeError:
            add_currency(elem)


run(host='localhost', port=8081, debug=True)
