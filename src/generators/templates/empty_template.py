def generate_empty_template(label):
    return f"""{{% extends 'base.html' %}}\n
      {{% block content %}}\n
      <h1>{label}</h1>\n
      {{% endblock %}}"""