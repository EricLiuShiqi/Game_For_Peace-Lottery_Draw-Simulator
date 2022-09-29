# 和平精英（Game For Peace）抽奖模拟; just for fun
from random import *

class Object():
    def __init__(self):
        self.spend = 0 # money spend in one game
        self.spendTotal = 0 # total money spend (during many times of this game, unless choose 4 to clear the data)
        self.star = 0 #current star level 
        self.EnsureLevel = 0 # Max value of 3 to ensure to increase the star level; set to zero when anytime when star level increases
        self.LevelSpend = [0, 6, 17, 51, 153, 430, 827] # star level 0 for position = 0; star level 6 for position = 6; len = 7
        self.inc_prob = [0.82, 0.17, 0.01] # the probability of increase the star level; 0.17 for for increasing 2 stars; 0.01 for increasing 3 stars
        self.dec_prob = [0.75, 0.25] # the probability of decrease the star level; 0.25 for decreasing 2 stars
        self.piecesList = [2, 12, 36, 108, 324, 960, 2880, 8640] # from star level = 0 to 7; len = 8
        self.piece = 0 # pieces get in current one game
        self.pieceTotal = 0 # cummulative pieces get 

def init():
    object_ex.spend += 6
    object_ex.spendTotal += 6
    num = randint(1,100)
    if (num > 82) and (num < 100):
        object_ex.star += 2
    elif num == 100:
        object_ex.star += 3
    else:
        object_ex.star += 1
    result_print(0)

def Normal_Draw():
    count = 0
    object_ex.spend += 0
    object_ex.spendTotal += 0
    num = randint(1,5)
    if num == 1:
        print("追加成功")
        object_ex.EnsureLevel = 0
        i = randint(1,100)
        if (i > 82) and (i < 100):
            object_ex.star += 2
        elif i == 100:
            object_ex.star += 3
        else:
            object_ex.star += 1
    else: # ending this turn
        print("追加失败")
        count = 1
        j = randint(1,4)
        if j == 4:
            object_ex.star -= 2
        else:
            object_ex.star -= 1
    
    check = True
    while check == True:
        if object_ex.star > 7:
            object_ex.star = 7
            #print("overflow")
        elif object_ex.star < 0:
            object_ex.star = 0
            #print("underflow")
        check = False
    return count
    

def Special_Draw():
    object_ex.spend += object_ex.LevelSpend[object_ex.star]
    object_ex.spendTotal += object_ex.LevelSpend[object_ex.star]
    object_ex.EnsureLevel += 1
    k = randint(1, 5)
    if (object_ex.EnsureLevel == 3) or (k == 5): # increase layer
        print("追加成功")
        object_ex.EnsureLevel = 0
        num = randint(1,100)
        if num == 100:
            object_ex.star += 3
        elif (num > 82) and (num < 100):
            object_ex.star += 2
        else:
            object_ex.star += 1
    else:                                       # decrease layer; no decrease in special_draw
        print("追加失败")
        num = randint(1,4)
        if num == 4:
            object_ex.star -= 0
        else: 
            object_ex.star -= 0
    
    check = True
    while check == True:
        if object_ex.star > 7:
            object_ex.star = 7
            #print("Star overflow")
        elif object_ex.star < 0:
            object_ex.star = 0
            #print("Star underflow")
        check = False
    

def Clear(): # every dynamic value is set to zero
    print("Warning: Reset all data")
    object_ex.spend = 0
    object_ex.spendTotal = 0
    object_ex.star = 0
    object_ex.EnsureLevel = 0
    object_ex.piece = 0
    object_ex.pieceTotal = 0

def End(): # uncummulated dynamic values are set to zeros
    print("End of this turn, starting a new turn...")
    object_ex.spend = 0
    object_ex.star = 0
    object_ex.EnsureLevel = 0 
    object_ex.piece = 0 

def Decide():
    print("0 denotes showing current data information")
    print("1 denotes normal hit")
    print("2 denotes special hit")
    print("3 denotes ending this turn and start a new turn (data cummulated)")
    print("4 denotes ending this turn and start a new turn (data all cleared)")
    print("5 denotes ending the whole program")
    num_dec = eval(input("Please input:"))
    while (num_dec > 5) or (num_dec < 1):
        #print("0 denotes stay(directly get piece without hit)")
        print("1 denotes normal hit")
        print("2 denotes special hit")
        print("3 denotes ending this turn and start a new turn (data cummulated)")
        print("4 denotes ending this turn and start a new turn (data all cleared)")
        print("5 denotes ending the whole program")
        num_dec = eval(input("*Please input in the correct format*(an integer between 1 to 5)"))
    return num_dec

