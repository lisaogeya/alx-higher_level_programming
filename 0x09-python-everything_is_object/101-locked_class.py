#!/usr/bin/python3
"""Defines locked class """


class LockedClass:
    """
    Prevent the user from instantiating newly LockedClass attributes
    for anything except 'first_name' attributes.
    """
    __slots__ = ["first_name"]
