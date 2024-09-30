""" 

    @Author: Likhitha S
    @Date: 30-09-2024 15:40
    @Last Modified by: Likhitha S
    @Last Modified time: 30-09-2024 15:40
    @Title: Write a Python program to append a list to the second list.
    
"""

   
def main(): 
    """
        
        Description:
            This function is used append the second list to first one.
        Parameters:
           lt1 and lt2 is a container which is holding a data init .
        Return:
           It print's overall second list  .
                    
    """
    
    lt1=[12,23,34,54,45]
    lt2=[12,34,78,56]
    
    lt2.append(lt1)
    print(lt2)
    
if __name__=="__main__":
    main()