def repetir(s, r):
    resultado = ""
    contador_repetido = 0
    for i, c in enumerate(s):
        if i != 0:
            if c == s[i-1]:
                contador_repetido += 1
            else:
                contador_repetido = 0
            if contador_repetido < r:
                resultado += c
        else:
            resultado += c
    return resultado

s = "A"
r = 2

print(repetir(s, r))