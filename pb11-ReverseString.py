""" 

    @Author: Likhitha S
    @Date: 23-09-2024 13:30
    @Last Modified by: Likhitha S
    @Last Modified time: 23-09-2024 13:30
    @Title: Write a Program to calculate the minimum number
    of Notes as well as the Notes to be returned by the Vending Machine as a
    Change

"""


def main():
    """
        
        Description: 
            This function is used to reverse a given string.
        Parameters:
          Taking f_name and l_name from the user.
        Return:
            It returns the reversed string. 
        
    """
    
    
    f_name=input('Enter the first name:')
    l_name=input('Enter the last name:')
    new_str=" "
    new_str1=" "

    for i in f_name:
        new_str=i+new_str
 

    for i in l_name:
        new_str1= i+ new_str1
   
    r_name= new_str1+new_str
    print("reversed string will be: ",r_name)

if __name__=="__main__":
    main()