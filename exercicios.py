numeros = [1,2,3,4,5,6,7,8,9,10]
nomes = ['Gabriel','maria','João']
anoAtual = [2004, 2024]

#for numero in numeros:
 #   print(f'.{numero}')

soma_impares = 0
for i in range(1,11,2):
    soma_impares += i
print(soma_impares)

for i in range(10,0,-1):
    print(i)

numero_tabuada = int(input('Digite um numero')) 
for i in range(1,11):
 resultado = numero_tabuada * i
print(f"{numero_tabuada} x {i} = {resultado}")