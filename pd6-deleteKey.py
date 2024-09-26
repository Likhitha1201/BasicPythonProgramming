""" 

    @Author: Likhitha S
    @Date: 26-09-2024 16:00
    @Last Modified by: Likhitha S
    @Last Modified time: 26-09-2024 16:00
    @Title: Write a Python program to remove a key from a dictionary.
    
"""


def main():
    """
        
        Description: 
            This function is used to remove a key from the dictionary.
        Parameters:
            dist is an parameter given from calling function 
        Return:
            It prints the new dictionary. 
    
    """
    
    dic= {1:'q',2:'d',3:'rt',4:'ss',5:'xs',6:'er',7:'sd'}
    num=5
    del dic[5]
    print(dic)
    
if __name__=="__main__":
    main()