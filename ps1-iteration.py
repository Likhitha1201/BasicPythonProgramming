""" 

    @Author: Likhitha S
    @Date: 27-09-2024 14:15
    @Last Modified by: Likhitha S
    @Last Modified time: 27-09-2024 14:15
    @Title: Write a Python program to iterate a set.
    
"""

   
def main():
    """
        
        Description:
            This function is used to create a set.
        Parameters:
           set1  is a container which holds the data init .
        Return:
            It prints the elements one by one from a set.
                    
    """

    set1={12,23,45,'hii','hello'}
    print(set1)
    
    for i in set1:
        print(i)
    
if __name__=="__main__":
    main()