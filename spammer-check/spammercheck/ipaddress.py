"""
Provides functionality related to IPv4 addresses.
"""


_SEPARATOR = "."


_NUMBER_OF_OCTETS = 4


def is_valid(address):
    """
    :param address: A string.
    :returns: Returns a boolean indicating whether the string is a valid
    IPv4 address.
    """
    potential_octets = _octets_of(address)

    return (len(potential_octets) == _NUMBER_OF_OCTETS and
            all(_is_octet(o) for o in potential_octets))


def _octets_of(address):
    return address.split(sep=_SEPARATOR)


def _is_octet(string):
    try:
        value = int(string)
    except ValueError:
        return False
    else:
        return 0 <= value < 256


def reverse(address):
    """
    :param address: A string - IPv4 address.
    :returns: Returns a string - an IPv4 address whose octets are the same
    as the octets of the original address but in reversed order.

    :raises ValueError: Raises an exception if the passed string is not a
    valid IPv4 address.
    """
    validate(address)

    return _SEPARATOR.join(reversed(_octets_of(address)))


def validate(address):
    """
    Receives a string. If it is a valid IPv4 address, the function does
    nothing. Otherwise an exception of type ValueError is raised.
    """
    if (not is_valid(address)):
        raise ValueError("Expected an IPv4 address!")

