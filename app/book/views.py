
#rotas referente a livro

from flask import render_template, redirect, url_for, flash

from app.forms import  BookForm
from app.models import Book
from app import db

from flask_login import current_user

from . import book

#importanto a blueprint (trocamos app.route -> book.route)
@book.route("/book/add", methods=["GET", "POST"])
def book_add():
    form = BookForm()

    #se o form passar nas validacoes
    if form.validate_on_submit():
        book = Book()
        book.name = form.name.data

        db.session.add(book)
        db.session.commit()

        flash("Livro cadastro com sucesso.", "success")
        return redirect(url_for(".book_add"))

    return render_template("book/add.html", form=form)