#!flask/bin/python
from flask import Flask
from Savoir.Savoir import Savoir


rpcuser = 'multichainrpc'
##rpcpasswd = 'Fgds4GySQ6AJV7BfP5xEtQjm4dTMZRPJyAPsPKqYVpak'
rpcpasswd = '7LKra1Cso4TnWzQKhQbMYPmJRu9S2TiD6JuN9DYNzB1L'
rpchost = 'localhost'
rpcport = '8366'
chainname = 'chain'
api = Savoir(rpcuser, rpcpasswd, rpchost, rpcport, chainname)

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)