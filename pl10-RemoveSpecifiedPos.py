""" 

    @Author: Likhitha S
    @Date: 30-09-2024 15:40
    @Last Modified by: Likhitha S
    @Last Modified time: 30-09-2024 15:40
    @Title: Write a Python program to print a specified list after removing the 0th, 4th and
    5th elements.
    Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    Expected Output : ['Green', 'White', 'Black']
    
"""

def remove(lt1,pos):
    
    """
        
        Description:
            This function is used takes list as an input and check the specified position and removes specific data present in that list.
        Parameters:
           lt is a container which is used to hold the data init .
        Return:
            It print's remaining elements present in that list .
                    
    """
    
    lt=[]
    for i in range(0,len(lt1)):
        if i not in pos:
            lt.append(lt1[i])
    return lt
   
def main():
    """
        lt1 is a container which is holding a data init .
    """
    lt1=['Red', 'Green','Pink','Yellow','black','White','Grey']
    pos=[0,4,5]
    res=remove(lt1,pos)
    print(res)
    
if __name__=="__main__":
    main()