# Напишите реализацию функции closest_mod_5, принимающую в качестве единственного аргумента целое число x и
# возвращающую самое маленькое целое число y, такое что:
#
# y больше или равно x
# y делится нацело на 5

def closest_mod_5(x):
    rem = x % 5
    if rem == 0:
        return x
    else:
        return x - rem + 5


print(closest_mod_5(13))
print(closest_mod_5(0))
print(closest_mod_5(5))
print(closest_mod_5(1722))
