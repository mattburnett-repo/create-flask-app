def generate_base_template(app_name):
    return """<!doctype html>\n
      <html lang=\"en\">\n
        <head>\n  
          <meta charset=\"utf-8\">\n  
          <title>{% block title %}{{ app_name }}{% endblock %}</title>\n
          <script src="https://cdn.tailwindcss.com"></script>\n
        </head>\n
        <body class="bg-gray-50 text-gray-900 font-sans">\n
            <!-- Navigation Bar -->
            {% include "./components/_navbar.html" %}\n

            <!-- Flash Messages -->
            {% include "./components/_flashMsgDisplay.html" %}\n

            <!-- Main Content -->
            <div class="py-12">\n
                <div class="max-w-7xl mx-auto sm:px-6 lg:px-8">\n
                    {% block content %}\n
                    {% endblock %}\n
                </div>\n
            </div>\n
        </body>\n
      </html>"""
