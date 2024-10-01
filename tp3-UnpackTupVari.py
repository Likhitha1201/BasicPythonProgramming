""" 

    @Author: Likhitha S
    @Date: 30-09-2024 9:40
    @Last Modified by: Likhitha S
    @Last Modified time: 1-10-2024 9:40
    @Title:Write a Python program to unpack a tuple in several variables.

"""

def main():
    
    """
        
        Description:
            This function is used to unpack a tuple in several variable.
        Parameter:
            tup is container which is used to store the elements init.
        Return:
           It print's the elements of unpacked type.
                    
    """
  
    tup= 1, "Chummi", 6, 2, 8
    a,b,c,d,e=tup
    print(tup)
    
  
    print("a: ",a)
    print("b: ",b)
    print("c: ",c)
    print("d: ",d)
    print("e: ",e)
    
if __name__=="__main__":
    main()