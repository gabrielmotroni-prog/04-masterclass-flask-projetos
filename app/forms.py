# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import Length, Email, DataRequired
from app.models import Book

#classe responsavel pelo form, a qual vai herdar de FlaskForm. Gera o form e sseus campos.
#inserimos aquis os campos e as valicacoes dos campos.
class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[
        Email("E-mail Invalido") # eu coloco um conjunto de classe que validam algo espefico. ex Email, tamanho
        ])
    password = PasswordField("Senha",  validators=[ 
            Length(3, 6, "O campo deve conter entre 3 a 6 caracteres.")
        ])
    remember = BooleanField("Permanecer Conectado")
    submit = SubmitField("Logar")

class RegisterForm(FlaskForm):
    name = StringField("Nome Completo", validators=[
        DataRequired("O campo e obrigatorio")])
    email = EmailField("Email", validators=[
        Email("E-mail Invalido") # eu coloco um conjunto de classe que validam algo espefico. ex Email, tamanho
        ])
    password = PasswordField("Senha",  validators=[ 
            Length(3, 6, "O campo deve conter entre 3 a 6 caracteres.")
        ])
    submit = SubmitField("Cadastrar")

class BookForm(FlaskForm):
    name = StringField("Nome do livro", validators=[
        DataRequired("Esse Campo e obrigatorio"),
        Length(1,125,"Minimo 1 e no maximo 125 caracteres")
    ])
    submit = SubmitField("Cadastrar")

class UserBookForm(FlaskForm):
    #input select
    book = SelectField("Livro",
    coerce=int) #informa que trabalharemos com valores do tipo inteiro

    #botao enviar
    submit = SubmitField("Salvar")
    
    #construtor
    #toda vez que essa classe for instacianda em routers, esse __init__ vai ser chamado primeiro
    # quando construtor for acionado, altere as opcoes do select 'book' para os registros do banco de dados
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.book.choices = [  #choices sempre esquema que as opcoes sejam TUPLAS
            #cria uma tupla para cada volta no laco for
            #compreensao de listas
            (book.id, book.name) for book in Book.query.all()
        ]

 

