""" 

    @Author: Likhitha S
    @Date: 30-09-2024 16:20
    @Last Modified by: Likhitha S
    @Last Modified time: 30-09-2024 16:20
    @Title: Write a Python program to generate all permutations of a list in Python.
    
"""

def permutation(n,r):
    """
        
        Description:
            This function is used takes list as an input and perform permutation.
        Parameters:
           lt is a container which is used to hold the data init .
        Return:
            It print's permutation of the given element .
                    
    """
    
    lt=[]
    for i in range(len(n)):
            lt.append(fact(n[i], r[i]))
    return lt
   
def fact(i,j):
    prod=1
    for x in range(1,i+1):
        prod*=x
        
    prod1=1
    rr= i-j
    for x in range(1,rr+1):
        prod1*=x
        
    div=prod/prod1
        
    return div
   
def main():
    """
        n and r is a container which is holding a data init .
    """
   
    n=[5,6,7,8]
    r=[3,4,2,1]
    res=permutation(n,r)
    print(res)
    
    
if __name__=="__main__":
    main()
    
    
