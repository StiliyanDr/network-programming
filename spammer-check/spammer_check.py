import socket
import sys

from spammercheck import blacklist, ipaddress


def determine_addresses_to_search(command_line_args):
    if (command_line_args):
        validate_addresses(command_line_args)
        return command_line_args
    else:
        address = current_host_address()
        return ([address]
                if (address is not None)
                else None)


def validate_addresses(addresses):
    invalid_addresses = [
        (address, index + 1)
        for index, address in enumerate(addresses)
        if (not ipaddress.is_valid(address))
    ]

    if (invalid_addresses):
        raise ValueError(
            "Invalid addresses found! The addresses "
            f"and their positions are {invalid_addresses}."
        )


def current_host_address():
    try:
        return socket.gethostbyname(socket.gethostname())
    except Exception:
        return None


def print_result_for(address, zones):
    print(f"The IP address {address!r} was ", end="")

    if (zones is not None):
        print("found in the following public IP zone(s):")
        print(*format_zones(zones), sep="\n")
    else:
        print("NOT found in the blacklist.")


def format_zones(zones):
    return (
        " - ".join([
            z.code,
            z.name,
            z.description,
        ])
        for z in zones
    )


def log_error(message):
    sys.stderr.write(f"{message}\n")


if (__name__ == "__main__"):
    try:
        addresses = determine_addresses_to_search(
            sys.argv[1:]
        )
    except ValueError as e:
        log_error(str(e))
    else:
        if (addresses is not None):
            for a in addresses:
                zones = blacklist.search(a)
                print_result_for(a, zones)
        else:
            log_error("Unable to obtain host address.")
