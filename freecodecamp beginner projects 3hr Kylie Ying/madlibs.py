 # madlib is a game where we read a sentence which has blank spaces filled person1 and read by someone other than person1

 # 3 ways to concat strings
    # 1. + operator
    # 2. "string {}".format("variable to interpolate in {}")
    # 3. fstring in python === f"string {py_variable}" more like template string

word1 = input("Enter word one: ")
word2 = input("Enter word two: ")

madlib = f"Your word1 is: {word1}. \
    Your word2 is {word2} "

print(madlib)  