#!/usr/bin/python3
"""This module defines a class LockedClass."""


class LockedClass:
    """A class that restricts dynamic creation of attributes.

    Attributes:
        first_name: The first name of the instance.
    """
    __slots__ = ['first_name']
