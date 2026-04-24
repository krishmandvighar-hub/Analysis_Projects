import random
print("enter numbers upto 1 to 10")
number = random.randint(1,10)

while True:
    try:
        guess =int(input("guess number: "))
        if guess==number:
            print("correct")
            break

        else:
            print("try again")
    except:
        print("enter invalid number")



        
