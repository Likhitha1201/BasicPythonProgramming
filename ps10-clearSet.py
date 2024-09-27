""" 

    @Author: Likhitha S
    @Date: 27-09-2024 14:50
    @Last Modified by: Likhitha S
    @Last Modified time: 27-09-2024 14:50
    @Title: Write a Python program to clear a set.
    
"""

   
def main():
    """
        
        Description:
            This function is used to clear a set.
        Parameters:
           set1 is a container which holds the data init .
        Return:
            It clear the set and it display None .
                    
    """
    
    set1={12,34,68,79,56}
    print("Before clearing set: ",set1)
    emp_set=set1.clear()
    print("After clearing a set1 it look's like: ", emp_set)
    
if __name__=="__main__":
    main()
