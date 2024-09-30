""" 

    @Author: Likhitha S
    @Date: 30-09-2024 17:00
    @Last Modified by: Likhitha S
    @Last Modified time: 30-09-2024 17:00
    @Title: Write a Python program to find common items from two lists.
    
"""

def is_common(lt1,lt2):
    
    """
        
        Description:
            This function is used the to print common elements from the list.
        Parameter:
            com is a container which is used to hold the common data init .
        Return:
           It print's com.
                    
    """
    
    com=[]
    for i in lt1:
        if i in lt2:
            com.append(i)
    print(com)
    
def main():
    """
        lt1 and lt2 is a container which is holding a data init .
    """
    
    lt1=[23,39,46,17]
    lt2=[16,92,23,49]
    
    is_common(lt1,lt2)
        
    
if __name__=="__main__":
    main()