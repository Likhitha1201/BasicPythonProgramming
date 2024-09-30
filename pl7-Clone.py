""" 

    @Author: Likhitha S
    @Date: 30-09-2024 13:30
    @Last Modified by: Likhitha S
    @Last Modified time: 30-09-2024 13:30
    @Title: Write a Python program to clone or copy a list.
    
"""
def clone(lt):
    
    """
        
        Description:
            This function is used to copy a list from oldv to new list.
        Parameters:
           lt is a container which holds the data of list init .
        Return:
            It print's the copied new list .
                    
    """
   
    lt11=lt.copy()
    return lt11

   
def main():
   
    lt=[12,34,45,45,56,57]
    lt1=lt
    print("directly done using reference: ",lt1)
    n_lt=clone(lt)
    print("done using copy method : ",n_lt)
    
    
if __name__=="__main__":
    main()