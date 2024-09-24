
""" 

    @Author: Likhitha S
    @Date: 24-09-2024 9:50
    @Last Modified by: Likhitha S
    @Last Modified time: 24-09-2024 9:50
    @Title: Write a Python program to create a histogram from a given list of integers.

"""

import matplotlib.pyplot as plt

def create_histogram(data):
    """
        
        Description: 
            This method is used to draw an histogram with the help of matplotlib.
        Parameters:
           data is taken as a parameter from calling method.
        Return:
            It returns the histogram based on user enterd points. 
        
    """
    
    
    plt.hist(data, bins=10, edgecolor='black')

    plt.title('Histogram of Given Integers')
    plt.xlabel('Value')
    plt.ylabel('Frequency')

    plt.show()
    
    
    
def main():
    """
        data is taken from user the user and pass to a called  function.
    """
    data=input('Enter elements separated by (,): ')
    data=data.split(',')
    create_histogram(data)

if __name__=="__main__":
    main()
