""" 

    @Author: Likhitha S
    @Date: 30-09-2024 11:35
    @Last Modified by: Likhitha S
    @Last Modified time: 1-10-2024 11:35
    @Title:Write a Python program to count the number of characters (character frequency) in a string.
    Sample String : google.com
    Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
    
"""

def is_frequency(s1):
    """
        
        Description:
            This function is used to find the frequency of given string.
        Parameter:
            freq is container which is used to store the frequency
        Return:
           It print's the frequency of the letters from a given string.
                    
    """
    
    freq={}
    
    for i in s1:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
            
    return freq
   
def main():
  
    s1="google.com"
    res=is_frequency(s1)
    
    expected=['o','g','.','e','l','m','c']
    result={i:res[i] for i in expected if i in res}
    
    print(f"Expected result will be: {result}")
    
    
if __name__=="__main__":
    main()