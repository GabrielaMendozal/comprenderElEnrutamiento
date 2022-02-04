from flask import Flask

app = Flask (__name__)


@app.route('/', methods = ['GET'])
def saludo():
    return "¡Hola Mundo!"


@app.route('/dojo', methods = ['GET'])
def dojo():
    return "¡Dojo!"

@app.route('/say/<nombre>', methods = ['GET'])
def nombre(nombre):
    return "¡Hola, " + nombre + " !"







if __name__ =="__main__":
    app.run (debug = True )