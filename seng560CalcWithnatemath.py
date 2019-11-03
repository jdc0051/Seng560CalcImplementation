from natemath import *

def validateMenu(inputValue):
    try:
        test = int(inputValue)
        return True
    except:
        return False
        
def validateFloat(inputValue):
    try:
        test = float(inputValue)
        return True
    except:
        return False

def main():
    selection = 0
    validate = True
    
    input1 = 0
    input2 = 0
    result = 0
    
    while int(selection) != 5:
        print("Select an operation")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        selection = input()
        
        validate = validateMenu(selection)
        
        if validate != True:
            print("Enter an integer between 1 and 5 \n")
            continue
        
        if int(selection) == 1:
            print("Enter first value")
            input1 = input()
            
            validate = validateFloat(input1)
        
            if validate != True:
                print("Enter a valid float value \n")
                continue
            
            print("Enter second value")
            input2 = input()
            
            validate = validateFloat(input2)
        
            if validate != True:
                print("Enter a valid float value \n")
                continue
            
            result = addValue(float(input1), float(input2))
            print("Result = " + str(result) + "\n")
            
        elif int(selection) == 2:
            print("Enter first value")
            input1 = input()
            
            validate = validateFloat(input1)
        
            if validate != True:
                print("Enter a valid float value \n")
                continue
            
            print("Enter second value")
            input2 = input()
            
            validate = validateFloat(input2)
        
            if validate != True:
                print("Enter a valid float value \n")
                continue
            
            result = subValue(float(input1), float(input2))
            print("Result = " + str(result) + "\n")
            
        elif int(selection) == 3:
            print("Enter first value")
            input1 = input()
            
            validate = validateFloat(input1)
        
            if validate != True:
                print("Enter a valid float value \n")
                continue
            
            print("Enter second value")
            input2 = input()
            
            validate = validateFloat(input2)
        
            if validate != True:
                print("Enter a valid float value \n")
                continue
            
            result = multiValue(float(input1), float(input2))
            print("Result = " + str(result) + "\n")
        
        elif int(selection) == 4:
            print("Enter first value")
            input1 = input()
            
            validate = validateFloat(input1)
        
            if validate != True:
                print("Enter a valid float value \n")
                continue
            
            print("Enter second value")
            input2 = input()
            
            validate = validateFloat(input2)
        
            if validate != True:
                print("Enter a valid float value \n")
                continue
                
            if float(input2) == 0:
                print("Divide by zero error \n")
                continue
            
            result = divValue(float(input1), float(input2))
            print("Result = " + str(result) + "\n")
        
        elif int(selection) == 5:
            print("Exiting...")
            
        else:
            print("Please enter an integer between 1 and 5")

if __name__ == '__main__':
    main()