""" 

    @Author: Likhitha S
    @Date: 27-09-2024 15:30
    @Last Modified by: Likhitha S
    @Last Modified time: 27-09-2024 15:30
    @Title: Write a Python program to count the number of strings where the string length
    is 2 or more and the first and last character are same from a given list of strings.
    Sample List : ['abc', 'xyz', 'aba', '1221']
    Expected Result : 2
    
"""

   
def count_match_str(data):
    """
        
        Description:
            This function is used to count the number of letters in string and to check last and first letters are same in a list.
        Parameters:
           lt is a container which holds the data init .
        Return:
           It print's number of string are following the context given .
                    
    """
    
    count=0
    
    for s in data:
        if len(s)>=2 and s[0]==s[-1]:
            count +=1
            
    return count






def main(): 
    lt = ['abc', 'xyz', 'aba', '1221']
  
    result=count_match_str(lt)
    print("Number of strings where length is 2 or more and first and last character are the same:", result)
    
    
if __name__=="__main__":
    main()