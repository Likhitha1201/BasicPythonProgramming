""" 

    @Author: Likhitha S
    @Date: 26-09-2024 18:10
    @Last Modified by: Likhitha S
    @Last Modified time: 26-09-2024 18:10
    @Title: Write a Python program to count number of items in a dictionary value that is a list.
    
"""

   
def count_items_in_lists(dict):
    """
        
        Description:
            This function is used to count the numbner of items present in a dictionary.
        Parameters:
            dict is an parameter called from a calling function .
        Return:
            It prints the number of items present in that dictionary.
                    
    """
        
    count = 0
    for value in dict.values():
        if isinstance(value, list):  # Check if the value is a list
            count += len(value)  # Add the length of the list to the count
    return count


def main():

    sample_dict = {
        'fruits': ['apple', 'banana', 'cherry'],
        'vegetables': ['carrot', 'broccoli'],
        'grains': ['rice', 'wheat', 'barley'],
        'Biscuts': ['marilight','Oreo','Unibic'],
        'dairy': 'milk',  # This value is not a list--> it is not considered
    }

    # Count the number of items in lists
    total_items = count_items_in_lists(sample_dict)

    # Print the result
    print(f"Total number of items in lists: {total_items}")


if __name__=="__main__":
    main()