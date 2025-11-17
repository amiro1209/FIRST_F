from .usersHandler import register_bp ,forgot_bp ,reset_bp ,login_bp

def setup_routes(app):
    app.register_blueprint(register_bp)
    app.register_blueprint(forgot_bp)
    app.register_blueprint(reset_bp)
    app.register_blueprint(login_bp)
    
   