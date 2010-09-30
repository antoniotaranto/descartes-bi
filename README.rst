============
Descartes-bi	
============

Descartes-bi is a database agnostic, Django based business intelligence.

Implementation
==============

Descartes-bi encapsulates small snipets of SQL in pseudo-objects called series, that can later be combined to create comparative charts.  Aside from containing series, charts can also define parameters for user interaction.  Parameters (called filters) can be programmed to be restrictive using a custom permission system.

Installation
============

 * Python 2.6
 * Django 1.1.1+

Setting up
==========

By default the project is set up to run on a SQLite database. Run::

    $ python manage.py syncdb


Executing
=========

Use::

    $ python manage.py runserver


Or since version 0.8, there is an experimental feature to integrate the tornado web server to allow Descartes-bi to run completly independent.

To try this feature use::

    $ python manage.py runtornado


License
=======
Descartes-bi in licensed under the terms of the GNU License version 3, see the included LICENSE file.