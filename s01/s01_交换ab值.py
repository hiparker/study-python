
a = 123
b = 456

c = b
b = a
a = c
print("交换位置 a = %d , b = %d ", a, b)

a = a ^ b
b = a ^ b
a = a ^ b
print("交换位置 a = %d , b = %d ", a, b)

a, b = b, a
print("交换位置 a = %d , b = %d ", a, b)
