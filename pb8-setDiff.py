""" 

    @Author: Likhitha S
    @Date: 27-09-2024 14:50
    @Last Modified by: Likhitha S
    @Last Modified time: 27-09-2024 14:50
    @Title: Write a Python program to create an intersection of sets.
    
"""

   
def main():
    """
        
        Description:
            This function is used to perform union of the two set.
        Parameters:
           set1 and set2 is a container which holds the data init .
        Return:
            It prints difference of set2 from set1 .
                    
    """
    
    set1={12,34,68,79,56}
    set2={12,23,45,34,65,10}
    diff_set=set1.difference(set2)
    print("difference of set2 from set1: ", diff_set)
    
if __name__=="__main__":
    main()
