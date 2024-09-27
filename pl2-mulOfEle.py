""" 

    @Author: Likhitha S
    @Date: 27-09-2024 15:20
    @Last Modified by: Likhitha S
    @Last Modified time: 27-09-2024 15:20
    @Title: Write a Python program to product of all the items in a list..
    
"""

   
def main():
    """
        
        Description:
            This function is used to multiply all elements from a list.
        Parameters:
           lt is a container which holds the data init .
        Return:
            It print's product of all element's .
                    
    """
    
    lt=[12,34,45,56,57]
    prod=1
    for i in lt:
        prod=prod*i
        
    print("product of all the element's are: ",prod)
    
    
if __name__=="__main__":
    main()