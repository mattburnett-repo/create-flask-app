def generate_empty_template(template_type, blueprint_name, app_name):
    """
    Generate an empty template with basic structure.
    template_type: 'Create', 'List', 'Edit', or 'Detail'
    blueprint_name: Name of the blueprint (e.g., 'users', 'admin')
    """
    if template_type == 'List':
        return f"""{{% extends "base.html" %}}

{{% block title %}}{{{{ blueprint_name|title }}}}{{% endblock %}}

{{% block content %}}
<div class="container mx-auto px-4 py-8">
    <div class="bg-white shadow-md rounded-lg p-6">
        <h1 class="text-2xl font-bold mb-4">{{{{ blueprint_name|title }}}}</h1>
        
        {{% if results %}}
        <div class="overflow-x-auto">
            <table class="min-w-full bg-white">
                <thead>
                    <tr class="bg-gray-100">
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">ID</th>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Name</th>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Description</th>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-gray-200">
                    {{% for result in results %}}
                    <tr class="hover:bg-gray-50">
                        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{{{ result['id'] }}}}</td>
                        <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{{{{ result['name'] }}}}</td>
                        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{{{ result['description'] }}}}</td>
                        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                            <div class="flex space-x-2">
                                <a href="{{{{ url_for('{blueprint_name}.edit', id=result['id']) }}}}"
                                   class="bg-yellow-400 hover:bg-yellow-500 text-white px-3 py-1 rounded-md text-sm">
                                    Edit
                                </a>
                                <form method="POST" 
                                      action="{{{{ url_for('{blueprint_name}.delete', id=result['id']) }}}}"
                                      onsubmit="return confirm('Are you sure you want to delete this item?');"
                                      class="inline">
                                    <button type="submit"
                                            class="bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded-md text-sm">
                                        Delete
                                    </button>
                                </form>
                            </div>
                        </td>
                    </tr>
                    {{% endfor %}}
                </tbody>
            </table>
        </div>
        {{% else %}}
        <p class="text-gray-500">No items found.</p>
        {{% endif %}}

        <div class="mt-6">
            <a href="{{{{ url_for('{blueprint_name}.create') }}}}" 
               class="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-md">
                Create New
            </a>
        </div>
    </div>
</div>
{{% endblock %}}"""

    elif template_type in ['Create', 'Edit']:
        return f"""{{% extends "base.html" %}}

{{% block title %}}{{{{ blueprint_name|title }}}} - {template_type}{{% endblock %}}

{{% block content %}}
<div class="container mx-auto px-4 py-8">
    <div class="bg-white shadow-md rounded-lg p-6">
        <h1 class="text-2xl font-bold mb-4">{{{{ blueprint_name|title }}}} - {template_type}</h1>
        
        <form method="POST" class="space-y-4">
            <div>
                <label for="name" class="block text-sm font-medium text-gray-700">Name</label>
                <input type="text" 
                       name="name" 
                       id="name" 
                       value="{{{{ result.name if result else '' }}}}"
                       class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
                       required>
            </div>
            
            <div>
                <label for="description" class="block text-sm font-medium text-gray-700">Description</label>
                <textarea name="description" 
                          id="description" 
                          rows="3"
                          class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
                          required>{{{{ result.description if result else '' }}}}</textarea>
            </div>
            
            <div class="flex space-x-4">
                <button type="submit" 
                        class="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-md">
                    {template_type}
                </button>
                <a href="{{{{ url_for('{blueprint_name}.index') }}}}" 
                   class="bg-gray-500 hover:bg-gray-600 text-white px-4 py-2 rounded-md">
                    Cancel
                </a>
            </div>
        </form>
    </div>
</div>
{{% endblock %}}"""

    else:  # Detail view
        return f"""{{% extends "base.html" %}}

{{% block title %}}{{{{ blueprint_name|title }}}} - Detail{{% endblock %}}

{{% block content %}}
<div class="container mx-auto px-4 py-8">
    <div class="bg-white shadow-md rounded-lg p-6">
        <h1 class="text-2xl font-bold mb-4">{{{{ blueprint_name|title }}}} - Detail</h1>
        
        {{% if result %}}
        <div class="space-y-4">
            <div>
                <h2 class="text-lg font-medium text-gray-900">Name</h2>
                <p class="mt-1 text-gray-600">{{{{ result.name }}}}</p>
            </div>
            
            <div>
                <h2 class="text-lg font-medium text-gray-900">Description</h2>
                <p class="mt-1 text-gray-600">{{{{ result.description }}}}</p>
            </div>
            
            <div class="flex space-x-4">
                <a href="{{{{ url_for('{blueprint_name}.edit', id=result.id) }}}}" 
                   class="bg-yellow-400 hover:bg-yellow-500 text-white px-4 py-2 rounded-md">
                    Edit
                </a>
                <form method="POST" 
                      action="{{{{ url_for('{blueprint_name}.delete', id=result.id) }}}}"
                      onsubmit="return confirm('Are you sure you want to delete this item?');"
                      class="inline">
                    <button type="submit"
                            class="bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded-md">
                        Delete
                    </button>
                </form>
            </div>
        </div>
        {{% else %}}
        <p class="text-gray-500">Item not found.</p>
        {{% endif %}}
        
        <div class="mt-6">
            <a href="{{{{ url_for('{blueprint_name}.index') }}}}" 
               class="bg-gray-500 hover:bg-gray-600 text-white px-4 py-2 rounded-md">
                Back to List
            </a>
        </div>
    </div>
</div>
{{% endblock %}}"""