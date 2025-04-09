# Django Templates and Static Files

## 1. Django Templates

**Theory**

Django's templating system allows you to create dynamic HTML pages by embedding Python code within your HTML. Templates separate the presentation logic from the business logic, making your code more maintainable and organized.

**Key Concepts**

- **Template Language:** Django uses its own template language, which is similar to other templating languages like Jinja2.
- **Template Variables:** You can pass data from your views to your templates using template variables.
- **Template Tags:** Template tags provide logic and control flow within your templates.
- **Template Filters:** Template filters modify the output of template variables.
- **Template Inheritance:** You can create base templates and extend them in child templates.

**Example**

Create a template file named `product_list.html` in your app's templates directory:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Product List</title>
  </head>
  <body>
    <h1>Product List</h1>
    <ul>
      {% for product in products %}
      <li>{{ product.name }} - ${{ product.price }}</li>
      {% endfor %}
    </ul>
  </body>
</html>
```

Modify your view to render the template:

```py
from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})
```

- The `render` function renders the template with the provided data.
- The `{% for product in products %}` tag iterates over the `products` list.
- The `{{ product.name }}` syntax displays the product's name.

## 2. Static Files

**Theory**

Static files are files that are served directly to the browser, such as CSS, JavaScript, and images. Django provides a way to manage and serve static files efficiently.

**Key Concepts**

- **Static Files Directory:** You need to create a static directory in your app to store your static files.
- `STATIC_URL`: This setting defines the base URL for your static files.
- `STATICFILES_DIRS`: This setting defines additional directories to search for static files.
- **`{% static %}` Template Tag:** This tag generates the URL for a static file.

**Example**

Create a `static` directory in your app and add a CSS file named `styles.css`:

```css
body {
  font-family: sans-serif;
}
```

Modify your template to include the CSS file:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Product List</title>
    {% load static %}
    <link rel="stylesheet" href="{% static 'styles.css' %}" />
  </head>
  <body>
    <h1>Product List</h1>
    <ul>
      {% for product in products %}
      <li>{{ product.name }} - ${{ product.price }}</li>
      {% endfor %}
    </ul>
  </body>
</html>
```

Add the `STATIC_URL` setting to your `settings.py` file:

```py
STATIC_URL = '/static/'
```

- The `{% load static %}` tag loads the static template tags.
- The `{% static 'styles.css' %}` tag generates the URL for the styles.css file.

## 3. Template Inheritance

**Theory**

Template inheritance allows you to create a base template with common elements and extend it in child templates. This helps to reduce code duplication and maintain consistency.

**Example**

Create a base template named `base.html` in your app's `templates` directory:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>{% block title %}{% endblock %}</title>
  </head>
  <body>
    {% block content %}{% endblock %}
  </body>
</html>
```

Modify your `product_list.html` template to extend the base template:

```html
{% extends 'base.html' %} {% block title %}Product List{% endblock %} {% block
content %}
<h1>Product List</h1>
<ul>
  {% for product in products %}
  <li>{{ product.name }} - ${{ product.price }}</li>
  {% endfor %}
</ul>
{% endblock %}
```

- The `{% extends 'base.html' %}` tag extends the base.html template.
- The `{% block title %}` and `{% block content %}` tags define blocks that can be overridden in child templates.
