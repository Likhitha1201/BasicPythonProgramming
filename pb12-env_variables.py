""" 

    @Author: Likhitha S
    @Date: 24-09-2024 12:30
    @Last Modified by: Likhitha S
    @Last Modified time: 24-09-2024 12:30
    @Title: Write a python program to access environment variables.

"""

import os

def main():
    """
        
        Description: 
            Here, In this we are going to access the environmental variable .
        Parameters:
            variable_name is an parameter, it accepts the path from calling function.
        Return:
            It prints all collected data present in that variable specified . 
        
    """    
    
    variable_name = input("Enter the name of the environment variable you want to access (or press Enter to list all): ")
    
    if variable_name:
        value = os.getenv(variable_name)
        
        if value is not None:
            print(f"{variable_name}: {value}")
        else:
            print(f"The environment variable '{variable_name}' does not exist.")
    else:
        print("\nAll Environment Variables:")
        for key, value in os.environ.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    main()