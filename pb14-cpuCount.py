""" 

    @Author: Likhitha S
    @Date: 25-09-2024 18:20
    @Last Modified by: Likhitha S
    @Last Modified time: 25-09-2024 18:20
    @Title:Write a Python program to find out the number of CPUs using.

"""


import multiprocessing

def main():
    """
        
        Description: 
            here, going to deal with the multiprocessing .
        Parameters:
          cpu_count it is container that is used the hold the count of the cpu.
        Return:
            It prints the number of cpu's were used . 
        
    """
    
    
    cpu_count=multiprocessing.cpu_count()

    print(f"therefore the number of cpu counting will be: {cpu_count}")
    
if __name__=="__main__":
    main()