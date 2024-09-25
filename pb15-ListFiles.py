""" 

    @Author: Likhitha S
    @Date: 25-09-2024 18:40
    @Last Modified by: Likhitha S
    @Last Modified time: 25-09-2024 18:40
    @Title: Write a Python program to list all files in a directory in Python..

"""


from pathlib import Path

def main():
    """
        
        Description: 
            here, going to deal with the multiprocessing .
        Parameters:
          directory_path is used get the path and it ir directed to fetch the files presented init.
        Return:
            It prints all the files present in that path. 
        
    """
    
    # it is a {r} raw string that is used to avoid the escape issues
    directory_path = Path(r"C:\Users\Likhitha S\OneDrive\Desktop\BridgeLabzz\Python")

    # List all files in the directory
    files = [f for f in directory_path.iterdir() if f.is_file()]

    # Print the list of files
    print("Files in directory:")
    for file in files:
        print(file.name)

        
if __name__=="__main__":
    main()