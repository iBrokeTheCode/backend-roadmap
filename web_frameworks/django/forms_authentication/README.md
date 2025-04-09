# Django Forms and User Authentication

## 1. Django Forms

**Theory**

Django forms provide a convenient way to handle user input and validate data. They simplify the process of creating HTML forms and processing form submissions.

**Key Concepts**

- **Form Class:** A Python class that defines the form fields and validation logic.
- **Form Fields:** Form fields represent HTML input elements (e.g., CharField, IntegerField, EmailField).
- **Form Validation:** Django automatically validates form data based on the field types and any custom validation logic.
- **Form Rendering:** Django forms can be rendered as HTML using template tags.
- **Form Processing:** Django provides methods for processing form submissions and accessing form data.

**Example**

Create a form class named `ProductForm` in your app's `forms.py` file:

```py
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock']
```

Modify your view to handle the form:

```py
from django.shortcuts import render, redirect
from .forms import ProductForm

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_create.html', {'form': form})
```

Create a template named `product_create.html`:

```html
<form method="post">
  {% csrf_token %} {{ form.as_p }}
  <button type="submit">Create</button>
</form>
```

- The `ProductForm` class defines a form based on the `Product` model.
- The view handles both GET and POST requests.
- The `form.is_valid()` method validates the form data.
- The `form.save()` method saves the form data to the database.
- `{{ form.as_p }}` renders the form fields as paragraphs.
- `{% csrf_token %}` is required for security.

## 2. User Authentication

**Theory**

Django provides a built-in authentication system that simplifies user registration, login, and logout.

**Key Concepts**

- **User Model:** Django's built-in `User` model represents users in your application.
- **Authentication Views:** Django provides views for login, logout, password change, and other authentication-related tasks.
- **Authentication Forms:** Django provides forms for login and password change.
- **Authentication Middleware:** Django's authentication middleware handles user sessions and authentication.
- **Permissions:** Django's permission system allows you to control access to views and models.

**Example**

Modify your `urls.py` file to include authentication URLs:

```py
from django.contrib.auth import views as auth_views

urlpatterns = [
    # ... other URLs
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
```

Create a `login.html` template:

```html
<form method="post">
  {% csrf_token %} {{ form.as_p }}
  <button type="submit">Login</button>
</form>
```

Modify your view to require authentication:

```py
from django.contrib.auth.decorators import login_required

@login_required
def product_list(request):
    # ... your view logic
```

- The `auth_views.LoginView` and `auth_views.LogoutView` handle login and logout.
- The `@login_required` decorator ensures that only authenticated users can access the view.
