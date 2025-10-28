from models import db
from app import app
from eralchemy2 import render_er

# Generar el diagrama UML
with app.app_context():
    render_er(db.Model, 'diagram.png')

print("✅ Diagrama UML generado correctamente: diagram.png")
