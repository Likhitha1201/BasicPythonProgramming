""" 

    @Author: Likhitha S
    @Date: 24-09-2024 10:10
    @Last Modified by: Likhitha S
    @Last Modified time: 24-09-2024 10:10
    @Title:Write a Python program to print the documents (syntax, description etc.) of Python built-in
    function(s).

"""

def fun():
    """
        
        Description: 
            here, going to convert the List to String type .
        Parameters:
          Listt is used to take an input from the user.
        Return:
            It prints the converted string as an output . 
        
    """
    
    Listt=[input("Enter the elements into a list separated by commas(,):")]
    print(Listt)
    strdata=','.join(Listt)
    print(strdata)

if __name__=="__main__":
    fun()
