# Реализуйте программу, которая будет вычислять количество различных объектов в списке.
# Два объекта a и b считаются различными, если a is b равно False.
# Вашей программе доступна переменная с названием objects, которая ссылается на список, содержащий не более 100
# объектов. Выведите количество различных объектов в этом списке.

def get_diff_objects(objects):
    id_arr = [id(objects[0])]

    for i in range(1, len(objects)):
        if not id(objects[i]) in id_arr:
            id_arr.append(id(objects[i]))
    return len(id_arr)


print(get_diff_objects([1, 2, 1, 2, 3]))
