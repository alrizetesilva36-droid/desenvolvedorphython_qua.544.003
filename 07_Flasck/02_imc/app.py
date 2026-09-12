from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/imc", methods = ['GET', 'POST'])
def calcular_imc():
    nome = None
    massa = None
    altura = None
    imc = None
    diagnosrico = None
    result = ""
    if request.method == "POST":
        nome = request.form.get("nome",0.0)
        massa = float(request.form.get("massa","").replace(",","."))
        altura = float(request.form.get("altura",0.0).replace(",","."))
        imc = massa/(altura**2)

        if imc < 15.5:
            diagnostico = "Você está abaixo do peso ideal."
        elif imc  < 25:
            diagnostico = "Voce esta no peso ideal."
        elif imc  < 30:
            diagnostico = "Voce esta acima do peso."
        elif imc < 35:
            diagnostico = "Voce esta obeso."
        elif imc < 40:
            diagnostico = "voce esta com obesidade nivel 2."
        else:
            diagnostico = "Voce esta com obesidade morbida"      

        result = f"{nome}, seu IMC é {imc:.2f}. {diagnostico}"

    return render_template('index.html',result=result)



if __name__ == "__main__":
    app.run(debug=True)