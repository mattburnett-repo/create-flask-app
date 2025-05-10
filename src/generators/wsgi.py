def generate_wsgi():
    return "from app import create_app\n\napp = create_app()\n"
