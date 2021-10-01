def main():
    #escribe tu código abajo de esta línea
    listaUno = []
    listaDos = []
    sumaListas = []
    n = int(input('Número de elementos en las listas: '))
    if n>0 :
        for i in range(n):
            a = int(input('Número '+str(i)+' de la lista Uno: '))
            listaUno.append(a)
        for i in range(n):
            b = int(input('Número '+str(i)+' de la lista Dos: '))
            listaDos.append(b)
        for i in range(n):
            c = listaUno[i]+listaDos[i]
            sumaListas.append(c)
            c = 0
        print(sumaListas)
    else:
        print('Error')

if __name__=='__main__':
    main()
