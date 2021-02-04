#Handle division by zero
def user_instruction():
    print("Welcome to the calculator app. The following funtionalities are avilable\n")
    print("1. Addition\n")
    print("2. Subtraction\n")
    print("3. Multiplication\n")
    print("4. Division\n")

    exit = 0
    while (exit != 1):
        option = input("Please choose from option 1-4: ")
        user_choice = option
        if (user_choice.isdigit() == True):
            if (int(user_choice) <= 4 and int(user_choice) >= 1):
                exit = 1
            else:
                print("Invalid input. Please choose from option 1-4")
        else:
            print("\nInvalid input. Please enter an integer")
    return user_choice

def take_input_a():
    exit = 0
    while(exit != 1):
        a = input("Number a: ")
        if(a.isdigit()):
            exit = 1
        else:
            print("The value you entered was not an integer. Please try again\n")
    return a

def take_input_b():
    exit = 0
    while(exit != 1):
        b = input("Number b: ")
        if(b.isdigit()):
            exit = 1
        else:
            print("The value you entered was not an integer. Please try again\n")
    return b

def add(a, b):
    sum = int(a) + int(b)
    return sum

def sub(a, b):
    diff = int(a) - int(b)
    return diff

def mult(a, b):
    mult = int(a) * int(b)
    return mult

def div(a, b):
    div = int(a) / int(b)
    return div

def main():
    option = user_instruction()
    #print("option is : " + str(option))

    print("Please input the numbers you would like to process one at a time\n")
    a = take_input_a()
    b = take_input_b()
    if(int(option) == 1):
        sum = add(a, b)
        print("\n")
        print("The sum of your numbers is: " + str(sum))
        print("\n")
    if(int(option) == 2):
        diff = sub(a, b)
        print("The difference of your numbers is: " + str(diff))
        print("\n")
    if(int(option) == 3):
        mult = mult(a, b)
        print("The product of your numbers is: " + str(mult))
        print("\n")
    if(int(option) == 4):
        div = div(a, b)
        print("Number a divided by number b is: " + str(div))
        print("\n")

if __name__ == "__main__":
    main()