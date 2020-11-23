import random
import datetime
Score=0
bad=0
allquestion=0
nameoftoday=datetime.datetime.now().strftime("%A")
year=datetime.datetime.now().year
print("*"*49)
alldate=datetime.datetime.now().strftime("%x")
alltime=datetime.datetime.now().strftime("%X")
print("today is {} in Year {}  : {}".format(nameoftoday,year,alldate))
print("time is = {}".format(alltime))
print("*"*49)
#list of the names language DEvelopment
list=["html","css","java","python","kotlin","php","c++","c#","ruby"]
next="yes"
while next=="yes":
    languagechoice=random.choice(list)
    print("#"*40)

    print("the category of the question is {} ".  format(languagechoice))
    print("#"*40)
#the Array of the languagechoice word in list
    q=[]
    if languagechoice=="html":
        q=["why use html","web"]
    elif languagechoice=="css":
        q=["why use css","design web"]
    elif languagechoice=="java":
        q=["why use java","application"]
    elif languagechoice=="python":
        q=["why use python","all"]
    elif languagechoice=="kotlin":
        q=["why use kotlin","application"]
    elif languagechoice=="php":
        q=["why use php","backend web"]
    elif languagechoice=="c++":
        q=["why use c++","games"]
    elif languagechoice=="c#":
        q=["why use c#","games"]
    elif languagechoice=="ruby":
        q=["why use ruby","hacker"]
#use the q Array to show question
    print("your question in language {} is:".format(languagechoice))
    print("_"*20)
    print(q[0])
    print("_"*20)
#the answer of the user in console

    answer=input("your answer is : ")
    if answer==q[1]:
        Score+=1
        print(answer)
        print("$"*10)
        print("configuration ,you wen in the game!!!!")
        print("$"*10)
    else:
        bad+=1
        print(q[1])
        print("-"*10)
        print("opps you lost in the game your question wrong!!!")
        print("-"*10)
        #the value of the variable next to continue the Game loop 
    next=input("enter yes to continue or no to exit : ")
#end the game end show Score
allquestion=Score+bad
print("^"*40)
print("bye game is ended your Score is : {} points from {} question ".format(Score,allquestion))
print("^"*40)
    
