""" 

    @Author: Likhitha S
    @Date: 30-09-2024 10:30
    @Last Modified by: Likhitha S
    @Last Modified time: 1-10-2024 10:30
    @Title:Write a Python program to remove an item from a tuple.
    
"""


def isremove(tup, ele) :
    """
        
        Description:
            This function is used to remove an item from a tuple.
        Parameter:
            tup is container which is used to store the tuple type of data.
        Return:
           It print's .
                    
    """ 
  
    ntt=()
    
    for i in tup:
        if i==ele:
            continue
        else:
            ntt=ntt+(i,)
    
    print(f"{tup} after deleting an element from it, looks like: {ntt}")
  
def main():
    tup=(12,23,45,67,89,97,75)
    ele=23
    isremove(tup,ele)    
    
if __name__=="__main__":
    main()