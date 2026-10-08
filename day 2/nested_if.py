age = 82
Indian_Citizenship = False

if age >= 18:
    if Indian_Citizenship:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote. You must be an Indian citizen.")
else:
    print("You are not eligible to vote. You must be at least 18 years old.")