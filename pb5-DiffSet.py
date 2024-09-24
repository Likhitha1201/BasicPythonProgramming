""" 

    @Author: Likhitha S
    @Date: 24-09-2024 11:10
    @Last Modified by: Likhitha S
    @Last Modified time: 24-09-2024 11:10
    @Title: Write a Python program to print out a set containing all the colors from color_list_1 which
    are not present in color_list_2.

"""

def fun():
    """
        
        Description: 
            here, going to find the difference from a set to b set .
        Parameters:
            set1 and set2 are used to take an input from the user.
        Return:
            It prints the difference between a and b . 
        
    """
    
    set1 = input("Enter the colours: ")
    set2 = input("Enter the colours: ")
    
    set1 = set1.split()
    set2 = set2.split()
   
    set1=set(set1)
    set2=set(set2)
    
    print("Colors in set1 but not in set2:", set1 - set2)



if __name__=="__main__":
    fun()
