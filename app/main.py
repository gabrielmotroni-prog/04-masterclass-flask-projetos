# inicia a aplicacao usando __init__.py para construi o app ( pois __init__.py tem a funcao create_app )
#esse arquivo fica na raiz do projeto - fora da pasta app
from app import create_app

#create_app returna um app ja construido
app = create_app()

if __name__ == '__main__':
    #verificao que n deixa outros arquivos importarro que vem abaixo
    app.run(debug=True)
