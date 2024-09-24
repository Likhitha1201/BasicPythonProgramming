""" 

    @Author: Likhitha S
    @Date: 23-09-2024 17:50
    @Last Modified by: Likhitha S
    @Last Modified time: 23-09-2024 17:50
    @Title: Write a Python program to calculate number of days between two dates.

"""

def main():
    """
        
        Description: 
            This function is used to calculate the number of days present between two date's.
        Parameters:
          d1 and d2 are the two user input .
        Return:
            It returns the number of days present in between the two date's. 
        
    """
    d1 = input("Enter the date (day,month,year) separated by (,):")
    d2 = input("Enter the date (day,month,year) separated by (,):")
    
    
    date1=d1.split(',')
    date2=d2.split(',')
    
    day1, month1, year1= int(date1[0]), int(date1[1]), int(date1[2])
    day2, month2, year2= int(date2[0]), int(date2[1]), int(date2[2])
    
    day=day1-day2
    month=month1-month2
    year=year1-year2
    
    print(abs(day),'days', abs(month),'months', abs(year),'years')
    
if __name__=="__main__":
    main()
