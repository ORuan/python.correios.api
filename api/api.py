import flask, os
from flask import request, jsonify
from selenium_controller import SearchCorreios


app = flask.Flask(__name__)
print('[*]:É provavel que um diretório driver seja criado, não se precoupe\n')
print('[*]:Para usar a API digite: no browser\n')
print('http:localhost:5000/?code={code}\n')

@app.route('/', methods=['GET'])
def query_bot():
    code = request.args['code']
    search = SearchCorreios(code)
    response = search.selenium_get_code()
    return response

app.run()