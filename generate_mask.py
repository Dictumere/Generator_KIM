import random


def generate_mask():
    octet = [255]

    for i in range(3):
        if octet[i] == 0:
            octet.append(0)
        else:
            possible_values = [0, 128, 192, 224, 240, 248, 252, 254, 255]

            filtered_values = []

            for x in possible_values:
                if x < octet[i]:
                    filtered_values.append(x)

            next_value = random.choice(filtered_values)
            octet.append(next_value)

    mask = ".".join(map(str, octet))

    return mask


print(generate_mask())