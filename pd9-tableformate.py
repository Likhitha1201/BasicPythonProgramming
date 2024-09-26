""" 

    @Author: Likhitha S
    @Date: 26-09-2024 17:10
    @Last Modified by: Likhitha S
    @Last Modified time: 26-09-2024 17:10
    @Title: Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
    
"""


from tabulate import tabulate

def main():
    """
        
        Description: 
            This function is used to display the data in tabulaer formate.
        Parameters:
            dic is an reference which acts as a container to hold the data. 
        Return:
            It prints the key between from dictionary. 
    
    """

    dic={'Name':'Rachuu', 'age':23, 'country':'India'}

    table=[(k,v) for k, v in dic.items()]

    print(tabulate(table, headers=["key","value"], tablefmt="pretty"))
    
    
if __name__=="__main__":
    main()