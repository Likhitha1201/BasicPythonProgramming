""" 

    @Author: Likhitha S
    @Date: 26-09-2024 15:40
    @Last Modified by: Likhitha S
    @Last Modified time: 26-09-2024 15:40
    @Title: Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
    
"""


def main():
    """
        
        Description: 
            This function is used to display the data between mentioned key based.
        Parameters:
            dist is an parameter given from calling function 
        Return:
            It prints the key between from dictionary. 
    
    """
    
    dic= {1:'q',2:'d',3:'rt',4:'ss',5:'xs',6:'er',7:'sd'}
    num=5
    for index,value in dic.items():
        if (index<=num):
            print(index, value)

if __name__=="__main__":
    main()