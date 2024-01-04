def find_volume(length=1, breadth=1, height=1):
    # Al devolver varios valores, se crea una tupla
    return length * breadth * height, "Found it!"


volume_1 = find_volume(2, 3, 4)
print(type(volume_1))  # <class 'tuple'>
print(volume_1[0])  # 24

volume_2 = find_volume(2, 3)
print(volume_2[0], volume_2[1])  # 6 Found it!

# Realiza desempaquetado de tuplas
volume_3, msg_3 = find_volume(height=20)
print(volume_3, msg_3)  # 20 Found it!
