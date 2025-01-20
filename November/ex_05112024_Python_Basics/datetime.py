from datetime import datetime
date = "Nov 28 1987 4:00AM"
print(type(date))

date_time = datetime.strptime(date,"%b %d %Y,%I:%M%p")
print(date_time)