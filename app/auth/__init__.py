#auth -> autenticao
#modulo sobre rotas de autenticao
from flask import Blueprint
                 #nome da blueprint / __name__ eh o mesmo usando para iniciar o app flask
auth = Blueprint("auth", __name__)

#import as views (rotas) desse modulo auth
from . import views