## Importing our local self made module ##
from Funcs import Forb
## Importing Built in Python Libs
import time as tm


## Main Class ##
class Main():
    ## Constractor ##
    def __init__(self):
        w = 0
        ## Main Loop ##
        while w==0:
            ## our main menu ##
            try:
                txt =  "######### Menu ########\n"
                txt += "# 1.Add Two Nums      #\n"
                txt += "# 2.Minus Two Nums    #\n"
                txt += "# 3.Mult Two Nums     #\n"
                txt += "# 4.Devide Two Nums   #\n"
                txt += "# 5.Mod Of Two Nums   #\n"
                txt += "# 6.Power Nums X^2    #\n"
                txt += "# 7.Power of two Nums #\n"
                txt += "# 8.Exit              #\n"
                txt += "#######################\n"
                print(txt)
                ## menu end ##
                
                ## main input text field (DataType : int)##
                a_field = int(input('choose an option: '))
                
                ## Menu Conditions
                if a_field == 1:
                    num1 = int(input('Num 1: '))
                    num2 = int(input('Num 2: '))
                    Forb.plus(num1, num2)
                    tm.sleep(5)
                    
                
                elif a_field == 2:
                    num1 = int(input('Num 1: '))
                    num2 = int(input('Num 2: '))
                    Forb.minus(num1, num2)
                    tm.sleep(5)
                    
                    
                elif a_field == 3:
                    num1 = int(input('Num 1: '))
                    num2 = int(input('Num 2: '))
                    Forb.mult(num1, num2)
                    tm.sleep(5)
                    
                
                elif a_field == 4:
                    num1 = int(input('Num 1: '))
                    num2 = int(input('Num 2: '))
                    Forb.dev(num1, num2)
                    tm.sleep(5)
                    
                
                elif a_field == 5:
                    num1 = int(input('Num 1: '))
                    num2 = int(input('Num 2: '))
                    Forb.mod(num1, num2)
                    tm.sleep(5)
                    
                elif a_field == 6:
                    num1 = int(input('Number: '))
                    Forb.power(num1)
                    tm.sleep(5)
                    
                elif a_field == 7:
                    num1 = int(input('Num 1: '))
                    num2 = int(input('Num 2: '))
                    Forb.powxy(num1, num2)
                    tm.sleep(5)
                    
                elif a_field == 8:
                    exit()
                    
                
                else:
                    break
                ## Menu Conditions End ##
                
            ## Handle Value Error If str is to be put in our input ##    
            except ValueError:
                print('Must Be Of Type INT')
                tm.sleep(3)

        
## Runs The Whole App ##     
if __name__ == "__main__":
    run = Main()