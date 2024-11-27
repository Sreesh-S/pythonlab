day=int(input("enter the day (1-31):"))
month=int(input("enter the month (1-12):"))
year=int(input("enter the day (eg:2024....):"))
print(f"entered date: {day:02d} - 2{month:02d} - {year}")
if(year % 4 == 0 and year == 100 != 0)or(year % 400 == 0):
    print(f"The year {year} is leap year.")
else:
    print(f"Tne Entered {year} is not an leap year")