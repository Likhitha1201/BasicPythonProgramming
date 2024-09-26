""" 

    @Author: Likhitha S
    @Date: 26-09-2024 14:40
    @Last Modified by: Likhitha S
    @Last Modified time: 26-09-2024 14:40
    @Title: Write a Python script to add a key to a dictionary.
    
"""


def add_ele(dec):
    """
        
        Description: 
            This function is used to add an element to dictionary.
        Parameters:
            dec is an parameter given from calling function 
        Return:
            It prints the new dictionary. 
    
    """
    
    dec[2]='keww'
    dec[6]='neww'
    return dec

def main():
    """
    Here, dic is an reference to hold the data of type dictionary.
    
    """
    
    dic= {1:'q',2:'d',3:'rt',4:'ss',5:'xs'}
    new_dict=add_ele(dic)
    print(new_dict)

if __name__=="__main__":
    main()