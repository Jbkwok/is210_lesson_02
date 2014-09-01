#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides the is_empty() method."""


def get_member_count(my_sequence):
    """Returns the number of members of a list object.

    Args:
        my_sequence (sequence): The sequence object being measured.

    Returns:
        mixed: If the object can be measured it returns an integer. If not it
               returns ``False``

    Examples:
        >>> get_member_count(42)
        False

        >>> get_member_count('duck')
        4

        >>> get_member_count(['knights', 'who', 'say', 'ni'])
        4
    """
    try:
        length = len(my_sequence)
    except TypeError:
        length = False

    return length

def is_empty(my_sequence):
    """Tests whether or not the passed sequence is empty.

    Args:
        my_sequence (sequence): The sequence object being measured.

    Returns:
        bool: If empty, returns True, otherwise, False.

    Raises:
        TypeError: If my_sequence is not a sequence object type.

    Examples:

        >>> is_empty('')
        True

        >>> is_empty('apple')
        False

        >>> is_empty([])
        True

        >>> is_empty(42)
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        TypeError: object has no len()
    """
    count = get_member_count(my_sequence)

    if count != False:
        return count == 0
    else:
        raise TypeError('Object has no len()')


TEST = ''
print len(TEST)
print is_empty(TEST)
