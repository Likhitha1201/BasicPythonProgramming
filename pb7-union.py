""" 

    @Author: Likhitha S
    @Date: 27-09-2024 14:40
    @Last Modified by: Likhitha S
    @Last Modified time: 27-09-2024 14:40
    @Title: Write a Python program to create an union of sets..
    
"""

   
def main():
    """
        
        Description:
            This function is used to perform union of the two set.
        Parameters:
           set1 and set2 is a container which holds the data init .
        Return:
            It prints all the elements from a set.
                    
    """
    
    set1={12,34,68,79,56}
    set2={12,23,45,34,65,10}
    uni_set=set1.union(set2)
    print("union of all the elements are: ", uni_set)
    
if __name__=="__main__":
    main()
