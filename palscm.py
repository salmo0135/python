"""
Luke Salmon
A01167625
Set C
"""
"""
Command line arguments for palindromes searching
"""

import sys


def number_of_iterations(num: int, reverse_num: int) -> (print):
    """Excepts a list as in put looping through each integer to find its palindrom"""
    palindrome = True
    total = 1
    add_num = num + reverse_num
    while palindrome != False:
        new_reverse_num = int(str(add_num)[::-1])
        if add_num == new_reverse_num:
            palindrome = False
            print(total, add_num)
        else:
            add_num = add_num + new_reverse_num
            total += 1


def main():


    iterations = 1
    while iterations <= len(sys.argv)-1:
        """this program excepts command line arguments to find integer palindromes"""
        try:
            num = int(sys.argv[iterations])
            reverse_num = int((sys.argv[iterations])[::-1])
            if num == reverse_num:
                print('no iterations needed already a palindrome')
            elif num == 196:
                print('no palindrome is understood to be found')
            else:
                number_of_iterations(num, reverse_num)
                iterations += 1
        except ValueError:
            """will throw an excpetion if string cannot be converted to integer"""
            print(f'Bad Data {sys.argv[iterations]}')
            iterations += 1

main()
