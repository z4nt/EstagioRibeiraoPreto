stri = list(input('Insira uma palavra: '))
k = 0
l = -1
for i in range(len(stri)//2): 
    stri[k], stri[l] = stri[l], stri[k]
    k = k + 1
    l = l - 1
print(''.join(stri))