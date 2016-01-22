__author__ = 'student'

# Function a acts as a simple counter,
# using a while loop makes the function add '1'
# until the statement is no longer true

def a ():

    '''
    Write a while loop that counts from 0 to 10, inclusive.
    Print out each number.
    :return: None
    '''

    number=0
    while number <= 10:
        print (number)
        number=number +1



# Function b1 uses a while loop (similar to function a)
# to count from 0 to any positive number n, that the user wants

def b1(n):

    '''
    Count from 0 to n inclusive. Print out each number.
    Use a while loop.
    :param n: an integer
    :return: None
    '''

    number=0
    if n>=0:
        while number <= n:
            print (number)
            number=number +1



# Function b2 counts from 0 to any positive number n, but uses a for loop

def b2(n):

    '''
    Count from 0 to n inclusive. Print out each number.
    Use a for loop.
    :param n: an integer
    :return: None
    '''

    number=0
    if n > 0:
        for number in range (0,n+1):
            print (number)



# Function get_input asks users to input a number between 1-3
# Since the function must continue until a valid number is entered, an infinite while loop is used
# and break is used to stop the loop when desired number is inputted
# if not xfirst.isdigit() is used to make sure that the function sees strings as an invalid input

def get_input():

    '''
    Continually prompt the user for a number, 1,2 or 3 until
    the user provides a good input. You will need a type conversion.
    :return: The users chosen number as an integer
    '''

    while True:
        xfirst= input("Give me 1,2 or 3: ")
        if not xfirst.isdigit():
            print("Invalid Input")
            continue
        x=int(xfirst)
        if x>3:
          print("Invalid Input")
        elif x<1:
            print("Invalid Input")
        else:
            return x
            break



# Function c asks for a number between 1 and 3
# then it counts from 0 to the inputted number

def c():

    '''
    Write a few lines of code which does the following.
    Ask the user to input a 1,2 or 3.
    If the user enters anything else, then tell the user
    they did something wrong, and prompt them again for a good input.
    Hint: use get_input()
    Hint: use another function above.
    Once the user enters the number, counts from 0 to the number and then returns.
    :return: None
    '''

    while True:
        xfirst= input("Give me 1,2, or 3: ")
        if not xfirst.isdigit():
            print("Invalid Input")
            continue
        x=int(xfirst)
        if x>3:
          print("Invalid Input")
        elif x<1:
            print("Invalid Input")
        else:
            b1(x)
            break
    return None



# Function d, If a valid number is entered, then it is added to the total value and then printed

def d():

    '''
    Write a few lines of code which does the following...
    Same as in c(), but this time, keep track of the total
    of all numbers (1,2,3) input so far. Exit when the total
    is 25 or more. You don't actually have to count to the input
    number, just add it.
    :return: None
    '''

    sum=0
    while sum<25:
        xfirst= input("Give me 1,2 or 3: ")
        if not xfirst.isdigit():
            print("Invalid Input")
            continue
        x=int(xfirst)
        if x>3:
          print("Invalid Input")
        elif x<1:
            print("Invalid Input")
        else:
            sum=sum + x
            print ("Total is ",sum )
    return None



# Function e, A condition is added to make sure that the sum doesnt exceed 25
# If it does, then the function warns the user until a valid number is entered

def e():

    '''
    Same as in d(), but this time, make sure that the user can't enter
    a number that would put the total over 25.
    :return: None
    '''

    sum=0
    while sum<25:
        xfirst= input("Give me 1,2 or 3: ")
        if not xfirst.isdigit():
            print("Invalid Input")
            continue
        x=int(xfirst)
        if x>3:
          print("Invalid Input")
        elif x<1:
            print("Invalid Input.")
        elif sum+x>25:
            print ("The number you chose would put the total over 25. Try Again.")
        else:
            sum=sum+x
            print ("Total is ",sum )
    return None



# Function get_input_from_player is exactly the same as get_input
# it just addresses the player before asking the question

def get_input_from_player(player):

    '''
    This is the same as get_input, except this time, the prompt includes which player
    is supposed to supply the input.
    :param player: The player, either 1 or 2
    :return: An integer, either 1,2 or 3
    '''

    print ('Hello Player', player,'.')
    while True:
        xfirst= input("Give me 1,2 or 3: ")
        if not xfirst.isdigit():
            print("Invalid Input")
            continue
        x=int(xfirst)
        if x>3:
            print("Invalid input")
        elif x<1:
            print("invalid input")
        else:
            break
    return x



