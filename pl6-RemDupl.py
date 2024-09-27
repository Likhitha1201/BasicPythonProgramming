""" 

    @Author: Likhitha S
    @Date: 27-09-2024 16:30
    @Last Modified by: Likhitha S
    @Last Modified time: 27-09-2024 16:30
    @Title: Write a Python program to remove duplicates from a list.
    
"""

def remove_duplicates(lt):
    
    """
        
        Description:
            This function is used to remove duplicates from a list.
        Parameters:
           lt is a container which holds the data init .
        Return:
            It print's the element's from list .
                    
    """
   
    return list(set(lt))


   
def main():
   
    lt=[12,34,45,45,56,57]
    unique_ele=list(set(lt))
    remove_duplicates(lt)
    print("Unique element's are: ",unique_ele)
    
    
if __name__=="__main__":
    main()