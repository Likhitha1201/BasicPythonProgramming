""" 

    @Author: Likhitha S
    @Date: 23-09-2024 18:00
    @Last Modified by: Likhitha S
    @Last Modified time: 23-09-2024 18:00
    @Title: Write a Python program to check whether a specified value is contained in a group of values.

"""


def isFound(List,num):
    """
        
        Description: 
            This function is used to check the specified value present in list.
        Parameters:
            lt and num are the user input.
        Return:
            It returns the boolean value if present or not. 
        
    """
    for i in List:
      return i==num

def main():
  
    List=[input("Enter the number separated by comma(,): ")]
    num=int(input("Enter the number: "))


    result=isFound(List,num)
    if result==True:
        print(num,',',List,' in a list is it found Yes..!!!')
    else:
        print(num,',',List,' in a list is it found No...???')


if __name__=="__main__":
    main()