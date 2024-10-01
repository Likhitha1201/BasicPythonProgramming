""" 

    @Author: Likhitha S
    @Date: 1-10-2024 15:32
    @Last Modified by: Likhitha S
    @Last Modified time: 1-10-2024 15:32
    @Title: write a program to count occurrences of a substring in a string
"""


import textwrap

def count_occurrences(s1, ch):
    """
        
        Description:
            This function is used to count the given charecter. how many time it is repeated.
        Parameter:
            s1 and ch are the parameter. 
        Return:
           It returns the how many time it is repeated.
                    
    """
    
   
    return s1.count(ch)

def main():
    s1="Rachuu is a good boy. Rachuu can do any thing. yes he is well behavied!!!!!"
    ch='good'
    
    stt=count_occurrences(s1, ch)
    
    print(ch,' appeared ',stt,' times')
    
if __name__=="__main__":
    main()
