#day 3


#_____________________________________________________________
def data_table(table):
    for row in table:
        print(" ".join(map(str, row)))


table_data = [
    [1, 1, 1, 1, 1],
    [2, 1, 2, 4, 8],
    [3, 1, 3, 9, 27],
    [4, 1, 4, 16, 64],
    [5, 1, 5, 25, 125],
]

data_table(table_data)

#_____________________________________________________________
def print_table(rows):
    for i in range(1,rows + 1):
        rows = [i , 1 , i , i ** 2 , i ** 3]
        print(" ".join(map(str , rows)))
        
numberof_rows = 5

print_table(numberof_rows)


#the number of seconds a person can live. Assume a person can live hundred years

def calculate_seconds(years):
    if years <= 0:
        return 0
    else:
        days_in_year = 365
        hr_in_day = 24
        min_in_hr = 60
        sec_in_min = 60
        
        total_secs = years * days_in_year * hr_in_day * min_in_hr * sec_in_min 
        
        return total_secs
    
    
try:
    years = int(input("Please enter the years: "))
    if years <= 0:
        raise ValueError("The number of years cannot be negative or Zero")
    max_years = 100
    total_secs = calculate_seconds(min(years, max_years))
    
    print(f"You have lived approximately {total_secs:,} seconds in {years} years.")
except ValueError as ve:
    print(f"Error: {ve}. Please enter a valid number of years.")
except Exception as e:
    print(f"Error: {e}")
    
    
# Weekly earning calculator

def weekly_earning(hrs, rate_per_hrs):
    if hrs <= 0:
        return 0
    elif rate_per_hrs <= 0:
        return 0 
    else:
        weekly_earn = hrs * rate_per_hrs
        
        return weekly_earn

try:
    hours = int(input("Please enter the numbers of Hours you have worked in a week: "))
    rate_per_hours = int(input("Please enter your pay rate per hour: "))
    if hours <= 0:
        raise ValueError("The number of Hours cannot be negative or Zero")
    elif rate_per_hours <= 0:
        raise ValueError("The number of Pay Rate Per Hour cannot be negative or Zero")
    
    weekly_earn = weekly_earning(hours,rate_per_hours)
    
    print(f"Your Weekly earning is {weekly_earn} ")
except ValueError as ve:
    print(f"Error: {ve}. Please enter a valid number of Hours and Pay Rate Per Hour.")
except Exception as e:
    print(f"Error: {e}") 
    