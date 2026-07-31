from datetime import date
import sys
import inflect

p = inflect.engine()

class DateOfBirth:
    def __init__(self, date_str):
        try:
            self.date = date.fromisoformat(date_str)
        except ValueError:
            sys.exit("Invalid date")

    def totalminutes(self):
        dif=date.today()-self.date
        minutes_number=(dif.days)*24*60
        minutes_text=p.number_to_words(minutes_number, andword="").capitalize()
        return f"{minutes_text} minutes"

    def __str__(self):
        return self.totalminutes()
    
def main():
    print(get_date())

def get_date():
    date=input("Date of birth: ")
    return DateOfBirth(date)

if __name__ == "__main__":
    main()