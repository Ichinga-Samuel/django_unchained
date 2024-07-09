from datetime import date
from .models import Blog, Entry, Author


def example_1():
    # create an instance directly from the model instance 
    # then save
    b = Blog(name="Beatles Blog", tagline="All the latest Beatles news.")
    b.save()
    a = Author(name='John')
    a.save()
    
    # The below won't work
    # Direct assignment to the forward side of a many-to-many set is prohibited. Use authors.set() instead.
    # e = Entry(headline='Man Utd Win 2025 Premier League', body_text='We Won', pub_date=date.today(), authors=a)


def example_2():
    b = Blog.objects.get(name='Beatles Blog')
    a = Author.objects.get(name='John')
    e = Entry(headline='Man Utd Win 2025 Premier League', body_text='We Won', pub_date=date.today(), blog=b)
    e.authors.add(e)    
    e.save()
    # Update operations needs to be saved
    a.name = 'John Mark'
    a.save()
    # Create multiple authors
    a1 = Author.objects.create(name='Paul')
    a2 = Author.objects.create('Peter')
    e.add(a1, a2)

