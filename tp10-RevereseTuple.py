""" 

    @Author: Likhitha S
    @Date: 30-09-2024 9:45
    @Last Modified by: Likhitha S
    @Last Modified time: 1-10-2024 9:45
    @Title:Write a Python program to reverse a tuple.
    
"""

def is_reverse(tup):
    """
        
        Description:
            This function is used to reverse the tuple.
        Parameter:
            ntt is container which is used to store the tuple type of data.
        Return:
           It print's the new tuple which contains the reversed elements.
                    
    """
    
    
    ntt=()
    
    for i in range(len(tup)-1,-1,-1):
        if tup[i] not in ntt:
            ntt=ntt+(tup[i],)
        
    print(f"{tup} after reversing it looks like..{ntt}")
    
    

def main():
  
    tup=(12,29,34,75,89,56,45) 
    is_reverse(tup)
    
    
    
if __name__=="__main__":
    main()