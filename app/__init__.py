#arquivo criador/construtor do meu app (funcao create_app)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

                                                      
#repare que esse arquivo app esta dentro da pasta app
# quem fica no arquivo raiz agr eh o main.py

#sqlacemy recebe o app como parameto
db = SQLAlchemy() 

#parte de login
login_manager = LoginManager()
#flask login exige a instalcao do metodos na classe, porem se herdamos usermix ele faz isso pra nos

#factory function - construtor do nosso app
def create_app():
    app = Flask(__name__) #name nome da funcao => __name__ eh uma feacture que pega o nome desse modulo/aplicacao de forma dinamica
    # isso tbm eh necessario criptgrafar com hash em producao
    app.config["SECRET_KEY"] = 'secret' 
    #tipo do banco de dados
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db" 
    #tira o erro warning
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    #antes isso era feito la em agr eh feito aqui dentro passando aos contrutores de cada coisa o app
    db.init_app(app) # passando ao contrutor de db o app
    login_manager.init_app(app) #passasndo ao contrutor de login_manager o app

    #importando as rotas para o app para ele carregar as rotas
    from app import routers
    routers.init_app(app) #passa o app para o construtor de routes

    #retorna o nosso proprio app construido
    return app
