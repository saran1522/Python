name=input("enter your name: ")
field=int(input("Ok "+name+" In which field do you want to give a quiz\npress 1 for history, 2 for sports, 3 for current affairs: "))
score=0
if(field==1):
    print("question 1:")
    print("in which year india became independent?")
    answer=int(input())
    if(answer==1947):
           score=score+1
    print(score)


