""" 

    @Author: Likhitha S
    @Date: 26-09-2024 11:30
    @Last Modified by: Likhitha S
    @Last Modified time: 26-09-2024 11:30
    @Title: Write a Python program to create an array of 5 integers and display the array items. 
    Access individual element through indexes.

"""


import array

def main():
    """
        
        Description: 
            This function is used iterate the array using for loop.
        Parameters:
          arr ia an input of array type 
        Return:
            It prints the individual element from the array. 
        
    """
    
    
    arr = array.array('i',[12,25,78,90,67,54])
    print(f"the individual ele from {arr} are listed below: ")
    for i in arr:
        print(i)
        
if __name__=="__main__":
    main()