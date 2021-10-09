#arquivo main da raiz do programa para iniciar nosso programa
from app import create_app
import os

#importanto a criacao do meu app da funcao create_app
app = create_app()

# nada abaixdo dessa funcao sera importado
if __name__ == "__main__": 
    #local
    app.run(debug=True)
    #heroku
    #port = int(os.environ.get("PORT", 5000))
    #app.run(host='0.0.0.0', port=port,debug=True)