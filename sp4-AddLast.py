""" 

    @Author: Likhitha S
    @Date: 30-09-2024 12:40
    @Last Modified by: Likhitha S
    @Last Modified time: 1-10-2024 12:40
    @Title:Write a Python program to add 'ing' at the end of a given string (length should be at
    least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the

    given string is less than 3, leave it unchanged.
    Sample String : 'abc'
    Expected Result : 'abcing'
    Sample String : 'string'
    Expected Result : 'stringly'

"""

def is_additional(s1):
    """
        
        Description:
            This function is used to perform given operation on a string.
        Parameter:
            s2 is container which is used to store the newly added data along with the original String. 
        Return:
           It print's the newly created string.
                    
    """
    
    s2=''
    
    if s1[len(s1)-3] in 'ing':
        s2=s2+s1+'ly'
    elif len(s1)>=3:
        s2=s2+s1+'ing'
    elif len(s1)<3:
        s2=s1 

    return s2
   
def main():
  
    s1=input("Enter the string:")
    res=is_additional(s1)
    
    print(f"Expected result will be: {res}")
 
 
if __name__=="__main__":
    main()