from des import Des1, Des3
from abc import abstractmethod


class Algorithm:
    @abstractmethod
    def encrypt(self, data):
        pass

    @abstractmethod
    def decrypt(self, data):
        pass


def get_algorithm(algorithm_number):
    try:
        key_str = input('key: ')
        if algorithm_number == 1:
            return Des1(key_str)
        elif algorithm_number == 2:
            return Des3(key_str)
        else:
            # TODO: dodatkowy_parametr = input('coś: ')
            # TODO: return Aes(bla, bla, bla)
            pass

    except:
        print('Initialization error, probably wrong key')
        return get_algorithm(algorithm_number)


def get_int(description, minimum, maximum):
    try:
        number = int(input(description))
        if is_in_range(number, minimum, maximum):
            return number
        else:
            print('Number not in range')
            get_int(description, minimum, maximum)
    except:
        print('It is not a number')
        get_int(description, minimum, maximum)


def is_in_range(number, minimum, maximum):
    return minimum <= number <= maximum
