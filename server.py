from flask import Flask, render_template

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

@app.route('/repeat/<int:num>/<string:palabra>')
def repeat_word(num, palabra):
    output = ""
    for i in range (0,num):
        output += f" {palabra} "
    return output
    



if __name__ =="__main__":
    app.run (debug = True )