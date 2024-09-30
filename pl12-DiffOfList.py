""" 

    @Author: Likhitha S
    @Date: 30-09-2024 15:40
    @Last Modified by: Likhitha S
    @Last Modified time: 30-09-2024 15:40
    @Title: Write a Python program to get the difference between the two lists.
    
"""

def difference(lt1,lt2):
    
    """
        
        Description:
            This function is used takes list as an input and perform the difference of it .
        Parameters:
           res is a container which is used to hold the data init .
        Return:
           It print's difference that stored in res  .
                    
    """
    
    res=[]
    for i in lt1:
        if i not in lt2:
            res.append(i)
        
    print(res)
   
def main():
    """
        lt1 and lt2 is a container which is holding a data init .
    """
    
    lt1=[12,23,34,54,45]
    lt2=[12,34,78,56]
    
    difference(lt1,lt2)
    
if __name__=="__main__":
    main()