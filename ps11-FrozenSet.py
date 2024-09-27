""" 

    @Author: Likhitha S
    @Date: 27-09-2024 15:10
    @Last Modified by: Likhitha S
    @Last Modified time: 27-09-2024 15:10
    @Title: Write a Python program to use of frozensets.
    
"""

   
def main():
    """
        
        Description:
            This function is to know how frozen will work.
        Parameters:
           fro_set1, fro_set2 is a container which holds the data init .
        Return:
            it print's frozen set will work .
                    
    """
    
    fro_set1=frozenset([12,34,68,79,56])
    # we can't an element to frozen_set using add method.
    try:
         fro_set1.add(22)
    except AttributeError as e:
            print("error", e)
   
    print("Frozen set's are: ",fro_set1)
    
    # 2nd frozen_set
    fro_set2=frozenset([11,13,34,78,45,56])
    
    fro_set=fro_set1.intersection(fro_set2)
    print("Intersection of two frozen set's are: ", fro_set)
    
    fro_sett=fro_set1.union(fro_set2)
    print("Union of two frozen set's are: ", fro_sett)
    
    set_frozen=(fro_set1,fro_set2)
    print("set of frozen's are: ",set_frozen)
    
if __name__=="__main__":
    main()
