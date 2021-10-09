from app import  db, login_manager
from flask_login import UserMixin

#huck
@login_manager.user_loader
#vai sempre lidar/ me dar o usuario logado
def current_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin): #herdamos UserMixin para facilitar; ele eh uma interface que herdamos ja trazendo os metodos obrgatorio pelo flask-login
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(84), nullable=False)
    # unique-unico: nao posso criar dois email iguais
    #index= quando fizer uma pesquisa no bd ela sera pouco mais performatica pq permiti indexacao
    email = db.Column(db.String(84), nullable=False, unique=True, index=True)
    password = db.Column(db.String(255), nullable=False)
    profile = db.relationship('Profile', backref='users', uselist=False) #faz a conexao

class Profile(db.Model): #perfil
    __tablename__ = "profiles"
    id = db.Column(db.Integer, primary_key=True)
    photo = db.Column(db.Unicode(2124), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    

#representacao do objeto - toda vez que instancia essa classse ele nao vem com referencia da memoria, 
#mas sim o atributo == toString
    def __str__(self):
        return self.name

