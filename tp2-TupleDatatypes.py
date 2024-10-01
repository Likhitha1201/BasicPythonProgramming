""" 

    @Author: Likhitha S
    @Date: 30-09-2024 9:20
    @Last Modified by: Likhitha S
    @Last Modified time: 1-10-2024 9:20
    @Title:Write a Python program to create a tuple.

"""

def main():
    
    """
        
        Description:
            This function is used to create a tuple of heterogeneous type.
        Parameter:
            tup is container which is used to store the tuple type of data.
        Return:
           It print's the elements.
                    
    """
  
    tup=() # Empty tuple is created
    tup=tup+(100,200,)
    tup=tup+("reeya",)
    tup=tup+(300,400,500,) # inserting values to  an empty tuple
    tup=tup+("chummi",600,700)
    print(tup)
    
if __name__=="__main__":
    main()