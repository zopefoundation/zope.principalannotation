##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Utility for storing `IAnnotations` for principals.
"""
__docformat__ = 'restructuredtext'

from zope.interface import Interface


class IPrincipalAnnotationUtility(Interface):
    """Stores :class:`~.IAnnotations` for :class:`~.IPrinicipals`."""

    def getAnnotations(principal):
        """Return object implementing :class:`~.IAnnotations` for the given
        :class`~.IPrinicipal`.

        If there is no :class:`~.IAnnotations` it will be created and then
        returned.
        """

    def getAnnotationsById(principalId):
        """Return object implementing :class:`~.IAnnotations` for the given
        *prinicipalId*.

        If there is no :class:`~.IAnnotations` it will be created and then
        returned.
        """

    def hasAnnotations(principal):
        """Return boolean indicating if given :class:`~.IPrincipal` has
        :class:`~.IAnnotations`."""
