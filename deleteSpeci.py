""" 

    @Author: Likhitha S
    @Date: 26-09-2024 13:20
    @Last Modified by: Likhitha S
    @Last Modified time: 26-09-2024 13:20
    @Title: Write a Python program to remove the first occurrence of a specified element from an array.

"""


import pandas as p


def count(arr, num):
    inx=0
    cou=0
    dele=[]
    for i in arr:
        if num==i:
           print(num,'->',inx)
           cou=inx
           break
        inx+=1
    return cou

def dele(arr,fd):
    arr_lt = []
    for i in arr:
        if i==arr[fd]:
            fd-=1
            continue
            
        else:
          arr_lt.append(i)
    
    return arr_lt
    
def main():
    """
        
        Description: 
            This function is used iterate the array and delete the specified element from array  at first occurrence.
        Parameters:
          arr and num  is an input of array type 
        Return:
            It prints the left over element from an array. 
    
    """
    
    
    arr = p.array([12,34,45,56,78,67,89,34,90])
    num=34
    print(arr," before deletion")
    first_inx=count(arr,num)
    new_arr=dele(arr,first_inx)
    print("After deleting the first occurrence of a given elelment:",new_arr)

    for i in new_arr:
        print(i)

if __name__=="__main__":
    main()    