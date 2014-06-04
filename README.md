pycity
======

Provides programmatic access to a list of the largest US Cities. Currently contains the top 140 more populus cities in the US

Usage::

    >>> import pycity
    >>> pycity.cities.get(code='US-AL')
    [
            {u'code': u'US-AL', u'name': u'Birmingham', u'population': 212113}, 
            {u'code': u'US-AL', u'name': u'Montgomery', u'population': 201332}, 
            {u'code': u'US-AL', u'name': u'Mobile', u'population': 194899}, 
            {u'code': u'US-AL', u'name': u'Huntsville', u'population': 186254}
    ]

The `get` method can take one of three keys - 'code', 'name', or 'population' - as a filter

