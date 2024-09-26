""" 

    @Author: Likhitha S
    @Date: 26-09-2024 11:40
    @Last Modified by: Likhitha S
    @Last Modified time: 26-09-2024 11:40
    @Title: Write a Python program to create an array of 5 integers and display the array items. 
    Access individual element through indexes.

"""


import numpy as np

def main():
    """
        
        Description: 
            This function is used iterate the array in reverse order using for loop.
        Parameters:
          arr is an input of array type 
        Return:
            It prints the individual element from the array. 
        
    """
    
    arr=np.array([12,23,3,44,556,67,78,89])
    
    for i in range(len(arr)-1,-1,-1):
        print(arr[i])
        
if __name__=="__main__":
    main()