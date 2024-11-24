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


# Не правильно считает
def find_min_count_mask(ip_adr, net):
    for mask in range(33):
        net_r = ip_network(f'{ip_adr}/{mask}', 0)
        if str(net_r) == f'{net}/{mask}':
            return 32-mask


def find_count_one(ip_adr, network):
    last_mask = None
    for mask in range(33):
        net = ip_network(f'{ip_adr}/{mask}', strict=False)
        if str(net) == f'{network}/{mask}':
            last_mask = mask
    return last_mask


def find_third_mask(ip_adr, network):
    last_mask = None
    for mask in range(33):
        net = ip_network(f'{ip_adr}/{mask}',0)
        if str(net) == f'{network}/{mask}':
            last_mask = net.netmask
    return str(last_mask)[8:11]


def find_max_adr_network(ip_adr, network):
    for mask in range(33):
        net = ip_network(f'{ip_adr}/{mask}', 0)
        if str(net) == f'{network}/{mask}':
            return net.num_addresses
            exit()


def find_min_one_mask(ip_adr, network):
    for mask in range(33):
        net = ip_network(f'{ip_adr}/{mask}', 0)
        if str(net) == f'{network}/{mask}':
            return mask
            exit()


def find_min_count_network(ip_adr, network):
    last_mask = None
    for mask in range(33):
        net = ip_network(f'{ip_adr}/{mask}', 0)
        if str(net) == f'{network}/{mask}':
            last_mask = net.num_addresses
    return last_mask
