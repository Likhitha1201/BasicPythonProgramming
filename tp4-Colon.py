""" 

    @Author: Likhitha S
    @Date: 30-09-2024 9:45
    @Last Modified by: Likhitha S
    @Last Modified time: 1-10-2024 9:45
    @Title:Write a Python program to create the colon of a tuple.
    
"""

def main():
    
    """
        
        Description:
            This function is used to create the colon of a tuple.
            colon-> it can created using slice operator. 
        Parameter:
            tup is container which is used to store the tuple type of data.
        Return:
           It print's the elements.
                    
    """
  
    tup=(12,29,34,75,56,89,56,45) 
    print("tup: ",tup)
    print("Elements between 3-6 are: ",tup[3:7]) # (:) -> is a symbol of slice operator
    
if __name__=="__main__":
    main()