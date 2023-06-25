#random guess number
import random
r = random.randint(1,100)
while(True):
    i = int(input())
    if(i<r):
        print("Wrong guess, Please try greater number")
    elif(i>r):
        print("wrong guess, please try smaller number")
    else:
        print("Congrats ,You guess right")
        break;
