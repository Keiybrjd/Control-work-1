a = int(input("Длина 1:"))
b = int(input("Ширина 1:"))
h = int(input("Высота 1:"))
A = int(input("Длина 2:"))
B = int(input("Ширина 2:"))
H = int(input("Высота 2:"))

V1 = a*b*h
V2 = A*B*H

if V1<V2:
    print(V2,"Больше")
elif V1>V2:
    print(V2,"Меньше")