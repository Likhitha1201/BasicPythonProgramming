""" 

    @Author: Likhitha S
    @Date: 30-09-2024 10:10
    @Last Modified by: Likhitha S
    @Last Modified time: 1-10-2024 10:10
    @Title:Write a Python program to check whether an element exists within a tuple.
    
"""


def search_ele(tup,ele):
    """
        
        Description:
            This function is used to check an element is exist or not.
        Parameter:
            tup is container which is used to store the tuple type of data.
        Return:
           It print's weather the element exists or not.
                    
    """ 
    
    
    for i in tup:
        if i==ele:
            return True
    return False


def main():
  
    tup=(12,29,34,75,56,89,56,45)
    Ele= 13
    pos = search_ele(tup,Ele)
    
    if(pos):
        print(f"{Ele} is exists in a tuple")
    else:
         print(f"{Ele} is not exists in a tuple")
         
         
if __name__=="__main__":
    main()