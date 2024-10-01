""" 

    @Author: Likhitha S
    @Date: 30-09-2024 10:10
    @Last Modified by: Likhitha S
    @Last Modified time: 1-10-2024 10:10
    @Title:Write a Python program to convert a list to a tuple.
    
"""


def main():
    """
        
        Description:
            This function is used to convert list to tuple.
        Parameter:
            tup is container which is used to store the tuple type of data.
        Return:
           It print's weather the element exists or not.
                    
    """ 
  
    lt=[12,23,45,67,89,97,75]
    tup=tuple(lt)
    print(f"{lt} after converting to tuple, it looks like: {tup}")
         
         
if __name__=="__main__":
    main()