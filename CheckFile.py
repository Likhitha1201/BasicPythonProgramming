""" 

    @Author: Likhitha S
    @Date: 24-09-2024 12:10
    @Last Modified by: Likhitha S
    @Last Modified time: 24-09-2024 12:10
    @Title: Write a Python program to check whether a file exists.

"""

   
from pathlib import Path   
    
def f_pathexists(f_path):
    """
        
        Description: 
            here, going to in search of path of a file that exist .
        Parameters:
            f_path is an parameter, it accepts the path from calling function.
        Return:
            It returns the path if exist if not present it gives relevent message . 
        
    """    
    
    return Path(f_path).is_file()
    
    
def main():
    """
    file_path is an input from the user search the file
    """
    
    file_path = input("Enter the path of the file: ").strip()
        
    if  f_pathexists(file_path):
        print(f"The file'{file_path}' exists")
    else:
        print(f"The file'{file_path}' does not exists")
        
        
        
if __name__=="__main__":
        main()