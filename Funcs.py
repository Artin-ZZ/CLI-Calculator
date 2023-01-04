## Helpers Class : Contains our self made funcs that our calculator uses to calc stuff ##

# @Params:
    # plus() --> +
    # minus() --> -
    # mult() --> *
    # dev() --> /
    # mod() --> %
    # power() --> x^2
    # powxy() --> x^y

class Forb():
    def plus(num1, num2):
        result = num1 + num2
        
        print(result)
    
    def minus(num1, num2):
        result = num1 - num2
        
        print(result)
    
    def mult(num1, num2):
        result = num1 * num2
        
        print(result)
    
    def dev(num1, num2):
        result = num1 / num2
        
        print(result)
    
    def mod(num1, num2):
        result = num1 % num2
        
        print(result)
        
    def power(num1):
        result = num1 * num1
        
        print(result)
        
    def powxy(num1, num2):
        result = num1 ^ num2
        
        print(result)
