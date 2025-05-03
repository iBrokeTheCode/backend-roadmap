# Class-Based Views (CBVs) in Django

## What are Class-Based Views?

- **Class-Based Views (CBVs)** allow you to structure your Django views using Python classes instead of functions.
- They provide a more organized and reusable way to handle HTTP requests.

> [!TIP]
> For more details, review the [documentation](https://docs.djangoproject.com/en/5.2/topics/class-based-views/)

## Why Use CBVs?

- Reduce code repetition (DRY principle).
- Reuse and extend logic using inheritance.
- Django provides many built-in generic CBVs for common tasks like listing, creating, updating, and deleting objects.

## Basic Structure

A CBV is a Python class that inherits from Django's built-in `View` class or a generic class.

Example:

```python
from django.views import View
from django.http import HttpResponse

class MyView(View):
    def get(self, request):
        return HttpResponse('Hello from a class-based view!')
```

- `get(self, request)`: Handles GET requests.
- `post(self, request)`: Handles POST requests.

## Common Generic CBVs

Django provides ready-to-use CBVs to make CRUD operations easy:

| View Class   | Purpose                            |
| :----------- | :--------------------------------- |
| `ListView`   | Display a list of objects          |
| `DetailView` | Display details of a single object |
| `CreateView` | Form to create a new object        |
| `UpdateView` | Form to update an existing object  |
| `DeleteView` | Confirm and delete an object       |

## Example: Using a Generic CBV

```python
from django.views.generic import ListView
from .models import MenuItem

class MenuItemListView(ListView):
    model = MenuItem
    template_name = 'menu/menuitem_list.html'
    context_object_name = 'menu_items'
```

This automatically:

- Fetches all `MenuItem` objects.
- Renders them using `menu/menuitem_list.html`.
- Passes the objects into the template under the name `menu_items`.

## URL Configuration

To use a CBV in `urls.py`, use `.as_view()`:

```python
from django.urls import path
from .views import MenuItemListView

urlpatterns = [
    path('menu/', MenuItemListView.as_view(), name='menuitem-list'),
]
```

## Customizing CBVs

You can override methods like:

- `get_queryset(self)`
- `form_valid(self, form)`
- `get_context_data(self, **kwargs)`

Example: customizing the context

```python
class MenuItemListView(ListView):
    model = MenuItem
    template_name = 'menu/menuitem_list.html'
    context_object_name = 'menu_items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['special_note'] = 'Today\'s special menu!'
        return context
```

# When to Use CBVs vs FBVs

- Use **CBVs** when the view logic fits a **standard pattern** (like CRUD).
- Use **FBVs (Function-Based Views)** for **very simple** or **highly custom** logic.

Both are valid and can be combined in the same project.
