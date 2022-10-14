def myDecorator(func):
    def nestedFunc(): 
        
        print("first test")
        
        func()
        
        print("final test")
    return nestedFunc  

# Sugar Syntax 
@myDecorator
def hello():
    print("Hello")

hello()    