"""Examples of how to use the models defined in the band app."""
from datetime import date

from .models import person, Group, Membership


def example1():
    """
    This example illustrates how to create a many-to-many relationship with an intermediate model.
    """
    # Create a person
    p = person(name='Fred')
    # call save() to save the person to the database because we are not using the create() method.
    p.save()

    # Create a group
    g = Group(name='Python Programmers')
    g.save()

    # Add the person to the group
    m = Membership(person=p, group=g, date_joined=date.today(), invite_reason='I like Python.')
    m.save()

    # Retrieve all the members of the group
    members = g.members.all()
    print(members)


def example2():
    """
    Use the relationship manager directly.
    """
    # we can also add a person to a group using the relationship manager,
    # use the through_defaults argument to set the date_joined and invite_reason fields.
    p = person.objects.create(name='Barney')
    p.save()
    g = Group.objects.create(name='Bad Ass Programmers')
    g.members.add(p, through_defaults={'date_joined': date.today()})
