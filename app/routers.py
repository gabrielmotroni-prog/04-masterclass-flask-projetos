#todos imports necessarios paras routers

from datetime import timedelta

from flask import render_template, redirect, url_for, flash
from flask_login import (login_user, logout_user, login_required, current_user)
from werkzeug.security import generate_password_hash, check_password_hash # gerador / verificador das senhas

from app.models import User, Book
from app import db
from app.forms import LoginForm, RegisterForm, BookForm, UserBookForm # import class LoginForm


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
        form = RegisterForm()

        if form.validate_on_submit():

            user = User()
            user.name= form.name.data  
            user.email= form.email.data
            #criptogrando a senha com hash ao guardar no banco de dados
            #assim que enviamos as senhas para o banco de dados para um hacker nao ter acesso a essa informacao
            user.password= generate_password_hash(form.password.data)
            
            db.session.add(user)
            db.session.commit()

            return redirect(url_for("index"))

        return render_template("register.html",form=form)

    @app.route ("/login", methods=["GET", "POST"])
    def login():
        #esse form eh retornado junto ao render template
        form = LoginForm() 
        
        # valida o the CSRF token is missing. Valida o token enviado pelo form.csrf_token
        if form.validate_on_submit(): 
            #acionado via postdo formulario tentativa de login

                # agora pegamos os dados pelo form, nao mais pelo request
                user = User.query.filter_by(email=form.email.data).first()

                #verifica se usuario existe
                if not user :
                    flash("Credenciais incorretas", "danger")
                    return redirect((url_for("login")))
                
                #verifica a senha
                if not check_password_hash(user.password, form.password.data) :
                    flash("Credenciais incorretas", "danger")
                    return redirect((url_for("login")))

                # se for bem sucedido
                #remeber = vem do html true ou false
                #duration: uso biblioteca datime time para ajudar converter em dias
                # eh o tempo de sessao - para o servidor permanecer a sessar por 7 dias no caso
                login_user(user, remember=form.remember.data, duration=timedelta(days=7))
                return redirect(url_for("index"))

        return render_template("login.html", form=form)

    @app.route("/logout")
    def logout():
        #metodo importando la em cima com flasklogin
        logout_user()
        return redirect(url_for("index"))

    @app.route("/book/add", methods=["GET", "POST"])
    def book_add():
        form = BookForm()

        #se o form passar nas validacoes
        if form.validate_on_submit():
            book = Book()
            book.name = form.name.data

            db.session.add(book)
            db.session.commit()

            flash("Livro cadastro com sucesso.", "success")
            return redirect(url_for("book_add"))

        return render_template("book/add.html", form=form)

    #rota responsavel por fazer relacao ente livros e usuario
    @app.route("/user/<int:id>/add-book", methods=["GET", "POST"])
    def user_add_book(id):
        form = UserBookForm()
        
        #valida form - CSRF e post
        if form.validate_on_submit():
            #procura se livro existe
            book = Book.query.get(form.book.data)
            print(form.book.data)
            print(current_user.name)
            #adiciona livro ao usuario
            #com current_user nao precisamos criar instacia de User pois o proprio current ja tem referencia de user
            #usamos append pois o current ja eh um conjuto de proproedades nome, email, senha e livros do usuario
            current_user.books.append(book)
            db.session.add(current_user)
            db.session.commit()

            flash("Livro cadastro com sucesso.", "success")
            return redirect(url_for("user_add_book", id=current_user.id)) # retorna para mesma pagina referente o msm usuario

        return render_template("book/user_add_book.html", form=form)