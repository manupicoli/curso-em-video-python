a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a + b > c and a + c > b and b + c > a:
    print('Os segmentos acima PODEM formar triângulo!')
    if  a == b and b != c and a != c or a == c and c != b and a != b or b == c and b != a and c != a:
        print('O triâgulo formado será isósceles')
    elif a == b == c:
        print('O triângulo formado será equilátero!')
    else:
        print('O triângulo formado será escaleno!')
        
#tb podia ser if a == b == c 
#   print('equilatero')
# elif a != b != c
#   print('escaleno')
# else:
#   print('isosceles)

else:
    print('Os segmentos acima NÃO PODEM formar triângulo!')