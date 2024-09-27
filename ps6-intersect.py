""" 

    @Author: Likhitha S
    @Date: 27-09-2024 14:00
    @Last Modified by: Likhitha S
    @Last Modified time: 27-09-2024 14:00
    @Title: Write a Python program to create an intersection of sets..
    
"""

   
def main():
    """
        
        Description:
            This function is used to perform intersection of the two set.
        Parameters:
           set1 and set2 is a container which holds the data init .
        Return:
            It prints the set.
                    
    """
    
    set1={12,34,68,79,56}
    set2={12,23,45,34,65,10}
    inter_set=set1.intersection(set2)
    print("common elements present are: ", inter_set)
    
if __name__=="__main__":
    main()
