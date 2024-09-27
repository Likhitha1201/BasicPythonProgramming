""" 

    @Author: Likhitha S
    @Date: 27-09-2024 14:15
    @Last Modified by: Likhitha S
    @Last Modified time: 27-09-2024 14:15
    @Title: Write a Python program to remove an item from a set if it is present in the set.
    
"""

   
def main():
    """
        
        Description:
            This function is used to delete an ele from a set.
        Parameters:
           set1  is a container which holds the data init .
        Return:
            It prints the elements present in a set.
                    
    """

    set1={12,23,45,'hii','hello'}
    print("Before Deletion: ",set1)
    num=23
    if num in set1:
        set1.remove(num)
        print(num,' is deleted sucessfully!!!')
    else:
        print(num,' is not present???')
    print("After deletion: ",set1)
   
    
if __name__=="__main__":
    main()