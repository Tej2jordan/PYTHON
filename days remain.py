# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
years_remaining =  90 - int(age)

days_remaining = years_remaining * 365

weeks_remaining = 52 * years_remaining

months_remaining = 12 * years_remaining

print(f"You have {days_remaining} days, {weeks_remaining} weeks and {months_remaining} months remaining in your life.")


