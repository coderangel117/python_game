import random


def main():
    test = input('I am a test')
    print(test)
    pass


def guess_number():
    number_min: int = 1
    number_max: int = 100
    random_number: int = random.randint(number_min, number_max)
    user_number = input(f'Entrez un nombre entre {number_min} et {number_max}')

    while random_number:
        pass

    if user_number > number_max or user_number < number_min:
        print('tou tou fout de ma gueule ?!')
    else:
        pass
    return number_max


if __name__ == '__main__':
    main()
