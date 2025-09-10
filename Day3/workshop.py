day1=input("Enter emails for day1:").split()
day2=input("Enter emails for day2:").split()
day3=input("Enter emails for day3:").split()
d1=set(email.lower() for email in day1)
d2=set(email.lower() for email in day2)
d3=set(email.lower() for email in day3)

unique_attend=d1|d2|d3
print("total no.of unique attendees is",len(unique_attend))
print((sorted(unique_attend)))

all_days=d1&d2&d3
print("attendees attended all 3 days are ",len(all_days))
print((sorted(all_days)))
one_day=d1^d2^d3 - (d1&d2&d3)
print("attendees attended exactly 1 day are ",len(one_day))
print((sorted(one_day)))
print("day1&day2:",len(d1&d2))
print("day2&day3:",len(d2&d3))
print("day3&day1:",len(d3&d1))