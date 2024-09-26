""" 

    @Author: Likhitha S
    @Date: 26-09-2024 14:40
    @Last Modified by: Likhitha S
    @Last Modified time: 26-09-2024 14:40
    @Title: Write a Python script to concatenate following dictionaries to create a new one.
    
"""


def conc_dics(dict1, dict2, dict3):
    """
        
        Description: 
            This function is used to concatenate different dictionaries into single dictionary.
        Parameters:
            dist1, dict2, dict3 is an parameter given from calling function 
        Return:
            It prints the new dictionary. 
    
    """
    
    dict=dict1.copy()
    dict.update(dict2)
    dict.update(dict3)
    return dict


def main():
    """
     Here, dict1, dict2, dict3 are the input of type dictionary.
    """
    dict1={1:'zx', 2:'xc'}
    dict2={3:'cv', 4:'vb'}
    dict3={5:'dr',6:'fg'}
    
    new_dict= conc_dics(dict1, dict2, dict3)
    print(new_dict)  
 

if __name__=="__main__":
    main()