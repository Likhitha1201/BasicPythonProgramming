""" 

    @Author: Likhitha S
    @Date: 26-09-2024 11:50
    @Last Modified by: Likhitha S
    @Last Modified time: 26-09-2024 11:50
    @Title: Write a Python program to reverse the order of the items in the array.

"""


import pandas 

def main():
    """
        
        Description: 
            This function is used iterate the array in reverse order using for loop.
        Parameters:
          arr is an input of array type 
        Return:
            It prints the individual element from the array. 
    
    """
    
    
    arr=pandas.array([12,34,56,45,78,89,34,78,70,34])
    ele=12
    count=0
    for i in arr:
        if ele==i:
            count+=1
            
    print(ele," is occured ",count," times.")
    
if __name__=="__main__":
    main()            
