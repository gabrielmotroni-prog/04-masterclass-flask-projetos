#todos imports necessarios paras routers

from datetime import timedelta

from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash # gerador / verificador das senhas

from app.models import User
from app import db


#atraves desse codigo que recebe o proprio app eu consigo fazer o registro/manipular das rotas aqui 
#o app seria todo o modulo ( a pasta que contem o mvc)
def init_app(app): 

    #lista de usuarios
    @app.route("/")
    def index():
        users = User.query.all()# select * from users
        return render_template("users.html", users=users)

    #deleta usuarios
    @app.route("/user/delete/<int:id>")
    def delete(id): # recebo o parametro pela rota
        #primeiro encontra o usuario
        user = User.query.filter_by(id=id).first()
        db.session.delete(user) #seta
        db.session.commit()#escreve no banco de dados

        return redirect("/")

    #consulta um usuario
    @app.route("/user/<int:id>")
    @login_required # declara que somente usuario logado tem acesso a essa rota
    def unique(id):
        user = User.query.get(id) # com id podemos usar filter_by ou get: que compara um resultado unico
        return render_template("user.html", user=user)

    @app.route ("/register", methods=["GET", "POST"])
    def register():
        # verifica se a requisicao do usuario eh via post
        if request.method == "POST":
            user = User()
            user.name= request.form['name'] # atraves do request conseguimos pegar os dados do form
            user.email= request.form['email']
            #criptogrando a senha com hash ao guardar no banco de dados
            #assim que enviamos as senhas para o banco de dados para um hacker nao ter acesso a essa informacao
            user.password= generate_password_hash(request.form['password'])
            
            db.session.add(user)
            db.session.commit()

            return redirect(url_for("index"))

        return render_template("register.html")

    @app.route ("/login", methods=["GET", "POST"])
    def login():
        #acionado via postdo formulario tentativa de login
        if request.method == "POST":
            email = request.form['email']
            password = request.form['password']
            remember = request.form['remember']

            print(remember)
            user = User.query.filter_by(email=email).first()

            #verifica se usuario existe
            if not user :
                flash("Credenciais incorretas")
                return redirect((url_for("login")))
            
            #verifica a senha
            if not check_password_hash(user.password, password) :
                flash("Credenciais incorretas")
                return redirect((url_for("login")))

            # se for bem sucedido
            #remeber = vem do html true ou false
            #duration: uso biblioteca datime time para ajudar converter em dias
            # eh o tempo de sessao - para o servidor permanecer a sessar por 7 dias no caso
            login_user(user, remember=remember, duration=timedelta(days=7))
            return redirect(url_for("index"))

        return render_template("login.html")

    @app.route("/logout")
    def logout():
        #metodo importando la em cima com flasklogin
        logout_user()
        return redirect(url_for("index"))