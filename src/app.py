from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)


#Conexion a la base de datos usa "sqlite" por defecto
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db= SQLAlchemy(app)
MIGRATE = Migrate(app,db)

#Importamos los modelos 
from models import Users, Post, Comment, Followers


#Ruta de prueba
@app.route('/')
def hello():
    return("Hola ! la API de instagram model esta funcionando")


if __name__ == '__main__':
    app.run(debug=True)
