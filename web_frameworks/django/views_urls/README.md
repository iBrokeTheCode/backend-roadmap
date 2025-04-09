# Django Views and URL Routing

## 1. Django Views

**Theory:**

- Views are Python functions or classes that handle HTTP requests and return HTTP responses.
- They contain the logic for processing requests and generating responses.
- Views interact with models, templates, and other components of your Django application.

**Function-Based Views (FBVs):**

- Simple Python functions that take an `HttpRequest` object as input and return an `HttpResponse` object.
- This view function returns an HTTP response with an HTML heading.

**Example:**

```py
from django.http import HttpResponse

def product_list(request):
    return HttpResponse("<h1>Product List</h1>")
```

**Passing Data to Views:**

- Views can retrieve data from models and pass it to templates or include it directly in the HTTP response.
- This view retrieves all Product objects from the database, serialize it to json and returns a json response.

**Example:**

```py
from django.http import HttpResponse
from .models import Product
from django.core import serializers
import json

def product_list_json(request):
    products = Product.objects.all()
    products_json = serializers.serialize('json', products)
    return HttpResponse(products_json, content_type='application/json')
```

## 2. URL Routing:

**Theory:**

- URL routing maps URLs to views.
- Django's `urls.py` files define the URL patterns for your application.
- URL patterns use regular expressions to match URLs.

**Steps:**

- **Create URL Patterns:** In your app's `urls.py` file, define URL patterns using the `path()` or `re_path()` function.
- **Include App URLs:** In your project's `urls.py` file, include your app's `urls.py` file using the `include()` function.

**Example:**

In `myapp/urls.py`:

```py
from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('products/json', views.product_list_json, name='product_list_json')
]
```

In `myproject/urls.py`:

```py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
]
```

- The `path('products/', ...)` pattern maps the URL `/myapp/products/` to the `product_list` view.
- The `path('myapp/', include('myapp.urls'))` line includes all URL patterns from the `myapp` app.

## 3. URL Parameters:

**Theory:**

- URL parameters allow you to capture values from URLs and pass them to views.
- This is useful for creating dynamic URLs.

**Example:**

In `myapp/urls.py`:

```py
path('products/<int:product_id>/', views.product_detail, name='product_detail'),
```

In `myapp/views.py`:

```py
from django.http import HttpResponse
from .models import Product

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return HttpResponse(f"<h1>{product.name}</h1><p>{product.description}</p>")
```

- The `<int:product_id>` pattern captures an integer value from the URL and passes it to the `product_detail` view as the `product_id` argument.
