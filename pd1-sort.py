""" 

    @Author: Likhitha S
    @Date: 26-09-2024 14:30
    @Last Modified by: Likhitha S
    @Last Modified time: 26-09-2024 14:30
    @Title: Write a Python script to sort (ascending and descending) a dictionary by value.
"""


def asc_sort(dec):
    """
        
        Description: 
            This function is used to sort the dictionary in ascending order.
        Parameters:
            dec is an parameter given from calling function 
        Return:
            It prints the sorted dictionary. 
    
    """
    
    sort=dict(sorted(dec.items(), key=lambda x:x))
    return sort
    
def dec_sort(dec):
    """
        
        Description: 
            This function is used to sort the dictionary in descending order.
        Parameters:
            dec is an parameter given from calling function 
        Return:
            It prints the sorted dictionary. 
    
    """
    
    sort= dict(sorted(dec.items(),key=lambda x:x , reverse=True))
    return sort

def main():
    """
    Here, dic is an reference to hold the data of type dictionary.
    
    """
    
    dic= {5:'q',2:'d',4:'rt',3:'ss',1:'xs'}
    
    a_sort = asc_sort(dic)
    print("sorted in ascending order:",a_sort)
    
    d_sort = dec_sort(dic)
    print("sorted in descending order:",d_sort)
    
    print(asc_sort)
if __name__=="__main__":
    main()