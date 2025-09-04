def word():
    number_words = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"
    }
    for num in range(1, 11):
        print(number_words[num])

word()
