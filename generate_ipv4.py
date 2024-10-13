import random


def generate_ipv4():
    ip_parts = []

    for i in range(4):
        part = random.randint(0, 255)
        ip_parts.append(str(part))

    ip_address = ".".join(ip_parts)

    return ip_address