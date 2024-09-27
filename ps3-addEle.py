""" 

    @Author: Likhitha S
    @Date: 27-09-2024 14:00
    @Last Modified by: Likhitha S
    @Last Modified time: 27-09-2024 14:00
    @Title:3. Write a Python program to add member(s) in a set.
    
"""

   
def main():
    """
        
        Description:
            This function is used to add an element in to a set.
        Parameters:
           set1 and set2 is a container which holds the data init .
        Return:
            It prints the set.
                    
    """
    
    set1=set()
    set1.add(10)  # adding an elements to a emptyset
    set1.add(20)
    set1.add(30)
    print(set1)
    
    set2={12,23,45}
    set2.add(45)
    set2.add(87)
    set2.add(90)
    print(set2)
    
if __name__=="__main__":
    main()