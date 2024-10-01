""" 

    @Author: Likhitha S
    @Date: 30-09-2024 10:35
    @Last Modified by: Likhitha S
    @Last Modified time: 1-10-2024 10:35
    @Title:Write a Python program to slice a tuple.
    
"""

def main():
    
    """
        
        Description:
            This function is used to slice an elements from tuple.
            slice operator-> it acts as substr. 
        Parameter:
            tup is container which is used to store the tuple type of data.
        Return:
           It print's the elements specified between.
                    
    """
  
    tup=(12,29,"rachuu",75,56,"menni",56,45,"chummi") 
    print("tup: ",tup)
    print("Elements between 3-6 are: ",tup[3:6]) # (:) -> is a symbol of slice operator
    
if __name__=="__main__":
    main()