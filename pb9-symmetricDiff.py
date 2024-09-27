""" 

    @Author: Likhitha S
    @Date: 27-09-2024 14:50
    @Last Modified by: Likhitha S
    @Last Modified time: 27-09-2024 14:50
    @Title: Write a Python program to create a symmetric difference.
    
"""

   
def main():
    """
        
        Description:
            This function is used to perform symmetric difference of the two set.
        Parameters:
           set1 and set2 is a container which holds the data init .
        Return:
            It prints symmetric difference of set2 from set1 .
                    
    """
    
    set1={12,34,68,79,56}
    set2={12,23,45,34,65,10}
    symm_diff=set1.symmetric_difference(set2)
    print("symmetric_difference of set2 from set1: ", symm_diff)
    
if __name__=="__main__":
    main()
