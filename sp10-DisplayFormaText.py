""" 

    @Author: Likhitha S
    @Date: 1-10-2024 15:10
    @Last Modified by: Likhitha S
    @Last Modified time: 1-10-2024 15:10
    @Title: write a python program to display formatted text (width=50) as output

"""


import textwrap

def format_text(text, width=50):
    """
        
        Description:
            This function is used to display formatted text according to a given size.
        Parameter:
            new_str, new_str1 is container to store the sorted data. 
        Return:
           It returns the sorted string.
                    
    """
    #The fill() method in Python's textwrap module takes a long string of text and breaks it into multiple lines, ensuring that each line does not exceed a specified width.
    wrapped_text = textwrap.fill(text, width=width)
    print(wrapped_text)

def main():
    sample_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""


    format_text(sample_text, 200)
    
if __name__=="__main__":
    main()
