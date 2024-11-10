from ipaddress import ip_network


def find_address_net(ip_adr, mask_net):
    net = ip_network(f'{ip_adr}/{mask_net}', 0)
    net = str(net)[:-3]
    return net


def find_count_mask(ip_adr, net):
    k = 0
    for mask in range(33):
        net_r = ip_network(f'{ip_adr}/{mask}', 0)
        if str(net_r) == f'{net}/{mask}':
            k += 1
    return k
