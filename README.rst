==============================
 ``zope.principalannotation``
==============================

.. image:: https://img.shields.io/pypi/v/zope.principalannotation.svg
        :target: https://pypi.python.org/pypi/zope.principalannotation/
        :alt: Latest release

.. image:: https://img.shields.io/pypi/pyversions/zope.principalannotation.svg
        :target: https://pypi.org/project/zope.principalannotation/
        :alt: Supported Python versions

.. image:: https://travis-ci.org/zopefoundation/zope.principalannotation.png?branch=master
        :target: https://travis-ci.org/zopefoundation/zope.principalannotation

.. image:: https://coveralls.io/repos/github/zopefoundation/zope.principalannotation/badge.svg?branch=master
        :target: https://coveralls.io/github/zopefoundation/zope.principalannotation?branch=master

This package implements annotations for zope.security principals. Common
annotation techniques, like ``AttributeAnnotations`` cannot be applied to
principals, since they are created on the fly for every request.
