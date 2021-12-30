import random
name=input("PLEASE ENTER YOUR NAME ")
print("HELLO",name,"WELCOME  TO COWS AND BULLS GAME ")
def Secretnum():
    num=list(range(10))
    random.shuffle(num)
    return num
def getsecretnum():
    number=Secretnum()
    secret_numlist=[]
    for i in range(5):
        secret_numlist.append(number[i])
    a=[]
    for i in secret_numlist:
        b=str(i)
        a.append(b)
    return a
def cow_bull():
    b=getsecretnum()
    tries=0
    while tries<=4:
        cow=0
        bull=0
        guess = int(input("Enter your guess in 5 digit : "))
        guess_in_str=str(guess)
        if len(guess_in_str)==5:
            strguess=str(guess)
            l=[]
            for i in range(len(strguess)):
                l.append(strguess[i])
            list=[]
            for j in range(len(l)):
                if l[j] not in list:
                    list.append(l[j])
                    if l[j] in b:
                        cow=cow+1
                    if l[j]==b[j]:
                        bull=bull+1
                elif l[j] in list:
                    print(" sorry, Number should not have repeated digits ,plz Try again.")
                    break
        else:
            print("sorry,number is not in 5 digit so,please enter 5 digit no.")
            continue
        print("cow = ",cow,"  ","bull =",bull)
        if bull==5:
            print("waoo! , you are winner :-)")
            break
        tries=tries+1
    if bull!=5:
        print("oops! , you are looser :-(") 
        print("your secret number =",getsecretnum())           
cow_bull()
def play_again():
    while True:
        again=input("If you Want to play again press y for yes or N of No  =") 
        if again=="y":
            cow_bull()
        else:
            break 
play_again()
            




