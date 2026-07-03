months= [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        date=input("Date: ")
        if "/" in date:
            month, day, year = date.split("/")
            year=int(year)
            month=int(month)
            day=int(day)

            if not (1 <= month <= 12 and 1 <= day <= 31):
                raise ValueError
            
            # make the month and day two digits long
            print(f"{year}-{month:02d}-{day:02d}")
            break

        elif "," in date:
            month_day, year = date.split(",")
            year=year.strip()
            month, day = month_day.split()
            month = months.index(month) + 1
            print(f"{year}-{month:02d}-{int(day):02d}")
            break


    except ValueError:
        continue
    
