## Models
Models are the core of Django. They are used to define the structure of the data that is stored in the database.
Django models are Python classes that inherit from `django.db.models.Model`. Each model class usually but not always
represents a table in the database. The attributes of the model class represent the fields of the table.
A primary key field `pk` is automatically created for each model class using the `DEFAULT_AUTO_FIELD` setting.
It can be also be accessed using the `id` attribute.
