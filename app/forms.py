# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Length, Email, DataRequired

#classe responsavel pelo form, a qual vai herdar de FlaskForm. Cria os fields
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

