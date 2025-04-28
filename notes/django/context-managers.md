# Context Processors in Django

## What are Context Processors?

- **Context processors** are Python functions that return a dictionary.
- They make variables **available in all templates automatically**, without having to pass them manually from each view.

> [!TIP]
> For more details, review the [documentation](https://docs.djangoproject.com/en/5.1/ref/templates/api/#writing-your-own-context-processors)

## Why Use Context Processors?

- Avoid repeating code in every view.
- Share common data like site settings, user info, or global menus across all pages.
- Make templates cleaner and views simpler.

## How to Create and Use a Context Processor

### 1. Create the Context Processor Function

Inside your app (example: `core/context_processors.py`):

```python
from .models import BusinessInfo

def business_info(request):
    try:
        info = BusinessInfo.objects.first()
    except BusinessInfo.DoesNotExist:
        info = None
    return {
        'business_info': info
    }
```

- This function tries to get the first `BusinessInfo` record.
- Returns it inside a dictionary as `'business_info'`.

### 2. Register the Context Processor in `settings.py`

In your `TEMPLATES` setting, under `'OPTIONS' -> 'context_processors'`, **add the path** to your function:

```python
TEMPLATES = [
    {
        ...
        'OPTIONS': {
            'context_processors': [
                ...
                'core.context_processors.business_info',  # 👈 Add this line
            ],
        },
    },
]
```

### 3. Use It in Any Template

Now you can access `business_info` in **any template** without passing it manually:

```html
<header>
  <h1>{{ business_info.name }}</h1>
  <p>{{ business_info.address }}</p>
</header>

<footer>
  <p>Phone: {{ business_info.phone }}</p>
</footer>
```

✅ It will be available on **all pages** automatically.

## Extra Tips

- Use the `default` filter to avoid errors if the value is missing:

  ```html
  <h1>{{ business_info.name|default:"Default Restaurant Name" }}</h1>
  ```

- Keep context processors **small and fast** — they are called on every request!
