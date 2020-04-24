import sys

def number_of_iterations(num: int, reverse_num: int)->(list):
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


    get_user_input = input("Enter a number: ")
    try:
        num = int(get_user_input)
        reverse_num = int((get_user_input)[::-1])
        if num == reverse_num:
            print('no iterations needed already a palindrome')
        elif num == 196:
            print('There is believed to be no palindrome for this number')
        else:
            number_of_iterations(num,reverse_num)
    except ValueError:
        print(f'{get_user_input} bad value')







main()