def Decide2():
    print("3 denote start a new turn (data cummulated)")
    print("4 denote start a new turn (data all cleared)")
    print("5 denote ending the whole program")
    num_dec = eval(input("Please input:"))
    while (num_dec > 5) or (num_dec < 3):
        print("3 denote start a new turn (data cummulated)")
        print("4 denote start a new turn (data all cleared)")
        print("5 denote ending the whole program")
        num_dec = eval(input("*Please input in the correct format*(an integer between 3 to 5)"))
    return num_dec

def result_print(cho):
    if cho == 0:
        print("Your current star level is:", object_ex.star)
        print("You will get", object_ex.piecesList[object_ex.star],"number of pieces")
        print("Your current cummulative money spent is:", object_ex.spendTotal)

    elif cho == 1:
        print("结算:Your current star level is:", object_ex.star)
        print("结算:Your current cummulative money spent is:", object_ex.spendTotal)
        print("结算:Your cummulative number of pieces is:", object_ex.pieceTotal)
    
    else:  # cho = 2
        print(object_ex.star)
        print(object_ex.EnsureLevel)
        print(object_ex.spend)
        print(object_ex.spendTotal)
        print(object_ex.piece)
        print(object_ex.pieceTotal)

def EndCheck():
    if object_ex.star == 7:
        return 1
    elif object_ex.star == 0:
        return -1
    else:
        return 0

def overflow():
    print("You got star level >= 7, automatic ending of this turn.")
    object_ex.piece += object_ex.piecesList[object_ex.star]
    object_ex.pieceTotal += object_ex.piecesList[object_ex.star]
    result_print(1)
    End()
    run2()


def underflow():
    print("You got star level <= 0, automatic ending of this turn.")
    object_ex.piece += object_ex.piecesList[object_ex.star]
    object_ex.pieceTotal += object_ex.piecesList[object_ex.star]
    result_print(1)
    End()
    run2()

def run():  # start of run program; triggered when need artificial input
    num_dec = Decide()
    if num_dec == 0:
        result_print(2)

    elif num_dec == 1:
        count = Normal_Draw()
        if count == 1:
            print("Fail to hit. End of current turn.")
            object_ex.piece += object_ex.piecesList[object_ex.star]
            object_ex.pieceTotal += object_ex.piecesList[object_ex.star]
            result_print(1)
            run2()
        else:
            result = EndCheck()
            if result == 0:
                result_print(1)
                run()
            elif result == 1:
                overflow()
            else:   #result == -1:
                underflow()

    elif num_dec == 2:
        Special_Draw()
        result = EndCheck()
        if result == 0:
            result_print(1)
            run()
        elif result == 1:
            overflow()
        else:  # result == -1:
            underflow()

    elif num_dec == 3:
        object_ex.piece += object_ex.piecesList[object_ex.star]
        object_ex.pieceTotal += object_ex.piecesList[object_ex.star]
        result_print(1)
        End()
        main()

    elif num_dec == 4:
        object_ex.piece += object_ex.piecesList[object_ex.star]
        object_ex.pieceTotal += object_ex.piecesList[object_ex.star]
        result_print(1)
        Clear()
        main()

    else:
        object_ex.piece += object_ex.piecesList[object_ex.star]
        object_ex.pieceTotal += object_ex.piecesList[object_ex.star]
        result_print(1)
        Clear()
        print("*Ending of program*")


def run2():  # start of run2 program; triggered when systematic ending
    num_dec = Decide2()
    if num_dec == 0:
        result_print(2)

    elif num_dec == 3:
        print("Starting a new turn...")
        End()
        main()

    elif num_dec == 4:
        print("Clearing the data...")
        print("Starting a new turn")
        Clear()
        main()

    else:
        result_print(1)
        Clear()
        print("*Ending of program*")
    
def main(): # Start of main program
    input = "*Start of program*"
    init()
    run()

global object_ex
object_ex = Object()
main()
