'''o flask trabalha com conceito funk view - cada funcao @app.route em uma view,
cada uma gera um retorno. Por isso o arquivo chamado "views" nos modulos.
'''

'''
pense nas blueprint como modulos, imagine elas como se fossem controllers da nossa aplicacao mvc. 
E para cada modulo existe suas respetivas funcoes que são representadas como views 
'''

#bibliotecas necessaioas para esse modulo
from datetime import timedelta
from flask import render_template, redirect, url_for, flash

from werkzeug.security import generate_password_hash, check_password_hash # gerador / verificador das senhas
from flask_login import (login_user, logout_user, login_required)

from app.forms import LoginForm, RegisterForm
from app.models import  User
from app import  db

#importanto a blueprint (trocamos app.route -> auth.route)
from . import auth

# todas rotas que represetam auth - autenicacao

@auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():  # form valido e post, entao:

        user = User()
        user.name = form.name.data
        user.email = form.email.data
        # criptogrando a senha com hash ao guardar no banco de dados
        # assim que enviamos as senhas para o banco de dados para um hacker nao ter acesso a essa informacao
        user.password = generate_password_hash(form.password.data)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for("index"))

    return render_template("register.html", form=form)

@auth.route("/login", methods=["GET", "POST"])
def login():
    # esse form eh retornado junto ao render template
    form = LoginForm()

    # valida o the CSRF token is missing. Valida o token enviado pelo form.csrf_token
    if form.validate_on_submit():
        # acionado via postdo formulario tentativa de login

        # agora pegamos os dados pelo form, nao mais pelo request
        user = User.query.filter_by(email=form.email.data).first()

        # verifica se usuario existe
        if not user:
            flash("Credenciais incorretas", "danger")
            return redirect((url_for("login")))

        # verifica a senha
        if not check_password_hash(user.password, form.password.data):
            flash("Credenciais incorretas", "danger")
            return redirect((url_for("login")))

        # se for bem sucedido
        # remeber = vem do html true ou false
        # duration: uso biblioteca datime time para ajudar converter em dias
        # eh o tempo de sessao - para o servidor permanecer a sessar por 7 dias no caso
        login_user(user, remember=form.remember.data,
                    duration=timedelta(days=7))
        return redirect(url_for("index"))

    return render_template("login.html", form=form)

@auth.route("/logout")
def logout():
    # metodo importando la em cima com flasklogin
    logout_user()
    return redirect(url_for("index"))
