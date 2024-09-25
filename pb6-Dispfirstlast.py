""" 

    @Author: Likhitha S
    @Date: 23-09-2024 16:50
    @Last Modified by: Likhitha S
    @Last Modified time: 23-09-2024 16:50
    @Title: Write a Python program to display the first and last colors from a list.

"""

def main():
    """
        
        Description: 
            This function is used fetch first and last color from a list.
        Parameters:
          colours from the user .
        Return:
            It returns the first and last colour from the list. 
        
    """
    
    
    colours=input("Enter the colours separated by(,): ")
    #colours=['red','green','purple','black','white']--
    colour=colours.split(',')
    print("First color will be: ",colour[0].strip())
    print("Last color will be: ",colour[len(colour)-1].strip())
    
    
if __name__=="__main__":
    main()