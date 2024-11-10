from random import randint


def generate_ip():
    result = [randint(10, 223) for _ in range(4)]
    result = ".".join(map(str, result))
    return result


def generate_mask(count1):
    """
    Функция создания маски сети по количеству единиц в ней

    :param count1: количество единиц в маске сети
    :return: маска сети в виде списка из 4 целых чисел из диапазона 0..255
    """
    result = []
    byte = [0, 128, 192, 224, 240, 248, 252, 254, 255]
    for _ in range(4):
        if count1 > 8:
            result.append(byte[8])
        else:
            result.append(byte[count1])
        count1 = count1 - 8 if count1 >= 8 else 0
    result = ".".join(map(str, result))
    return result


def generate_net(mask):
    ip = generate_ip()
    result = [ip[i] & mask[i] for i in range(4)]
    return result


def get_random_ip(net, mask):
    result = []
    for i in range(4):
        if mask[i] == 255:
            result.append(net[i])
        else:
            result.append(net[i] + randint(1, 255 - mask[i] - 1))
    return result
