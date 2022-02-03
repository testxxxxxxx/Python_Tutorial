# Тип текста str
# Числовые типы int, float, complex
# Типы последовательностей list, tuple, range
# Тип отображения dict
# Типы наборов set, frozenset
# Логичесткий тип bool
# Бинарные типы bytes, bytearray, memoryview

x = "Hello World"
print(type(x)) # str

x = 20
print(type(x)) # int

x = 20.5
print(type(x)) # float

x = 1j
print(type(x)) # complex

x = ["apple", "banana", "cherry"]
print(type(x)) # list

x = ("apple", "banana", "cherry")
print(type(x)) # tuple

x = {"apple", "banana", "cherry"}
print(type(x)) # set

x = range(7) # range
print(type(x))

x = {"name" : "Vlad", "age" : "26"}
print(type(x)) # dict

x = frozenset({"apple", "banana", "cherry"})
print(type(x)) # frozenset

x = True
print(type(x)) # bool

x = b"Hello"
print(type(x)) # bytes

x = bytearray(5)
print(type(x)) # bytearray

x = memoryview(bytes(5))
print(type(x)) # memoryview

print("####")

# Установка определенного типа данных
x = str("Hello World")
print(x) # Hello World

x = int(20)
print(x) # 20

x = float(20.5)
print(x) # 20.5

x = complex(1j)
print(x) # 1j

x = list(["apple", "banana", "cherry"])
print(x) # ['apple', 'banana', 'cherry']

x = tuple(("apple", "banana", "cherry"))
print(x) # ('apple', 'banana', 'cherry')

x = range(7)
print(x) # range(0, 7)

x = dict(name="Vlad", age=37)
print(x) # {'name': 'Vlad', 'age': 37}

x = set({"apple", "banana", "cherry"})
print(x) # {'apple', 'banana', 'cherry'}

x = frozenset({"apple", "banana", "cherry"})
print(x) # frozenset({'cherry', 'banana', 'apple'})

x = bool(5)
print(x) # True

x = bytes(5)
print(x) # b'\x00\x00\x00\x00\x00'

x = bytearray(5)
print(x) # bytearray(b'\x00\x00\x00\x00\x00')

x = memoryview(bytes(5))
print(x) # <memory at 0x0000022B5652D9C0>

#########
# Кортежи изменять нельзя
# Кортежи меньше весят
# Кортежи быстрее в производительности
lst = [1, 2, 3]
tpl = (1, 2, 3)

print("Размер списка " + str(lst.__sizeof__())) # 104
print("Размер кортежа " + str(tpl.__sizeof__())) # 48

print(tpl[0]) # 1
print(list(tpl)) # [1, 2, 3]
print(tuple(lst)) # (1, 2, 3)