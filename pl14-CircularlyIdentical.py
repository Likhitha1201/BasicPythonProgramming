""" 

    @Author: Likhitha S
    @Date: 30-09-2024 17:00
    @Last Modified by: Likhitha S
    @Last Modified time: 30-09-2024 17:00
    @Title: Write a python program to check whether two lists are circularly identical.
    
"""

def isCircular(lt1,lt2):
    
    """
        
        Description:
            This function is used the to check the given list are identical or not.
        Parameter:
           res is a container which is used to hold the data init .
        Return:
           It print's wheather given is circularly identical or not .
                    
    """
    if len(lt1)!=len(lt2):
        return False
    
    concatination= lt1+lt1
    
    for i in range(len(lt1)):
        if concatination[i:i+len(lt2)]==lt2:
            return True
    
   
def main():
    """
        lt1 and lt2 is a container which is holding a data init .
    """
    
    lt1=[2,3,4,1]
    lt2=[1,2,3,4]
    
    res=isCircular(lt1,lt2)
    if res:
        print("The lists are circularly identical.")
    else:
        print("The lists are not circularly identical.")
        
    
if __name__=="__main__":
    main()