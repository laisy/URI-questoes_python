N = int(input())
while N > 0:
      lista = input().split(' ')
      maior = -1
      segMaior = -1
      im = 0
      ise = 0

      for i in range(len(lista)):
            lista[i] = int(lista[i])

      for i in range(len(lista)):
            if lista[i] > maior:
                  segMaior = maior
                  ise = im
                  maior = lista[i]
                  im = i
            elif lista[i] > segMaior:
                  segMaior = lista[i]
                  ise = i

      print (ise + 1)
      N = int(input())
