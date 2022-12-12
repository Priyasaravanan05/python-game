import random
class Game:
    def __init__(self,score):
        self.score=score
        
class State:
    def __init__(self,state):
        self.state=state

def state_check(state):
    p3.state=state

def condition_check(ch,rlist1,rlist2):
    for i in range(5):
        if ch == rlist1[i] or ch == rlist2[i]:
            p1.score = p1.score-rlist2[i]
            p2.score = p2.score-rlist1[i]
            print("Player1:",p1.score)
            print("Player2:",p2.score)
            if p3.state == 0:
                p3.state=1
            else:
                p3.state=0
            break
        if i== 5:
            if p3.state == 0:
                p3.state=1
            else:
                p3.state=0

def player1(score1):
    score1=score1
    rlist2=[0,0,0,0,0]
    rlist1=random.sample(range(1,100),5)
    print(rlist1)  
    ch1 = int(input("Player -1, Enter any one number from the list: "))
    condition_check(ch1, rlist1,rlist2)
    if p3.state ==1:
        if p1.score>0 and p2.score>0:
            player2(p2.score)
        else: 
            print("GAME OVER, Player 1 Wins")
    else:
        print("Player-1, Entered Value is invalid")
        print("Player1:",p1.score)
        print("Player2:",p2.score)
        player1(score1)
        

def player2(score2):
    score2=score2
    rlist1=[0,0,0,0,0]
    rlist2=random.sample(range(1,100),5)
    print(rlist2)
    ch2 = int(input("Player-2, Enter any one number from the list: "))
    condition_check(ch2, rlist1,rlist2)
    if p3.state ==0:
        if p1.score>0 and p2.score>0:
            player1(p1.score)
        else: 
            print("GAME OVER, Player 2 Wins")
    else:
        print("Player-2, Entered Value is invalid")
        print("Player1:",p1.score)
        print("Player2:",p2.score)
        player2(score2)        

score1=100
score2=100
state=0
p1=Game(score1)
p2=Game(score2)
p3=State(state)
state_check(p3.state)
player1(p1.score)