""" 

    @Author: Likhitha S
    @Date: 26-09-2024 17:30
    @Last Modified by: Likhitha S
    @Last Modified time: 26-09-2024 17:30
    @Title: Write a Python program to count the values associated with key in a
    dictionary.
    Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':
    False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
    Expected result: Count of how many dictionaries have success as True
"""

def count_success(sample, key):
    """
        
        Description: 
            This function is used to display the data in tabulaer formate.
        Parameters:
            dic is an reference which acts as a container to hold the data. 
        Return:
            It prints the key between from dictionary. 
    
    """
    
    count=0
    for item in sample:
        if item.get(key)==True:
            count+=1
    return count


def main():
   Sample= [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
   
   success_count=count_success(Sample, 'success')
   print(f"Count of dictionaries with success as True: {success_count}")
            
    

if __name__=="__main__":
    main()