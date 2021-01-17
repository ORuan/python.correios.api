#!/usr/bin/python3
import flask, os, json
from flask import request, jsonify
from controller import SearchCorreios



app = flask.Flask(__name__)
app.debug = True
print('')
print('[*] É provavel que um diretório driver seja criado, não se precoupes')
print('[*] Para usar a API digite no browser')
print('--> http://localhost:5000/?code={codigo-rastreio}\n')

@app.route('/', methods=['GET'])
def query_bot():
    code = request.args['code']
    search = SearchCorreios(code)
    response = search.selenium_get_code()
    return response

app.run()