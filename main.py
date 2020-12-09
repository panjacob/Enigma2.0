from kuba import des, des3

# TODO: Jak wprowadzisz cos innego niz int powtorz zapytanie
mode = int(input('mode: 1- encrypt | 2- decrypt: '))
algorithm_name = int(input('algorithm: 1- DES | 2- 3DES | 3- AES: '))
data = input('data: ')

if algorithm_name == 1:
    algorithm = des
elif algorithm_name == 2:
    algorithm = des3
else:
    pass

# result = algorithm.encrypt(mode, data)

result = algorithm(mode, data)
print(result)
