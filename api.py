from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if(request.method == "GET"):
        return render_template("index.html")
    else:
        if(request.form["n1"] != "" and request.form["n2"] != ""):
            n1 = request.form["n1"]
            n2 = request.form["n2"] 

            if(request.form["option"] == "soma"):
                soma = int(n1) + int(n2)
                return str(soma)
            elif (request.form["option"] == "subtracao"):
                subtracao = int(n1) - int(n2)
                return str(subtracao)
            elif (request.form["option"] == "multiplicacao"):
                multiplicacao = int(n1) * int(n2)
                return str(multiplicacao)
            elif (request.form["option"] == "divisao"):
                divisao = int(n1) / int(n2)
                return str(divisao)
            else:
                return render_template("error.html")
@app.errorhandler(404)
def not_found(error):
    return render_template("error.html")

app.run(port=8080, debug=True)                      



