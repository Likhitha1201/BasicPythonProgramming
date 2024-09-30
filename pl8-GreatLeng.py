""" 

    @Author: Likhitha S
    @Date: 27-09-2024 16:30
    @Last Modified by: Likhitha S
    @Last Modified time: 27-09-2024 16:30
    @Title: Write a Python program to find the list words that are longer than n from a given list of words."
"""

def longer(lt,l):
    
    """
        
        Description:
            This function is used to remove duplicates from a list.
        Parameters:
           lt is a container which holds the data init .
        Return:
            It print's the words which are longer than specified length .
                    
    """
   
    lt2=[]
    for i in lt:
       if len(i)>l:
          lt2.append(i)
    return lt2


   
def main():
    lt=['Rachu','Menni','Chitti','Reeya','Kencha']
    l=int(input("Enter the length of word to be searched: "))
    words=longer(lt,l)
    print(words)
   
    
if __name__=="__main__":
    main()