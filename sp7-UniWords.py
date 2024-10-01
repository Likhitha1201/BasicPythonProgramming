""" 

    @Author: Likhitha S
    @Date: 30-09-2024 13:40
    @Last Modified by: Likhitha S
    @Last Modified time: 1-10-2024 13:40
    @Title:Write a Python program that accepts a comma separated sequence of words as input
    and prints the unique words in sorted form (alphanumerically).
    Sample Words : red, white, black, red, green, black
    Expected Result : black, green, red, white,red

"""

def alphanum(s1):
    """
        
        Description:
            This function is used to sort given string.
        Parameter:
            new_str, new_str1 is container to store the sorted data. 
        Return:
           It returns the sorted string.
                    
    """
    
    new_str=s1.split(',')
    new_str.sort() 
    new_str1=" ".join(new_str)           
    return new_str1  
    
   
def main():
  
  s1=input("Enter the word's separated with commas: ")
  n_str=alphanum(s1)
  print(n_str)
  
   
if __name__=="__main__":
    main()