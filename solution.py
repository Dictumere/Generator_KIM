def solution(ip_adr, mask_net):
    ip_parts = ip_adr.split('.')
    mask_parts = mask_net.split('.')

    network_parts = []

    for i in range(4):
        ip_part = int(ip_parts[i])
        mask_part = int(mask_parts[i])

        network_part = ip_part & mask_part

        network_parts.append(str(network_part))

    network_address = ".".join(network_parts)

    return network_address