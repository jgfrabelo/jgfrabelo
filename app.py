from flask import Flask, render_template, request,make_response, jsonify
import os
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/test")
def test():
    state = request.args.get('state')  # solicita o estado (vem do index.html (javascript,jquery))
    s = {"led": state}
    print("s= ", s, type(s))
    fname = os.path.join(app.static_folder, "json\sample.json") # caminho do arquivo sample.json
    with open(fname, "w") as outfile:  # abre arquivo no modo escrever
        json.dump(s, outfile)  # transforma dicionario python s{} em json, que é salvo no arquivo sample.json
    return "success"

'''
@app.route("/test_", methods=["POST"])
def test():
    output = request.get_json()
    s = json.loads(output) #this converts the json output to a python dictionary
    print("s= ", s, type(s)) # Printing the new dictionary
    fname = os.path.join(app.static_folder, "json\sample.json")  # caminho do arquivo sample.json
    with open(fname, "w") as outfile:  # abre arquivo no modo escrever
        json.dump(s, outfile)  # transforma dicionario python s{} em json, que é salvo no arquivo sample.json
    return "success"
'''

@app.route("/read",methods=['GET'])
def read():
    fname = os.path.join(app.static_folder, "json\sample.json") #caminho do arquivo sample.json
    with open(fname, "r") as openfile: #abre o arquivo no modo leitura
        json_obj = json.load(openfile) #transforma arquivo json em dicionario python
        print("Estado= ", json_obj['led'])
    #return json_obj['led'] #retorna com o estado 'on' ou 'off'
    return make_response(json_obj['led'])


@app.route("/ler")
def ler():
    return render_template("ler.html")


if __name__ == '__main__':
    #app.run(host="192.168.100.2", port=5000)
    app.run(host="192.168.0.17", port=5000)
    #app.run(host='0.0.0.0')
