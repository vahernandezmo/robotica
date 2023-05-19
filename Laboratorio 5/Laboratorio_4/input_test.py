valor = int(input(f'''Ingrese la pose a la que desea ir:
            1. Home [0, 0, 0, 0, 0]
            2. P1   [-25, 15, -20, 20, 0]
            3. P2   [ 35,-35, 30, -30, 0]
            4. P3   [-85, 20, -55, 17, 0]
            5. P4   [-80, 35, -55, 45, 0]
            '''))

if valor == 1:
    print(1)
elif valor == 2:
    print(2)
elif valor == 3:
    print(3)
elif valor == 4:
    print(4)
elif valor == 5:
    print(5)
else:
    print(6)