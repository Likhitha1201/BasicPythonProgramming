""" 

    @Author: Likhitha S
    @Date: 23-09-2024 17:00
    @Last Modified by: Likhitha S
    @Last Modified time: 23-09-2024 17:00
    @Title:Write a Python program to print the documents (syntax, description etc.) of Python built-in
function(s).

"""


def main():
    """
        
        Description: 
            here, going to deal with the function type like..abs, .
        Parameters:
          fun_name is used to an input from the user of type function.
        Return:
            It prints the output according to that fun_type . 
        
    """

fun_name= input("Enter the function name: ")
num=int(input("Enter the negative number:"))
print(f"Documentation of the {fun_name}() will be:")
answer=eval(fun_name)(num) # eval = This allows you to call the function based on its name as a string. 
print(f"{fun_name}({num}) willbe:",answer)


if __name__=="__main__":
    main()
