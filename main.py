from evento.evento_routes import eventoRoutes
from usuario.usuario_routes import usuarioRoutes
from palestra.palestra_routes import palestraRoutes
from minicurso.minicurso_routes import minicursoRoutes
from flask import Flask

app = Flask(__name__)
app.register_blueprint(usuarioRoutes)
app.register_blueprint(eventoRoutes)
app.register_blueprint(palestraRoutes)
app.register_blueprint(minicursoRoutes)

print("Lista de Rotas:")
for rule in app.url_map.iter_rules():
    print(rule)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)