from flask import Flask
from flask_cors import CORS
from evento.evento_routes import eventoRoutes
from usuario.usuario_routes import usuarioRoutes
from palestra.palestra_routes import palestraRoutes
from minicurso.minicurso_routes import minicursoRoutes

# Criação da aplicação Flask
app = Flask(__name__)

# Configuração do CORS para permitir requisições de qualquer origem
CORS(app, resources={r"/*": {"origins": "*"}}, methods=["GET", "POST", "PUT", "DELETE"], allow_headers=["Content-Type", "Authorization"])

# Registro dos blueprints
app.register_blueprint(usuarioRoutes, url_prefix='/usuario')
app.register_blueprint(eventoRoutes, url_prefix='/evento')
app.register_blueprint(palestraRoutes, url_prefix='/palestra')
app.register_blueprint(minicursoRoutes, url_prefix='/minicurso')

# Exibe a lista de rotas registradas no servidor
print("Lista de Rotas:")
for rule in app.url_map.iter_rules():
    print(f"{rule} -> {rule.endpoint}")

# Inicializa o servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
