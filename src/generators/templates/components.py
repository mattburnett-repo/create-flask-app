def generate_component_templates(path, blueprint_list=None, app_name=None):
    """
    Generate component templates based on the path.
    """
    if path.endswith("_navbar.html"):
        return generate_navbar(blueprint_list, app_name)
    elif path.endswith("_flashMsgDisplay.html"):
        return generate_flash_messages()
    return ""

def generate_navbar(blueprint_list=None, app_name=None):
    """
    Generate the navigation bar component template.
    """
    # Generate navigation links dynamically
    nav_links = ""
    if blueprint_list:
        for bp in blueprint_list:
            nav_links += f'<a href="/{bp}" class="text-white hover:bg-blue-700 px-3 py-2 rounded-md text-sm font-medium">{bp.title()}</a>\n'
    
    return """{% block navbar %}
<nav class="bg-blue-600 p-4">
  <div class="max-w-7xl mx-auto px-2 sm:px-6 lg:px-8">
    <div class="relative flex items-center justify-between h-16">
        <div class="absolute inset-y-0 left-0 flex items-center sm:hidden">
            <!-- Mobile menu button-->
            <button type="button" class="inline-flex items-center justify-center p-2 rounded-md text-white hover:text-gray-900 hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white" aria-controls="mobile-menu" aria-expanded="false">
                <span class="sr-only">Open main menu</span>
                <svg class="block h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
                </svg>
            </button>
        </div>
        <div class="flex-1 flex items-center justify-center sm:items-stretch sm:justify-start">
            <div class="flex-shrink-0 text-white text-2xl">{{ app_name }}</div>
            <div class="hidden sm:block sm:ml-6">
              <div class="flex space-x-4">
                  <a href="/" class="text-white hover:bg-blue-700 px-3 py-2 rounded-md text-sm font-medium">Home</a>
                  """ + nav_links + """
              </div>
            </div>
            <div class="hidden sm:flex items-center ml-auto">
                  <a href="https://github.com/mattburnett-repo/create-flask-app" target="_blank" rel="noopener noreferrer"
                    class="flex items-center text-white hover:bg-blue-700 px-3 py-2 rounded-md text-sm font-medium">
                        Created with create-flask-app. View create-flask-app on GitHub
                        <svg class="ml-2 h-5 w-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                            <path fill-rule="evenodd" clip-rule="evenodd"
                                  d="M12 0C5.37 0 0 5.373 0 12c0 5.302 3.438 9.8 8.205 11.387.6.113.82-.26.82-.577v-2.234c-3.338.727-4.033-1.415-4.033-1.415-.546-1.387-1.333-1.757-1.333-1.757-1.09-.745.082-.729.082-.729 1.205.085 1.84 1.238 1.84 1.238 1.07 1.834 2.807 1.304 3.492.996.108-.776.418-1.305.762-1.604-2.665-.305-5.466-1.335-5.466-5.931 0-1.31.468-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.3 1.23a11.45 11.45 0 0 1 3.003-.404c1.018.005 2.045.138 3.003.404 2.29-1.552 3.296-1.23 3.296-1.23.654 1.653.243 2.874.12 3.176.77.84 1.235 1.911 1.235 3.221 0 4.61-2.804 5.624-5.475 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.218.694.825.576C20.565 21.796 24 17.298 24 12c0-6.627-5.373-12-12-12z" />
                        </svg>
                    </a>
                </div>
            </div>
        </div>
    </div>
</nav>
{% endblock %}"""

def generate_flash_messages():
    """
    Generate the flash messages display component template.
    """
    return """{% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
        {% for category, message in messages %}
            <div class="alert alert-{{ category }} alert-dismissible fade show" role="alert">
                {{ message }}
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
        {% endfor %}
    {% endif %}
{% endwith %}"""
