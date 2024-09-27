""" 

    @Author: Likhitha S
    @Date: 27-09-2024 15:10
    @Last Modified by: Likhitha S
    @Last Modified time: 27-09-2024 15:10
    @Title: Write a Python program to find maximum and the minimum value in a set.
    
"""

   
def main():
    """
        
        Description:
            This function is used to find the maximum and minimum valu from a set.
        Parameters:
           set1 is a container which holds the data init .
        Return:
            It print's max and min value from a set .
                    
    """
    
    set1={12,34,68,79,56}
    max_val= max(set1)
    min_val= min(set1)
    
    print(f"from a given set: {set1} the maximum value willbe: {max_val} and minimum value will be: {min_val} ")
    
if __name__=="__main__":
    main()
