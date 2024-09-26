""" 

    @Author: Likhitha S
    @Date: 26-09-2024 14:40
    @Last Modified by: Likhitha S
    @Last Modified time: 26-09-2024 14:40
    @Title: Write a Python program to iterate over dictionaries using for loops.
    
"""


def looping(dict):
    """
        
        Description: 
            This function is used to iterate using looping statement.
        Parameters:
            dist is an parameter given from calling function 
        Return:
            It prints the new dictionary. 
    
    """
    print('---Using ForLoop---')
    for index,value in dict.items():
        print(index,value)
    
    print('---Using WhileLoop---')
    keys= list(dict.keys())
    
    i=0
    while i<len(dict):
        key=keys[i]
        print(key ,' ', dict[key])
        i+=1
        
def main():
    """
        Here, the function that is used will be looping statements.
    """
    
    dict={1:'liki', 2:'rachuu', 3:'menni', 4:'chitti'}
    
    looping(dict)
    
if __name__=="__main__":
    main()