""" 

    @Author: Likhitha S
    @Date: 30-09-2024 13:40
    @Last Modified by: Likhitha S
    @Last Modified time: 1-10-2024 13:40
    @Title:Write a Python program to reverse a string.

"""

def is_reverse(s1):
    """
        
        Description:
            This function is used to reverse the given string.
        Parameter:
            new_str is container to store the reversed data. 
        Return:
           It returns the reversed string.
                    
    """
    
    
    new_str=''
    
    for i in range(len(s1)-1,-1,-1):
        new_str+=s1[i]
        
    return new_str 
    
   
def main():
  
  s1=input("Enter the string: ")
  n_str=is_reverse(s1)
  print(n_str)
  
   
if __name__=="__main__":
    main()