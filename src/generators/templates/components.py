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
        <div class="w-full">
            {% for category, message in messages %}
                <div class="transform transition-all duration-300 ease-in-out"
                     x-data="{ show: true }"
                     x-show="show"
                     x-transition:enter="transition ease-out duration-300"
                     x-transition:enter-start="opacity-0 transform -translate-y-2"
                     x-transition:enter-end="opacity-100 transform translate-y-0"
                     x-transition:leave="transition ease-in duration-200"
                     x-transition:leave-start="opacity-100 transform translate-y-0"
                     x-transition:leave-end="opacity-0 transform -translate-y-2">
                    <div class="w-full py-3 px-4
                        {% if category == 'success' %}
                            bg-green-50 text-green-800 border-b border-green-200
                        {% elif category == 'error' %}
                            bg-red-50 text-red-800 border-b border-red-200
                        {% elif category == 'warning' %}
                            bg-yellow-50 text-yellow-800 border-b border-yellow-200
                        {% else %}
                            bg-blue-50 text-blue-800 border-b border-blue-200
                        {% endif %}">
                        <div class="max-w-7xl mx-auto flex items-center justify-center">
                            <div class="flex items-center">
                                <div class="flex-shrink-0">
                                    {% if category == 'success' %}
                                        <svg class="h-5 w-5 text-green-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                                            <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                                        </svg>
                                    {% elif category == 'error' %}
                                        <svg class="h-5 w-5 text-red-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                                            <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd" />
                                        </svg>
                                    {% elif category == 'warning' %}
                                        <svg class="h-5 w-5 text-yellow-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                                            <path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
                                        </svg>
                                    {% else %}
                                        <svg class="h-5 w-5 text-blue-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                                            <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd" />
                                        </svg>
                                    {% endif %}
                                </div>
                                <div class="ml-3">
                                    <p class="text-sm font-medium">{{ message }}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            {% endfor %}
        </div>
    {% endif %}
{% endwith %}"""
