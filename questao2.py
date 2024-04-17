fib = [0,1]
num = int(input('Digite um número: '))
for i in range(2, 30):
  proxNum = fib[-1] + fib[-2]
  fib.append(proxNum)

if num in fib:
  print('Este numero pertece a sequencia fibonacci')
else:
  print('Este numero não pertence a sequencia fibonacci')
print(fib)