from flask import Flask, render_template

app = Flask(__name__)

# cria  1° pagina
# route -> caminho  para chegar a pagina
#função -> oque vai exibir na tela

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def  contatos():
    return render_template("contatos.html")

@app.route("/usuarios")
def usuarios():
    return render_template("usuarios.html")




#colocar site no ar
if __name__=="__main__":
    app.run(debug=True)