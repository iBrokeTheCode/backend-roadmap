# Django Custom Management Commands

Django provides a powerful way to extend its CLI through **custom management commands**, allowing developers to script logic like populating databases, running background jobs, or generating reports.

## Why Use Custom Commands?

- Automate data setup for development and testing
- Perform custom batch operations
- Clean and maintain database records
- Run background or one-time scripts
- Avoid manual admin panel input

## How to Create a Custom Management Command

### 1. Create the Command Structure

Inside one of your Django apps (e.g., `myapp`), add the following directory structure:

```
myapp/
└── management/
└── commands/
└── my_command.py
```

You **must** include `__init__.py` files in each folder:

```bash
touch myapp/management/__init__.py
touch myapp/management/commands/__init__.py
```

### 2. Create the Command File

Here’s a basic template (`my_command.py`):

```python
from django.core.management.base import BaseCommand
from myapp.models import MyModel

class Command(BaseCommand):
    help = 'Populate the database with sample data.'

    def handle(self, *args, **options):
        # Add your logic here
        MyModel.objects.create(name="Sample", value=123)
        self.stdout.write(self.style.SUCCESS('Sample data created!'))
```

### 3. Run the Command

Once created, run your command with:

```bash
python manage.py my_command
```

You’ll see any `self.stdout.write(...)` outputs in your terminal.

## Example Use Cases

- `populate_sample_data`: Create sample categories, users, or products.
- `clear_expired_sessions`: Clean old session data.
- `recalculate_stats`: Rebuild analytics or leaderboards.
- `import_csv_data`: Load external files into your models.
- `send_daily_report`: Trigger automated notifications or summaries.

## Best Practices

- Keep each command focused and clearly named.
- Use `--options` (add_arguments) to accept CLI parameters.
- Wrap bulk operations in transactions for safety.
- Use `self.stdout.write()` instead of `print()` for better CLI formatting.

## References

- [Django docs – Custom commands](https://docs.djangoproject.com/en/stable/howto/custom-management-commands/)

```

```
