def show_menu() :
    print("[0] check palindrome \t [1]check if prime \n[99] Exit")
    return


def is_prime() :
    x=0
    try :
        num = int(input("Enter the num : "))
    except :
        print("invalid input\n")
    else :
        if num == 1 or num ==0:
            print(str(num) + " is a not prime number\n")
        elif num == 2:
            print(str(num) + " is a prime number\n")
        elif num != 1 and num != 2:
            for i in range(2, int(num)):
                if num % i == 0:
                    x = 1
            if x == 0:
                print(str(num) + " is a prime number\n")
            else:
                print(str(num) + " is a not prime number\n")


def is_palindrome() :
    word= input("Enter the word you want to check : ")
    y=""
    for i in range(len(word)-1,-1,-1) :
        y += word[i]
    if y == word :
        print("yes\n")
    else :
        print("No\n")


show_menu()
choice = input("")
while choice != "99" :
    if choice == "0" :
        is_palindrome()
        show_menu()
        choice = input("")
    elif choice == "1":
        is_prime()
        show_menu()
        choice = input("")
    else :
        print("invalid input")
        show_menu()
        choice = input("")




