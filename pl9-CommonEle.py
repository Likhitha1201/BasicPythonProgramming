""" 

    @Author: Likhitha S
    @Date: 30-09-2024 14:10
    @Last Modified by: Likhitha S
    @Last Modified time: 30-09-2024 14:10
    @Title: write a python program that takes two list and return true if they have atleast a common member.
    
"""

def common(lt1,lt2):
    
    """
        
        Description:
            This function is used takes two list and return true if one of the elements is matching from those list.
        Parameters:
           lt1 and lt2 is a container which holds the data init .
        Return:
            It print's true or false if common element is present .
                    
    """
    for i in lt1:
        for j in lt2:
            if i==j:
                return True
    return False


   
def main():
   
    lt1=[12,34,45,45,56,57]
    lt2=[23,46,67,57,98]
    
    res=common(lt1,lt2)
    print(res)
    
if __name__=="__main__":
    main()