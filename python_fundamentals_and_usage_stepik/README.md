Course: https://stepik.org/course/512/syllabus

## Модель данных. Объекты

Все данные в питоне хранятся в ОП как объекты.
Каждый объект обладает тремя обязательными свойствами:

-   идентификатор — характеризует адрес в памяти
-   тип — характеризует возможное принимаемое значение и набор действий, возможных в отношении объекта
-   значение

Оператор присваивания даёт интерпретатору команду связать имя из левой части с идентификатором объекта из правой части

```python
x = 5
id(x) # получить идентификатор
type(x) # получить тип
```

Объекты бывают изменяемые(mutable) и неизменяемые (immutable). Это зависит от _типа_ объекта.

##### Immutable

-   числа (int, float, complex)
-   строки (str)
-   булевы значения (bool)
-   кортежи (tuple)
-   frozenset

##### Mutable

-   списки (list)
-   словари (dict)
-   множества (set)

Интерпретатор не создаёт новые объекты для неизменяемых типов.
Для изменяемых типов новый объект создаётся каждый раз при появлении значения такого типа

## Функции и стек вызовов

Функции используются для:

-   переиспользования кода
-   структурирования кода
-   сокрытия деталей реализации

#### Стек вызовов

Стек — абстрактная структура данных по принципу LIFO

#### Способы передачи аргументов в функцию

```python
def printab(a, b):
    print(a, b)

printab(10, 20)
printab(a = 10, b = 20)

lst = [10, 20]
printab(*lst)

args = {'a': 10, 'b': 20}
printab(**args)
```

#### Аргументы по умолчанию

```python
def printab(a,b):
    return 0
def printab(a,b = 20):
    return 0
def printab(a = 10,b = 20):
    return 0
# Некорректная запись, аргументы по умолчанию должны идти после обычных
def printab(a = 10, b):
    return 0
```

#### Неопределённое число аргументов

##### Неименованные дополнительные аргументы
```python
def printab(a, b, *args):
    print(a) # Print positional argument a
    print(b) # Print positional argument b
    for i in args: # Print all additional arguments
        print(i)
printab(10, 20, 30, 40, 50)

# 10
# 20
# 30
# 40
# 50
```

##### Именованные дополнительные аргументы
```python
def printab(a, b, **kwargs):
    print(a) # Print positional argument a
    print(b) # Print positional argument b
    for key in kwargs: # Print all additional arguments
        print(key, kwargs[key])

printab(10, 20, c = 30, d = 40, jimmy = 50)
# 10
# 20
# c 30
# d 40
# jimmy 50
```

#### Синтаксически верное определение функции

```python
def function_name([positional args,
                  [positional_args_with_default,
                  [*pos_args_name,
                  [keyword_only_args,
                  [**kwargs_name]]]]])
```
