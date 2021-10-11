from app.auth import auth as auth_blueprint # colocamos um 'as' para melhorar identificar o blueprint
from app.book import book as book_blueprint # colocamos um 'as' para melhorar identificar o blueprint
from app.user import user as user_blueprint # colocamos um 'as' para melhorar identificar o blueprint


#atraves desse codigo que recebe o proprio app eu consigo fazer o registro/manipular das rotas aqui 
#o app seria todo o modulo ( a pasta que contem o mvc)
def init_app(app): 
    # pedido ao app registrar meu novo modulo blueprints auth com as rotas referente a autenticao
    app.register_blueprint(auth_blueprint)

    # pedido ao app registrar meu novo modulo blueprints book com as rotas referente a book
    app.register_blueprint(book_blueprint)

    # pedido ao app registrar meu novo modulo blueprints user com as rotas referente a user
    app.register_blueprint(user_blueprint)

  