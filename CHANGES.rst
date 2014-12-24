Changes
=======

4.0.0 (2014-12-24)
------------------

- Add support for PyPy.

- Add support for Python 3.4.

- Add support for testing on Travis.


4.0.0a2 (2013-02-25)
--------------------

- Correct Trove classifiers.


4.0.0a1 (2013-02-24)
--------------------

- Add support for Python 3.3.

- Replace deprecated ``zope.interface.implements`` usage with equivalent
  ``zope.interface.implementer`` decorator.

- Drop support for Python 2.4 and 2.5.

3.6.1 (2010-05-05)
------------------

- Fix a test failure in nested local site manager setup.

- Remove dependency on zope.container.

3.6.0 (2009-03-09)
------------------

Initial release. This package was splitted off zope.app.principalannotation
to remove its dependencies on "zope 3 application server" components.

In addition, the following changes were made after split off:

 - The IAnnotations implementation was fixed to look in the higher-level
   utility not only on ``__getitem__``, but also on ``get`` and ``__nonzero``.

 - Tests was reworked into the README.txt doctest.

 - Added a buildout part that generates Sphinx documentation from the
   README.txt