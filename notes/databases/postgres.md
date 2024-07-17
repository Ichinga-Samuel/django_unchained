# Using Postgres as a Database

Django supports PostgreSQL 12 and higher. psycopg 3.1.8+ or psycopg2 2.8.4+ is required, though the latest
psycopg 3.1.8+ is recommended.

## Connection Settings

### Default Settings

```python
DATABASES = {
    "default": {
    "ENGINE": "django.db.backends.postgresql",
    "OPTIONS": {
        "host": "localhost",
        "user": "db_user",
        "dbname": "db_name",
        "port": 5432
        },
    }
}
```

## Optimizing Postgres

### Manually-specifying values of auto-incrementing primary keys

Manually assigning a value to an auto-incrementing field doesn’t update the field’s sequence, which might later cause a conflict. If you need to specify such values, reset the sequence afterward to avoid reusing a value that’s already in the table. The `sqlsequencereset` management command generates the SQL statements to do that.
