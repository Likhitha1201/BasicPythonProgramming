""" 

    @Author: Likhitha S
    @Date: 1-10-2024 15:32
    @Last Modified by: Likhitha S
    @Last Modified time: 1-10-2024 15:32
    @Title: write a python program to lowercase first n characters in a string.
    
"""


def to_lower(s1, n):
    """
        
        Description:
            This function is used to convert the string to lowercase till specified length.
        Parameter:
            n_str is used to store the new data. 
        Return:
           It returns new string based on required result.
                    
    """
    
    
    n_str=''
    
    for i in range(len(s1)):
        if i<n:
            n_str+=s1[i].lower()
        else:
            n_str+=s1[i]
    
   
    return n_str

def main():
    s1=input("Enter the string: ")
    n=int(input("Enter the number till where i need to lower the charecters: "))
    
    stt=to_lower(s1, n)
    
    print(stt)
    
if __name__=="__main__":
    main()
