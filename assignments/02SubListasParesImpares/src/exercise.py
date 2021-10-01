def main():
    #escribe tu código abajo de esta línea
    a = input()
    pares = []
    impares = []
    while a != '*' :
        e = int(a)
        if e%2==0:
            pares.append(e)
        else:
            impares.append(e)
        a = input()
    print('PARES')
    print(pares)
    print('IMPARES')
    print(impares)


if __name__=='__main__':
    main()
