from flask import Flask, render_template, flash
from datetime import datetime
from filters import format_date #importanto meu filter personalizado

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret" # precisamos parar poder criar sessao e usar flash
# passando ao jinja meu filter personalizado importante 
app.jinja_env.filters["formatdate"] = format_date 



@app.route("/templates")
def templates ():
    #render tempalte: chama o html
    #1 parametro: nome do arquivo do template
    # jinja so acha templates na pasta templastes


    #uma segnda forma de enviar mensagem atraves de template( 1sessoes 2 flash)
    #forma dinamica de trababalhar com os tempaltes
    flash("usuario criado com sucesso")
    if 1 !=2:
        flash("passei aqui", category="warning")

                                       #template / objeto local
    return render_template("index.html")

@app.route("/users")
def users():            # habilitando e mandando a categoria
    flash("users route",category="success")

    users = [{
        "name":"marcus",
        "age":99,
        "email":"oi@gmail.com",
        "active":True,
        "since": datetime.utcnow()
            },
         {"name":"maria",
        "age":18,
        "email":"maria@gmail.com",
        "active":False,
        "since": datetime.utcnow()
            },
        {"name":"joao",
        "age":25,
        "email":"joao@gmail.com",
        "active":True,
        "since": datetime.utcnow()
            }
        ]

    user_page = False

    return render_template("users.html", users=users, user_page=user_page)

#essa linha abaixo serve para: o arquivo que importar app.py nao podera executar os codigdos abaixo
if __name__ == "__main__":
    app.run(debug=True)