""" 

    @Author: Likhitha S
    @Date: 26-09-2024 14:40
    @Last Modified by: Likhitha S
    @Last Modified time: 26-09-2024 14:40
    @Title: Write a Python script to concatenate following dictionaries to create a new one.
    
"""


def looping(dict):
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
        
        Description: 
            This function is used to concatenate different dictionaries into single dictionary.
        Parameters:
            dist1, dict2, dict3 is an parameter given from calling function 
        Return:
            It prints the new dictionary. 
    
    """
    
    dict={1:'liki', 2:'rachuu', 3:'menni', 4:'chitti'}
    
    looping(dict)
    
if __name__=="__main__":
    main()