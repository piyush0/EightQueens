import pytest

from core import runner
from db.main import put_answers, get_answers, clear_answers

if __name__ == '__main__':
    while True:
        print()
        print('1. Run n-queens for a given value of n')
        print('2. Store the solutions upto a given value in a database')
        print('3. View the database table')
        print('4. Clear the database table')
        print('5. Run tests')
        print('0. Quit')

        option = int(input('Enter a value '))

        if option == 1:
            n = int(input('Enter the value of n '))
            print(runner(n))
        elif option == 2:
            n = int(input('Enter the value of n '))
            put_answers(n)
            print('Successfully inserted the values')
        elif option == 3:
            get_answers()
        elif option == 4:
            clear_answers()
        elif option == 5:
            pytest.main()
        elif option == 0:
            break
