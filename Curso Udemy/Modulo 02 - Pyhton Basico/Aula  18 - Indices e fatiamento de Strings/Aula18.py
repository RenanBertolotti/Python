"""
Manipulando Strings
* Strings indices
* Fatiamento de strings [inicio:fim:passo]
* funçoes built-in len, abs, type, print, etc...
Essas funçoes podem ser usadas diretamente em cada tipo

Voce pode conferir tudo isso em:
https://docs.python.org/3/library/stdtypes.html
https://docs.python.org/3/library/functions.html
"""

# positivos [012345678]
texto =     "Python s2"
# negativos-[876543210]

print(texto[0]) # P
print(texto[-1])# 2

novo = texto[2:6] #escolhe no começo e no fim   OU texto[:6] = vai do 0 ate o 6
novo = texto[-9:-3]

novo = texto[0:6:2] # vai do 0 ate o 6, e ele pula em 2 em 2 caracteres

print(novo)

print( len(texto))