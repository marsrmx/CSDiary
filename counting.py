
f = open("cuentoFinalFinal.txt", "r")
#print(f.read())
cuento = f.read()
#print(cuento)
cuento_split = cuento.split(" ")
#print(cuento_split)
words = {}

for i in cuento_split:
    if i not in words:
        words[i] = 1
    else:
        words[i] = words[i] + 1

print(words)