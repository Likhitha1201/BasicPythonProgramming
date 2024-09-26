""" 

    @Author: Likhitha S
    @Date: 26-09-2024 17:40
    @Last Modified by: Likhitha S
    @Last Modified time: 26-09-2024 17:40
    @Title: Write a Python program to convert a list into a nested dictionary of keys.
    
"""

def list_to_nested_dict(lst, value=None):
    """
        
        Description:
            This function is used to convert in to nested dictionary of keys.
        Parameters:
            dic is an reference which acts as a container to hold the data.
        Return:
            It prints the nested dictionary.
                    
    """
    
    
    if not lst:
        return value
    
    # Start with the last element of the list
    return {lst[0]: list_to_nested_dict(lst[1:], value)}

# Sample list
sample_list = ['a', 'b', 'c', 'd']

# Convert the list into a nested dictionary
nested_dict = list_to_nested_dict(sample_list, '2344')

# Print the result
print(nested_dict)
    
  

