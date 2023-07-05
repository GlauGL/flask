numero = int(input('Digite um número: '))
for i in range(numero):
    if i * i == numero:
        print(f'A raiz do numero {numero}={i}')
        break
    if i * i > numero:
        print('Numero não existe')
        break    