# Function f has a condition in the if statement to change the value if the player value if the
# inputted number is valid

def f():

    '''
    Same as in e(), but ths time, print out which players move it is,
    on each turn. There are 2 players, Player 1 starts and they alternate.
    Hint: add a player variable, as well as use get_input_from_player(player)
    :return: None
    '''

    sum=0
    player=1
    while sum<25:
        xfirst= input("Player " + str(player) + " Give me 1,2 or 3: ")
        if not xfirst.isdigit():
            print("Invalid Input")
            continue
        x=int(xfirst)
        if x>3:
          print("Invalid input")
        elif x<1:
            print("Invalid input")
        elif sum+x>25:
            print ("The number you chose would put the total over 25. Try Again.")
        else:
            sum=sum+x
            print ("Total is ",sum )
            if player == 1:
                player =2
            elif player ==2:
                player=1



# Define a function with two variables:
# integer player - an integer which marks which player's turn it currently is.
# integer sum - an integer which is passed in which is the current sum of the race.
# This acts as a simple function that gets an input from the players and makes sure the input is correct
# I used this to make the final function more simpler

def get_input_check_overflow(player, sum):
    while True:
        xfirst= input("Player " + str(player) + " Give me 1,2 or 3: ")
        if not xfirst.isdigit():
            print("Invalid Input")
            continue
        x=int(xfirst)
        if x>3:
          print("Invalid Input")
        elif x<1:
            print("Invalid Input")
        elif sum+x>25:
            #We need to check if the sum + and the number entered is higher than the maxNumber. If it is, we print the message to alert the user,
            #and then continue the loop.
            print ("The number you chose would put the total over 25. Try Again.")
        else:
            return x
            break



# raceto25 asks users to input numbers from 1-3 and the first one to get to 25 is the winner

def raceto25():

    '''
    Same as in f(), but this time, print out which player won, before returning.
    :return: None
    '''

    sum=0
    player=1
    #We can use the while statement for flow control, but we are opting not to, and using break. So, we use True to get infini loop.
    while True:
        #I can call the function inside the equation, the function will first be resolved, and give you the user input.
        sum= sum + get_input_check_overflow(player,sum)
        print("The total is "+str(sum))
        if sum==25:
            print("Player "+ str(player)+ " Won!")
            break
        if player == 1:
            player =2
        elif player ==2:
            player=1



# This function is another custom function and is the same as the previous one
# The difference is that this one is not limited to 25, but rather any number the user desires

def get_input_check_overflow_v2(player, sum, maxCount):
    while True:
        xfirst= input("Player " + str(player) + " Give me 1,2 or 3: ")
        #Validate that the input is not empty nor a non-numerical integer string
        if not xfirst.isdigit():
            print("Invalid Entry")
            continue
        x=int(xfirst)
        if x>3:
            print("The Number You Chose is Larger than 3. Try Again")
        elif x<1:
            print("The Number You Chose is Smaller than 1. Please Try Again")
        elif sum+x>maxCount:
            #We need to check if the sum + and the number entered is higher than the maxNumber. If it is, we print the message to alert the user,
            #and then continue the loop.
            print ("The Number you entered will go higher than "+str(maxCount) +" when added with the sum. Try again.")
        else:
            return x
            break



# Same as raceto25 but lets users input any number they want to play up to
# Have fun!

def raceTo(m):

    '''
    define function raceTo below, which is the same as raceTo25,
    but has a parameter m. A call to raceTo(25) behaves as raceTo25() above does.
    A call to raceTo(17) is the same as raceTo25, but the winner is the player
    that forces the total to 17. A call to raceTo(100) is the same as raceTo25,
    but the winner is the player that forces the total to 100.
    '''

    sum=0
    player=1
    #We can use the while statement for flow control, but we are opting not to, and using break. So, we use True to get infini loop.
    while True:
        #I can call the function inside the equation, the function will first be resolved, and gives the user input.
        sum= sum + get_input_check_overflow_v2(player,sum, m)
        print("The total is "+str(sum))
        if sum==m:
            print ("Player "+ str(player)+ " Won")
            break
        if player == 1:
            player =2
        elif player ==2:
            player=1



#a()
#b1(0)
#b1(-5)
#b1(15)
#b2(0)
#b2(-5)
#b2(15)
#get_input()
#c()
#d()
#e()
#get_input_from_player(1)
#get_input_from_player(2)
#f()
#raceTo25()
#raceTo(25)
#raceTo(17)
#raceTo(100)