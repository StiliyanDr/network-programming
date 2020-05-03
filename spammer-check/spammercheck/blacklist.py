"""
Represents a black list of IPv4 addresses of hosts who are known to be
spammers.
"""


from types import MappingProxyType
from typing import NamedTuple
import socket

from spammercheck import ipaddress


class Zone(NamedTuple):
    """
    Represents a public IP zone in the black list of spammers.
    """
    name: str
    description: str
    code: str


_ZONES = MappingProxyType({
    code : Zone(name, description, code)
    for code, name, description in [
        ("127.0.0.2", "SBL", "Spamhaus SBL Data"),
        ("127.0.0.3", "SBL", "Spamhaus SBL CSS Data"),
        ("127.0.0.4", "XBL", "CBL Data"),
        ("127.0.0.9", "SBL", "Spamhaus DROP/EDROP Data"),
        ("127.0.0.10", "PBL", "ISP Maintained"),
        ("127.0.0.11", "PBL", "Spamhaus Maintained"),
    ]
})


_HOST_NAME_SEPARATOR = "."


_SERVICE_HOST_NAME = "zen.spamhaus.org"


def search(address):
    """
    :param address: A string which is assumed to be a valid IPv4 address.
    :returns: If the address is one of a host which is known to be a
    spammer, a set of Zone instances is returned. Otherwise, None is
    returned.
    """
    assert ipaddress.is_valid(address)
    name = _host_name_for(address)
    codes = _do_search(name)

    return ({_ZONES[c] for c in codes}
            if (codes is not None)
            else None)


def _host_name_for(address):
    return _HOST_NAME_SEPARATOR.join([
        ipaddress.reverse(address),
        _SERVICE_HOST_NAME
    ])


def _do_search(host_name):
    try:
        _, _, all_codes = socket.gethostbyname_ex(
            host_name
        )
    except socket.gaierror:
        return None
    else:
        public_IP_zone_codes = [
            c for c in all_codes
            if (c in _ZONES)
        ]

        return (public_IP_zone_codes
                if (public_IP_zone_codes)
                else None)
