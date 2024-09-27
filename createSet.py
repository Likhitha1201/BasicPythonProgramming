""" 

    @Author: Likhitha S
    @Date: 27-09-2024 14:00
    @Last Modified by: Likhitha S
    @Last Modified time: 27-09-2024 14:00
    @Title: Write a Python program to create a set.
    
"""

   
def main():
    """
        
        Description:
            This function is used to create a set.
        Parameters:
           set1 and set2 is a container which holds the data init .
        Return:
            It prints the set.
                    
    """
    
    set1=set() # creating empty set
    set1.add(10)
    set1.add(20)
    set1.add(30)
    print(set1)
    
    set2={12,23,45}
    print(set2)
    
if __name__=="__main__":
    main()