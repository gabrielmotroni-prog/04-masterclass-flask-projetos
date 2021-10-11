
#todas importacoes necessarias para essas rotas
from app.models import User, Book
from app import db
from app.forms import  UserBookForm # import class LoginForm

from flask import render_template, redirect, url_for, flash
from flask_login import (login_required, current_user)

#importanto do blueprint
from . import user

#lista de usuarios
@user.route("/")
def index():
    users = User.query.all()# select * from users
    return render_template("users.html", users=users)

#deleta usuarios
@user.route("/user/delete/<int:id>")
def delete(id): # recebo o parametro pela rota
    #primeiro encontra o usuario
    user = User.query.filter_by(id=id).first()
    db.session.delete(user) #seta
    db.session.commit()#escreve no banco de dados

    return redirect("/")

#consulta um usuario
@user.route("/user/<int:id>")
@login_required # declara que somente usuario logado tem acesso a essa rota
def unique(id):
    user = User.query.get(id) # com id podemos usar filter_by ou get: que compara um resultado unico
    return render_template("user.html", user=user)



#rota responsavel por fazer relacao ente livros e usuario
@user.route("/user/<int:id>/add-book", methods=["GET", "POST"])
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
        return redirect(url_for(".user_add_book", id=current_user.id)) # retorna para mesma pagina referente o msm usuario

    return render_template("book/user_add_book.html", form=form)