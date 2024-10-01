""" 

    @Author: Likhitha S
    @Date: 30-09-2024 13:40
    @Last Modified by: Likhitha S
    @Last Modified time: 1-10-2024 13:40
    @Title:Write a Python program to get the last part of a string before a specified character.

"""

def is_last(s1,char):
    """
        
        Description:
            This function is used to reverse the given string.
        Parameter:
            new_str is container to store the reversed data. 
        Return:
           It returns the reversed string.
                    
    """
    
    #split method implicitly splits in to two part likewise->[' https://www.w3resource.com', 'python-exercises']
    new_str=s1.rsplit(char,1)
    
    if len(new_str)>1:
        return new_str[0]
    
    return s1
    
   
def main():
  
  s1=input("Enter the string separated by '/': ")
  s2=" https://www.w3resource.com/python-exercises"
  n_str1=is_last(s1,'/')
  n_str2=is_last(s2,'/')
  print(n_str1)
  print(s2)
  print(n_str2)
  
   
if __name__=="__main__":
    main()