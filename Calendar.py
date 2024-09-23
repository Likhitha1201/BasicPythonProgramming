""" 

    @Author: Likhitha S
    @Date: 23-09-2024 17:30
    @Last Modified by: Likhitha S
    @Last Modified time: 23-09-2024 17:30
    @Title:Write a Python program to print the calendar of a given month and year.

"""
import calendar

def main():
    """
        
        Description: 
            here, according to user input, it going to print the caledar.
        Parameters:
          month is used to take an input from the user .
        Return:
            It prints the calendar according to that of given month . 
        
    """
    
    year = int(input("Enter the year be like 2024..")) 
    month = int(input("Enter the month between (1-12)"))
    
    cal = calendar.TextCalendar()
    
    print(cal.formatmonth(year, month))
    
    
if __name__=="__main__":
    main() 
    