import re

def uno():
    D = [
        {"make": "Nokia", "model": 216,  "color": "Black"}, 
        {"make": "Apple", "model": 2, "color": "Silver"}, 
        {"make": "Huawei", "model": 50, "color": "Gold"},
        {"make": "Samsung", "model": 7, "color": "Blue"}
    ]

    def Sort(key_indicado):
        D.sort(key = lambda x: x[key_indicado])
        return D
    
    regex = "^[012]$"

    keys = ["make", "model", "color"]
    print("Ingrese el numero de la key por el que desea ordenar:\n0) make\n1) model\n2) color")
    key = input("Ingrese el key: ")

    if(re.match(regex, key)):

        print(f"Ordenado por {keys[int(key)]}")
        ord = Sort(keys[int(key)])
        for value in ord:
            print(value)

    else:
        print("Entrada invalida")

def dos():
    displayList = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10]

    def power(n):
        return list(map(lambda x: x**n, displayList))
    
    n = input("Ingrese le valor de n para la potencia: ")

    regex = r"^-?\d+$"

    if(re.match(regex, n)):
        print(power(int(n)))
        
    else:
        print("la potencia tiene que ser un numero entero")

def tres():
    x = [[1,2,3,1],
        [4,5,6,0], 
        [7,8,9,-1]]

    def transpose():
        return list(map(lambda *x: list(x), *x))
    
    y = transpose()
    for yRow in y:
        print(yRow)

def cuatro():
    arr = ['rojo', 'verde','azul', 'amarillo', 'gris', 'blanco', 'negro']
    delArr = []

    def deleteElement(delete):
        return list(filter(lambda x: x not in delete, arr))

    print("Lista incial"+str(arr))
    while True:
        element = input("Ingrese un elemento a borrar: ")
        delArr.append(element)

        opc = input("Desea agregar otro elemento: \n0) Si\n1) No\nQue desea hacer?: ")
        if(opc != "0"):
            break

    print("Lista depues de borrar los elementos: ")
    print(deleteElement(delArr))

print("EJERCICIO 1")
uno()
print("\nEJERCICIO 2")
dos()
print("\nEJERCICIO 3")
tres()
print("\nEJERCICIO 4")
cuatro()