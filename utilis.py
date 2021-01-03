from des_algorithm import Des1, Des3
from aes_algorithm import Aes
from elgamal_algorithm import ElgamalAlgorithm
from dsa_algorithm import Dsa


def get_algorithm(algorithm_number, mode):
    """
    Chooses right algorithm class based on user's input

     Parameters
    ----------
        algorithm_number : int
             Selected algorithm number

        mode : int
            Selected encryption or decryption

    Returns
    -------

    """
    try:
        if algorithm_number == 1:
            key_str = input('key: ')
            return Des1(key_str)
        elif algorithm_number == 2:
            key_str = input('key: ')
            return Des3(key_str)
        elif algorithm_number == 3:
            key_str = input('key: ')
            return Aes(key_str)
        elif algorithm_number == 4:
            p = int(input('p: '))
            if mode == 1:
                g = int(input('g: '))
                y = int(input('y: '))
                return ElgamalAlgorithm(p=p, g=g, y=y)
            if mode == 2:
                x = int(input('x: '))
                return ElgamalAlgorithm(p=p, x=x)
        elif algorithm_number == 5:
            return Dsa

    except:
        print('Initialization error, probably wrong key')
        return get_algorithm(algorithm_number, mode)


def get_int(description, minimum, maximum):
    """
    Gets input number and checks if is in right range

     Parameters
    ----------
        description : int
             Selected number

        minimum : int
            Minimum range value

        maximum : int
            Maximum range value

    Returns
    -------
        get_int(description, minimum, maximum): int
            If the input number is in wrong range or is not a number

        is_in_range(number, minimum, maximum): boolean
            If the input number is in a number and is in right range
    """
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
    """
    Returns true/false depending whether input number is in right range

    Parameters
    ----------
        number : int
             Selected number

        minimum : int
            Minimum range value

        maximum : int
            Maximum range value

    Returns
    -------
        true
            If it is within the specified range
        false
            if it is not within the specified range
    """
    return minimum <= number <= maximum
