""" 

    @Author: Likhitha S
    @Date: 30-09-2024 9:55
    @Last Modified by: Likhitha S
    @Last Modified time: 1-10-2024 9:55
    @Title:Write a Python program to find the repeated items of a tuple.
    
"""

def main():
    
    """
        
        Description:
            This function is used to fined the elements which are repeated.
        Parameter:
            tup is container which is used to store the tuple type of data.
        Return:
           It print's the elements.
                    
    """
  
    tup=(12,29,45,75,56,89,56,45) 
    unq=()
    for i in range(len(tup)):
        for j in range(i+1, len(tup)):
            if tup[i]==tup[j]:
                if tup[i] not in unq:
                    unq=unq+(tup[i],)
            
    print(unq)
if __name__=="__main__":
    main()