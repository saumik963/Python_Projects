def age_cal(cy, cm, cd, by, bm, bd):
    # Calculate age in days
    age_in_days = (cy - by) * 365 + (cm - bm) * 30 + (cd - bd)
    
    # Calculate years, months, and remaining days
    age_years = age_in_days // 365
    age_months = (age_in_days % 365) // 30
    age_days = (age_in_days % 365) % 30

    print(f"|>  Current Age is: {age_years} years {age_months} months {age_days} days")  
    print(f"|>  Or Current Age is: {age_in_days} days")


print("Age Calculator\nUse space after each input.\n")

cy, cm, cd = map(int, input("Enter Current YY/MM/DD: ").split())


by, bm, bd = map(int, input("Enter D.O.B YY/MM/DD: ").split())

print("----------------------------------------------------")
age_cal(cy, cm, cd, by, bm, bd)
print("----------------------------------------------------")
