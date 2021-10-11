#modulo sobre rotas de book
#blueprint chama as views (as rotas)

'''
pense nas blueprint como modulos, imagine elas como se fossem controllers da nossa aplicacao mvc. 
E para cada modulo existe suas respetivas funcoes que são representadas como views 
'''

from flask import Blueprint
                 #nome da blueprint / __name__ eh o mesmo usando para iniciar o app flask
book = Blueprint("book", __name__)

#import as views (rotas) desse modulo auth
from . import views