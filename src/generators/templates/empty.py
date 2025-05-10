def generate_empty_template(template_type, blueprint_name, app_name=None):
    """
    Generate an empty template with basic structure.
    template_type: 'Create', 'List', 'Edit', or 'Detail'
    blueprint_name: Name of the blueprint (e.g., 'users', 'admin')
    """
    return """{% extends "base.html" %}

{% block content %}
<div class="py-12">
    <div class="max-w-7xl mx-auto sm:px-6 lg:px-8">
        <div class="bg-white overflow-hidden shadow-sm sm:rounded-lg">
            <div class="p-6 bg-white border-b border-gray-200">
                <h1 class="text-2xl font-bold mb-4">{{ blueprint_name }} - {{ template_type }}</h1>
                <p>This is the {{ template_type.lower() }} template for {{ blueprint_name }}.</p>
            </div>
        </div>
    </div>
</div>
{% endblock %}"""