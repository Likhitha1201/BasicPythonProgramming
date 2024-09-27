""" 

    @Author: Likhitha S
    @Date: 27-09-2024 15:15
    @Last Modified by: Likhitha S
    @Last Modified time: 27-09-2024 15:15
    @Title: Write a Python program to sum all the items in a list..
    
"""

   
def main():
    """
        
        Description:
            This function is used to add all elements from a list.
        Parameters:
           lt is a container which holds the data init .
        Return:
            It print's sum of all element's .
                    
    """
    
    lt=[12,34,45,56,57]
    sum=0
    for i in lt:
        sum=sum+i
        
    print("sum of all the element's are: ",sum)
    
    
if __name__=="__main__":
    main()