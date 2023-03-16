def fibonacci(n):
    a, b = 0, 1
    while b <= n:
        if b == n:
            return f"{n},pertence a sequência de Fibonacci"
        a, b = b, a + b
    return f"{n}, não pertence a sequência de Fibonacci"


while True:
    num = int(input('insira um número: '))
    print(fibonacci(num))
    continuar = input('para cancelar digite: "N" ')
    if continuar == 'N':
        break
