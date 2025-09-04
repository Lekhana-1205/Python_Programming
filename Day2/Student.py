s1 = int(input("Enter marks for subject 1: "))
s2 = int(input("Enter marks for subject 2: "))
s3 = int(input("Enter marks for subject 3: "))
total = s1 + s2 + s3
avg = total / 3
print(f"Total marks: {total}")
print(f"Average marks: {avg:.2f}")
def grade(m):
    if m < 40:
        return "Fail"
    elif 40 <= m <= 50:
        return "C grade"
    elif 50 < m <= 70:
        return "B grade"
    elif 70 < m <= 80:
        return "A grade"
    else:
        return "Distinction"
print("Grade:", grade(avg))
