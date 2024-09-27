""" 

    @Author: Likhitha S
    @Date: 27-09-2024 15:40
    @Last Modified by: Likhitha S
    @Last Modified time: 27-09-2024 15:40
    @Title: Write a Python program to get a list, sorted in increasing order by the last
    element in each tuple from a given list of non-empty tuples.
    Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
    
"""

   
def main():
    """
        
        Description:
           This function is used to sort the list in decending order.
        Parameter:
           lt is a container which holds the data init .
        Return:
           It print's list in decending order.
                    
    """
 
    lt = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
  
    sort_lt= sorted(lt,key=lambda n:n[-1])
    
    print("sorted list will be like: ",sort_lt)
    
if __name__=="__main__":
    main()