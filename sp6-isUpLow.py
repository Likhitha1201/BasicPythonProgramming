""" 

    @Author: Likhitha S
    @Date: 30-09-2024 13:15
    @Last Modified by: Likhitha S
    @Last Modified time: 1-10-2024 13:15
    @Title:Write a Python script that takes input from the user and displays that input back in upper and lower cases.

"""

def is_convertion(s1):
    """
        
        Description:
            This function is used to convert given string to upper case and lower case.
        Parameter:
            up,low is container to store the uppercase and lowercase word. 
        Return:
           It returns the up and low of given string.
                    
    """
    
    up=s1.upper()
    low=s1.lower()
            
    return up,low       
    
   
def main():
  
  s1=input("Enter the word: ")
  u_str,l_str=is_convertion(s1)
  print(f"conversion of {s1} to uppercase look's like: {u_str} ")
  print(f"conversion of {s1} to lowercase look's like: {l_str} ")
   
if __name__=="__main__":
    main()