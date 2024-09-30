""" 

    @Author: Likhitha S
    @Date: 30-09-2024 17:35
    @Last Modified by: Likhitha S
    @Last Modified time: 30-09-2024 17:35
    @Title: Write a Python program to split a list based on first character of word.
     
"""

def isSplitWord(lt):
    
    """
        
        Description:
            This function is used split the given list based on the words.
        Parameter:
           res is a container which is used to hold the data init .
        Return:
           It print's the list which are splited  based on alphebetical order.
                    
    """
    
    res={}  # dictionary
    
    for i in lt:
        first=i[0].lower()
            
        if i not in res:
            res[first]=[]
            
        res[first].append(i)
        
    return res
    
   
def main():
    """
        lt1 is a container which is holding a data init .
    """
    
    lt1 = ['Apple', 'Banana', 'avocado', 'blueberry', 'cherry', 'date', 'elderberry', 'fig', 'grape']

    
    split_words=isSplitWord(lt1)
    print(split_words) 
    
if __name__=="__main__":
    main()