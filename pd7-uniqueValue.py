""" 

    @Author: Likhitha S
    @Date: 26-09-2024 15:40
    @Last Modified by: Likhitha S
    @Last Modified time: 26-09-2024 15:40
    @Title: Write a Python program to print all unique values in a dictionary.
    Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
    {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
    Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
    
"""

def get_unique(dic):
    """
        
        Description: 
            This function is used to display the unique values from dictionaries.
        Parameters:
            dist is an reference which is storing dictionary type of data
        Return:
            It prints the unique value from dictionary. 
    
    """
    
    unique_values = set()
    

    for value in dic.values():
        unique_values.add(value)
        
    return unique_values


def main():
    """
        Here, dic is a container which holds the data of a dictionaries.
    """
 
    dic= {1:'q',2:'d',3:'rt',4:'ss',5:'xs',6:'rt',7:'dd'}
    
    unique=get_unique(dic)
    print("unique values are: ",unique)
    
if __name__=="__main__":
    main() 

