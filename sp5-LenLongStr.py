""" 

    @Author: Likhitha S
    @Date: 30-09-2024 12:40
    @Last Modified by: Likhitha S
    @Last Modified time: 1-10-2024 12:40
    @Title:Write a Python function that takes a list of words and returns the length of the longest one.

"""

def is_longest(lt):
    """
        
        Description:
            This function is used to find longest length of a string in given list.
        Parameter:
            long is container of type of String, which is used to hold the word of highest length. 
        Return:
           It print's the string of long.
                    
    """
    
    long=''
    
    for i in lt:
        if len(i)>len(long):
            long=i
            
    return long       
    
   
def main():
  
   lt=['rachuu','menni','chitti','chummi','siddi','kenchuu']
   greatest=is_longest(lt)
   print(greatest)
   
if __name__=="__main__":
    main()