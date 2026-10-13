def prob1() -> list[int]:
    n = int(input())
    prob1_la_patrat = lambda x : x**2
    lista = [prob1_la_patrat(x) for x in range(1,n+1)]
    print("_".join(map(str,lista)))
    return lista

def prob2() -> list[int]:
    count = int(input())
    suma = int(input())
    lista = [(i,suma-i) for i in range(1,count+1)]
    print(lista)

def prob3() -> None:
    lista = []
    while True:
        cmd = input().split()
        if cmd[0] == "PRINT":
            print(lista)
        if cmd[0] == "APPEND":
            lista.append(cmd[1])
        if cmd[0] == "REMOVE":
            if lista.index(cmd[1]) != -1:
                lista.remove(cmd[1])
            else:
                print("Doesn't exist")
        if cmd[0] == "INSERT":
            lista.insert(int(cmd[1]),cmd[2])
        if cmd[0] == "INIT":
            lista = []
        if cmd[0] == "EXIT":
            return

def prob4() -> None:
    rows = int(input())
    cols = int(input())
    lista = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            num = int(input())
            lista[i][j] = num
    for i in range(rows):
        for j in range(cols):
            if i%2 == 0:
                if lista[i][j] %2 == 1:
                    lista[i][j] = 'X'
            elif i%2 == 1:
                if lista[i][j] %2 == 0:
                    lista[i][j] = 'X'
    print(lista)

prob1()
prob2()
prob3()
prob4()