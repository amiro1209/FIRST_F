from .users.handler import user_bp
from .templates.handler import templates_bp

def setup_routes(app):
    app.register_blueprint(user_bp)
    app.register_blueprint(templates_bp)
