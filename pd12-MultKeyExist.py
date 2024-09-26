""" 

    @Author: Likhitha S
    @Date: 26-09-2024 15:45
    @Last Modified by: Likhitha S
    @Last Modified time: 26-09-2024 15:45
    @Title: Write a Python program to check multiple keys exists in a dictionary.
    
"""


def check_keys_exist(dict, keys):
    """
        
        Description: 
            This function is used to check the multiple key exist or not.
        Parameters:
            dict is an parameter given from calling function 
        Return:
            It prints the all the keys are present or not. 
    
    """
    
    return all(key in dict for key in keys)


def main():
    """
        Here, i
    """
    
    sample_dict = {
        'name': 'Alice',
        'age': 30,
        'city': 'New York',
        'occupation': 'Engineer'
    }

    # List of keys to check
    keys_to_check = ['name', 'age', 'occupation']

    # Check if the keys exist in the dictionary
    if check_keys_exist(sample_dict, keys_to_check):
        print("All keys exist in the dictionary.")
    else:
        print("Not all keys exist in the dictionary.")


if __name__=="__main__":
    main()