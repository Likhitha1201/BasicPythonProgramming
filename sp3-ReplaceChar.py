""" 

    @Author: Likhitha S
    @Date: 30-09-2024 11:35
    @Last Modified by: Likhitha S
    @Last Modified time: 1-10-2024 11:35
    @Title:Write a Python program to get a string from a given string where all occurrences of its
    first char have been changed to '$', except the first char itself.
    Sample String : 'restart'
    Expected Result : 'resta$t'

"""

def is_Replace(s1):
    """
        
        Description:
            This function is used to find the frequency of given string.
        Parameter:
            freq is container which is used to store the frequency
        Return:
           It print's the frequency of the letters from a given string.
                    
    """
    
    s2=''
    ss={}
    
    for i in s1:
        if i in ss:
            ss[i]+=1
            s2+='$'
        else:
            ss[i]=1
            s2+=i 
               
    # print(s2)
    # print(ss)    
    return s2

   
def main():
  
    s1="restart"
    res=is_Replace(s1)
    
    print(f"Expected result will be: {res}")
    
    
if __name__=="__main__":
    main()