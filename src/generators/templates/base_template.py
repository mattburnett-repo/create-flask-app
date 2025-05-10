def generate_base_template():
    return """<!doctype html>
<html lang=\"en\">\n<head>\n  <meta charset=\"utf-8\">\n  <title>{% block title %}My Flask App{% endblock %}</title>\n</head>\n<body>\n  {% include 'components/_header.html' %}\n  {% include 'components/_navBar.html' %}\n  <main>{% block content %}{% endblock %}</main>\n</body>\n</html>"""
