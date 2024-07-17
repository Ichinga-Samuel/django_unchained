# Databases

Django officially supports the following databases.

- PostgreSQL
- MariaDB
- MySQL
- Oracle
- SQLite
Django assumes that all databases use UTF-8 encoding.

## Persistent Notes

Persistent connections avoid the overhead of reestablishing a connection to the database in each request.
They’re controlled by the CONN_MAX_AGE parameter which defines the maximum lifetime of a connection.
It can be set independently for each database. The default is 0, to enable consitent connection to database set the `CONN_MAX_AGE` to a positive integer. Sometimes a database won’t be accessed by the majority of your views, for example because it’s the database of an external system, or thanks to caching. In such cases, you should set CONN_MAX_AGE to a low value or even 0, because it doesn’t make sense to maintain a connection that’s unlikely to be reused. This keeps the number of simultaneous connections to this database small.
Don’t `CONN_MAX_AGE` enable them during development.

```python
DATABASES = {
    'default': {
        "OPTIONS":{
            "CONN_MAX_AGE": 5
            }
    }
}
```

## Connection Management

Django opens a connection to the database when it first makes a database query. It keeps this connection
open and reuses it in subsequent requests. Django closes the connection once it exceeds the maximum age
defined by `CONN_MAX_AGE` or when it isn’t usable any longer.
Setting `CONN_HEALTH_CHECKS` to True can be used to improve the robustness of connection reuse and prevent
errors when a connection has been closed by the database server which is now ready to accept and serve new
connections, e.g. after database server restart.
