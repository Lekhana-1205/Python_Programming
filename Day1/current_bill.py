cno=int(input("Consumer number:"))
cname=input("Consumer name:")
pmr=int(input("Present month reading:"))
lmr=int(input("last month reading:"))
tu=pmr-lmr
cbill=tu*3.80
print("Consumer number:",cno)
print("Present month reading:",pmr)
print("Last month reading:",lmr)
print("Consumer name:",cname)
print("Total units:",tu)
print("Current bill:",cbill)
#print(f"Consumer Details: {cno}, {pmr}, {lmr}, {cname}, {tu}, {cbill} ")