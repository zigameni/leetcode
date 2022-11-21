def printJN(x):
    # iterating over all the numbers from 0 to X

    for i in range(x+1):
        if(i<10):
            print(f"Jumping number: {i}")
            continue

        # check tracks if the number is valid
        check = 1
        temp = i # number  
        digit = temp%10 # the second digit
        temp//=10       # thef first number 
        
        while(temp>0):
            if(abs(digit-temp%10)!= 1):
                check = 0
                break
        
            digit = temp%10
            temp//=10


        # print i if check is 1
        if(check):
            print(i, end=" ")

# runner code
if __name__ == "__main__":
    x = 101210
    printJN(x)