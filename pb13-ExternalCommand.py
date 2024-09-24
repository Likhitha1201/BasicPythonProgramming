""" 

    @Author: Likhitha S
    @Date: 24-09-2024 17:30
    @Last Modified by: Likhitha S
    @Last Modified time: 24-09-2024 17:30
    @Title: Write a python program to call an external command in Python.

"""


import os

def fun(ex_comm):
    """
        
        Description: 
            here, in this we are going to use user entered commands as an input and describe the data accordingly .
        Parameters:
          ex_comm is an parameter given from calling function, It will accept user enterd command to display accordingly.
        Return:
            It prints the output according to that ex_comm . 
        
    """
    #command=ex_comm   
    #result=os.system(command)
    #print(f"Command executed with the code:{result}")
    
    print(f"Command that is exected :{ex_comm} the result of this will be: ",os.system(ex_comm))

def main():
    """
      
    ex_comm is used to take an input from the user and to perform task accordingly.
       
    """
  
    ex_comm= input("Enter the external command: ")  
    
    fun(ex_comm)
    
    
if __name__=="__main__":
    main()