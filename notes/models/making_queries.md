# Making Queries

## Retrieving objects

To retrieve objects from your database, construct a QuerySet via a Manager on your model class.
A QuerySet represents a collection of objects from your database. It can have zero, one or many filters.
Filters narrow down the query results based on the given parameters. In SQL terms, a QuerySet equates to
a SELECT statement, and a filter is a limiting clause such as WHERE or LIMIT.

### Retrieving all objects

```python
# get all entries in the table
queryset = ModelClass.objects.all()
```

### Retrieving specific objects with filters

* filter(**kwargs) Returns a new QuerySet containing objects that match the given lookup parameters.
* exclude(**kwargs) Returns a new QuerySet containing objects that do not match the given lookup parameters.

```python
Entry.objects.filter(pub_date__year=2006)
Entry.objects.all().filter(pub_date__year=2006)
```

### Chaining filters

```python
Entry.objects.filter(headline__startswith="What").exclude(pub_date__gte=datetime.date.today()).filter(pub_date__gte=datetime.date(2005, 1, 30))
```

### Filtered QuerySets are unique

Each time you refine a QuerySet, you get a brand-new QuerySet that is in no way bound to the previous QuerySet. Each refinement creates a separate and distinct QuerySet that can be stored, used and reused.

### QuerySets are lazy

QuerySets are lazy –the act of creating a QuerySet doesn’t involve any database activity. You can stack
filters together all day long, and Django won’t actually run the query until the QuerySet is evaluated.

### Retrieving a single object with get()

Similarly, Django will complain if more than one item matches the get() query. In this case, it will raise
*MultipleObjectsReturned*, which again is an attribute of the model class itself. Generally, slicing a QuerySet returns a new QuerySet –it doesn’t evaluate the query. An exception is if you use the “step” parameter of Python slice syntax. For example, this would actually execute the query in order to return a list of every second object of the first 10.

### QuerySets

Use a subset of Python’s array-slicing syntax to limit your QuerySet to a certain number of results. This is
the equivalent of SQL’s LIMIT and OFFSET clauses.

### Field Lookups

Field lookups are how you specify the meat of an SQL WHERE clause. They’re specified as keyword arguments
to the QuerySet methods filter(), exclude() and get().
Basic lookups keyword arguments take the form `field__lookuptype=value`. (That’s a double-underscore) passed into queryset methods.
