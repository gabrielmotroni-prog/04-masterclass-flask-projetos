# inicia a aplicacao usando __init__.py para construi o app ( pois __init__.py tem a funcao create_app )
#esse arquivo fica na raiz do projeto - fora da pasta app
from app import create_app
import os

#-------------variavel de ambiente
from dotenv import load_dotenv
load_dotenv()
MY_ENV_VAR = os.getenv('MY_ENV_VAR')
print(MY_ENV_VAR)
#--------------- 

#create_app returna um app ja construido
app = create_app()


if __name__ == "__main__": 
    #verificao que n deixa outros arquivos importarro que vem abaixo
    #local
    app.run(debug=True)
    #heroku
    #port = int(os.environ.get("PORT", 5000))
    #app.run(host='0.0.0.0', port=port,debug=True)