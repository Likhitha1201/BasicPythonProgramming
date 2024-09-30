""" 

    @Author: Likhitha S
    @Date: 30-09-2024 18:00
    @Last Modified by: Likhitha S
    @Last Modified time: 30-09-2024 18:00
    @Title: Write a Python program to remove duplicates from a list of lists.
    Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    New List : [[10, 20], [30, 56, 25], [33], [40]]

"""

def isRemove(lt):
    
    """
        
        Description:
            This function is used remove the duplicates from list of list.
        Parameter:
           res is a container which is used to hold the non-duplicate data init .
        Return:
           It print's the res of non-duplicate elements.
                    
    """
    
    unq = set()
    new_lt = []
    
    for i in lt:
        tuple_lt=tuple(i)
        
        if tuple_lt not in unq:
            unq.add(tuple_lt)
            new_lt.append(list(tuple_lt))
            
    return new_lt
            
def main():
    """
        lt1 is a container which is holding a data init .
    """
    
    lt=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    res=isRemove(lt)
    print(res)
    
if __name__=="__main__":
    main()