import string
import random

def random_user_id(length):
    # 0~9 a~Z
    characters = string.digits + string.ascii_uppercase
    return ''.join(random.choice(characters) for _ in range(length))

print(random_user_id(6))

def user_id_gen_by_user(length, count) :
    for i in range(count) :
        print(random_user_id(length))

user_id_gen_by_user(12, 3)

def rgb_color_gen() :
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return f"rgb({red},{green},{blue})"

print(rgb_color_gen())


def list_of_hexa_colors(num) :
    hex_chars = '0123456789ABCDEF'
    colors = []

    for _ in range(num):
        color = '#' + ''.join(random.choice(hex_chars) for _ in range(6))
        colors.append(color)
    return colors

print(list_of_hexa_colors(3))

def list_of_rgb_colors(num) :
    colors = []
    for _ in range(num):
        color = rgb_color_gen()
        colors.append(color)
    return colors

print(list_of_rgb_colors(2))

def generate_colors(type, num) :
    colors = []
    if 'hexa' == type :
        colors = list_of_hexa_colors(num)
    elif 'rgb' == type :
        colors = list_of_rgb_colors(num)
    return colors

print(generate_colors('rgb', 10))

def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp

def shuffle_list(list) :
    shuffle_list = list.copy()

    for i in range(len(shuffle_list) - 1, 0, -1) :
        j = random.randint(0, i)
        swap(shuffle_list, i, j)
    return shuffle_list

print(shuffle_list(['1', '2', '3', '4', '5']))

def generate_unique_numbers():
    numbers = list(range(10))
    random.shuffle(numbers)
    return numbers[:7]

print(generate_unique_numbers())