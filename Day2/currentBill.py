cust_no = int(input("Enter customer number: "))
cust_name = input("Enter customer name: ")
pmr = int(input("Enter present meter reading: "))
lmr = int(input("Enter last meter reading: "))

tu = pmr - lmr  # total units

def cbill(tu):
    if tu <= 0:
         return 0
    if tu <= 50: 
        return tu * 3.80
    if tu <= 100:
         return 50 * 3.80 + (tu - 50) * 4.20
    if tu <= 200:
         return 50 * 3.80 + 50 * 4.20 + (tu - 100) * 5.10
    if tu <= 300:
         return 50 * 3.80 + 50 * 4.20 + 100 * 5.10 + (tu - 200) * 6.30
    return 50 * 3.80 + 50 * 4.20 + 100 * 5.10 + 100 * 6.30 + (tu - 300) * 7.50

bill = cbill(tu)

print("\ncust_no  cust_name   pmr   lmr   units   bill")
print(f"{cust_no:<8}{cust_name:<12}{pmr:<6}{lmr:<6}{tu:<7}{bill:.2f}")
