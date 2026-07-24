numero = 17

primo = True

for i in range(2, numero):
    if numero % i == 0:
        primo = False
        break

if primo:
    print("É primo")
else:
    print("Não é primo")
