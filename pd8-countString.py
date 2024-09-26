""" 

    @Author: Likhitha S
    @Date: 26-09-2024 16:55
    @Last Modified by: Likhitha S
    @Last Modified time: 26-09-2024 16:55
    @Title: 8. Write a Python program to create a dictionary from a string.
    Note: Track the count of the letters from the string.
    Sample string : 'w3resource'
    Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
    
"""


def count_letters(sample):
    """
        
        Description: 
            This function is used to count the charecters from a string.
        Parameters:
            sample in which it holds the string type .
        Return:
            It prints the count of a charecter. 
    
    """
    
    letter_count={}

    for char in sample:
        if char in letter_count:
            letter_count[char]+=1
        else:
            letter_count[char]=1
    return letter_count


def main():
    sample='w3resource'
    
    print(count_letters(sample)) 
    
    
if __name__=="__main__":
    main()        