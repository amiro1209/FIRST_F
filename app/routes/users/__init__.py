from .usersHandler import user_bp

def setup_routes(app):
    app.register_blueprint(user_bp)
