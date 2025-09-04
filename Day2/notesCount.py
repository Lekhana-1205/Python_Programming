m = int(input("Enter amount: "))

def noteCount(m):
    notes = [2000, 500, 200, 100, 50, 20, 10, 5, 1]
    for note in notes:
        c = m // note
        if c > 0:
            print(f"{note} : {c}")
        m = m % note

noteCount(m)
