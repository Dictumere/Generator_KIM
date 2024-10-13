from generate_mask import generate_mask
from generate_ipv4 import generate_ipv4
from solution import solution


def main():
    ip = generate_ipv4()
    mask = generate_mask()

    print(f"""
В терминологии сетей TCP/IP маской сети называют двоичное число, которое 
показывает, какая часть IP-адреса  узла сети относится к адресу сети, а какая – к адресу узла 
в этой сети. Адрес сети получается в результате применения поразрядной конъюнкции к 
заданному адресу узла и его маске. По заданным IP-адресу узла сети и маске определите адрес сети: 
IP-адрес: {ip}
Маска: {mask}
""")

    answer = input('Введите ваш ответ: ')
    right_solution = solution(ip, mask)
    if answer == right_solution:
        print('Ответ верный!')
    else:
        print('Попробуй еще раз!')

    print(f'Правильный ответ: {right_solution}')


if __name__ == '__main__':
    main()