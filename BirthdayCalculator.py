#!/usr/bin/env python3

import os
import math
from datetime import datetime, time, date

#function for date correction
def years_before(birth, current_date_time):
    if birth.year > current_date_time.year:
        day,month,year = birth.day , birth.month , birth.year
        x = year - 100
        new_date_str = "%s-%s-%s" % (day,month,x)
        b = datetime.strptime(new_date_str, '%m-%d-%Y')
        correct_date = b.strftime('%A, %B %d, %Y')
        print("Birthday: ", correct_date)

    elif birth.year < current_date_time.year:
        born = birth.strftime('%A, %B %d, %Y')
        print("Birthday: ", born)
        return

def days_birthday(current_date_time, birth):
    bday = date(2020, birth.month, birth.day)
    until_bday = bday - current_date_time
    return until_bday, bday



def main():

    cl = 0
    if cl == 0:
        os.system('clear||cls')
        cl =+ 1

    choice = "y"
    while choice.lower() == "y":
        print("\nBirthday Calculator\n")

        #gets input for name and birthday
        name = input("Enter name: ")
        birthday = input("Enter birthday (MM/DD/YY): ")
        
        #converts user input for birthday into a different format
        birth = datetime.strptime(birthday, '%m/%d/%y')
        
        #current date
        current_date_time = date.today()
        current_date_thing = current_date_time.strftime('%A, %B %d, %Y')
        
        #figuring out age
        age =  birth.year - current_date_time.year

        correct_date = years_before(birth, current_date_time)
        until_bday, bday = days_birthday(current_date_time, birth)
        
        #prints age and birthday info
        #makes it so if birthday after the current month and day, it minuses 1 to give the correct age
        print("Today:    ", current_date_thing)
        if age >= 0:
            if birth.month > current_date_time.month or birth.day > current_date_time.day:
                age -= 1
                print(name, "is", fix_age, "years old.")
            else:
                print(name, "is", age, "years old.")
        elif age < 0:
            if birth.month > current_date_time.month or birth.day > current_date_time.day:
                age_correct = abs(age)
                age_correct -= 1   
                print(name, "is", age_correct, "years old.")
            else:
                age_correct = age * -1
                print(name, "is", age_correct, "years old.")
        
        if until_bday.days == 1:
            print(name + "'s", "birthday is tomorrow!\n")
        elif until_bday.days == -1:
            print(name + "'s", "birthday was yesterday!\n")
        elif until_bday.days > current_date_time.day:
            print(name + "'s", "birthday is in", until_bday.days, "days.\n")
        elif until_bday.days == 0:
            print(name + "'s", "birthday is today!\n")
        elif until_bday.days < current_date_time.day:
            print(name + "'s", "birthday was", abs(until_bday.days), "days ago.\n")
        
        #continue
        choice = input("Continue (y/n): ")

if __name__ == "__main__":
    main()