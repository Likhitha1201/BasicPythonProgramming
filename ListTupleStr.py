""" 

    @Author: Likhitha S
    @Date: 23-09-2024 16:50
    @Last Modified by: Likhitha S
    @Last Modified time: 23-09-2024 16:50
    @Title: Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

"""

def main():
    """
        
        Description: 
            This function is used to cover to list and tuple a given string.
        Parameters:
          Taking f_name and l_name from the user.
        Return:
            It returns the reversed string. 
        
    """
    
    numbers = input("Enter the number separated by cammas:")
    print(numbers)
    li = numbers.split(',')
    li=[int(num.strip()) for num in li]
    tu = tuple(li)
    
    print("List: ",li)
    print("Tuple: ",tu)

if __name__=="__main__":
    main()


