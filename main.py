def binary(d):
    b = ''
    while True:
        if d == 0:
            break
        elif (d % 2) == 0:
            d = d // 2
            b = '0' + b
        else:
            d = d // 2
            b = '1' + b
    return b

def decimal(binary):
    binary = binary[::-1]
    d = 0
    power = 0 
    for i in binary:
        d += int(i) * (2 ** power)
        power +=1 
    return d 

def Sum(a, b):
    max_len = max(len(a), len(b))

    a = a.zfill(max_len)
    b = b.zfill(max_len)

    result = ''    
    temp = 0

    for i in range(max_len - 1, - 1, - 1):
        num = int(a[i]) + int(b[i]) + temp
        print(num)

        if num % 2 == 0:
            result = '0' + result
        else:
            result = '1' + result

        if num == 2:
            temp = 1
        else:
            temp = 0
    
    if temp !=0: 
        result = '01' + result
    
    if int(result) == 0:
        result = 0

    return result

def Sub(a, b):
    max_len = max(len(a), len(b))

    a = a.zfill(max_len)
    b = b.zfill(max_len)

    result = ''    
    temp = 0

    for i in range(max_len - 1, - 1, - 1):
        num = int(a[i]) - int(b[i]) - temp
        if num % 2 == 1:
            result = '1' + result
        else:
            result = '0' + result

        if num < 0:
            temp = 1
        else:
            temp = 0
    
    if temp !=0: 
        result = '01' + result
    
    if int(result) == 0:
        result = 0

    return result

def Multi(a, b):
    max_len = max(len(a), len(b))
    min_len = min(len(a), len(b))

    result = ''
    temp_result = ''

    temp = []
    zeroes = 0
    temp_index = 0

    for j in range(min_len - 1, - 1, - 1):
        
        temp_result = ''
        for i in range(max_len - 1, - 1, - 1):
            summ = int(a[i]) * int(b[j])
            if summ == 0:
                temp_result = '0' + temp_result
            elif summ == 1:
                temp_result = '1' + temp_result
        temp_result = temp_result + ('0' * zeroes)
        zeroes += 1
        
        temp.append(temp_result)

        if len(temp) == 2:
            result = Sum(str(temp[0]), str(temp[1]))
        elif len(temp) > 2:
            temp_index = len(temp)
            temp_index += 1
            result = Sum(str(result), str(temp[temp_index - 2]))
        else:
            pass
    return result

def Div(a, b):
    result = ''
    temp = '0'
    r = 0

    for i in range(len(a)):        
        if int(b) > int(temp):
            result += '0'
            temp += a[i]
        else:
            r = Sub(temp, b)
            if r == 0:
                temp = a[i]
                result += '1'
            else:
                r = str(r).lstrip('0')
                result += '1'
                temp = r + a[i]
    
    if temp !=int(0): 
        result = result + '0' 
                
    return result

def Or(x,y):
  a = bin(x)[2:]
  b = bin(y)[2:]
  result = int(a,2) | int(b,2)
  print(bin(result)[2:])

def And(x,y):
  a = bin(x)[2:]
  b = bin(y)[2:]
  result = int(a,2) & int(b,2)
  print(bin(result)[2:])

def Not():
    a = int(input("Digite um número: "))
    a = bin(a)[2:]
    result = int(a,2)
    result2 = ~result
    print(bin(result2)[2:])
def Xor(x, y):
  a = bin(x)[2:]
  b = bin(y)[2:]
  result = int(a,2) ^ int(b,2)
  print(bin(result)[2:])




print(' 1 - soma')
print(' 2 - subtração')
print(' 3 - multiplicação')
print(' 4 - divisão')
print(' 5 - or')
print(' 6 - and')
print(' 7 - not')
print(' 8 - xor')
c = input('Escolha uma operação ')
if c == '7':
    r = Not()
else:
    a = input('Digite o primeiro número: ')
    b = input('Digite o segundo número: ')

    a = int(a)
    b = int(b)
    
    
    ab = binary(a)
    bb = binary(b)   
    
    
    if c == '1':
        r = Sum(ab, bb)
    elif c  == '2':
        r = Sub(ab, bb)
    elif c == '3':
        r = Multi(ab, bb)
    elif c == '4':
        r = Div(ab, bb)
    elif c == '5':
        r = Or(a, b)
    elif c == '6':
        r = And(a, b)
    elif c == '8':
        r = Xor(a, b)    
    
    
    rd = decimal(r)
    
    print('binary:', r)
    print('decimal:', rd)
