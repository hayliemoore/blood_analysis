def HDL_analysis(HDL_level):
    if HDL_level >= 60:
        return "Normal"
    elif 40 <= HDL_level < 60:
        return "Borderline Low"
    else:
        return "Low"


def LDL_analysis(LDL_level):
    if LDL_level < 130:
        return "Normal"
    elif 130 <= LDL_level < 159:
        return "Borderline High"
    elif 160 <= LDL_level < 189:
        return "High"
    else:
        return "Very High"


def cholesterol_analysis():
    print("Cholesterol Analysis")
    HDLinput = input("Enter test results: ")
    test_info = HDLinput.split("=")
    if test_info[0] == "HDL":
        answer = HDL_analysis(int(test_info[1]))
        print("the level is {}".format(answer))
    elif test_info[0] == "LDL":
        answer = LDL_analysis(int(test_info[1]))
        print("The level is {}".format(answer))
    else:
        print("test not recognized")


def new_feature():
    pass


def name_fuction():
    first_name = input("First name")
    last_name = input("last name")


def interface():
    while True:
        print("cholestterol calculator")
        print("options: ")
        print(" 1 - cholesterol Analysis")
        print(" 9 - Quit")
        choice = input("Enter your option: ")
        if choice == '9':
            return
        elif choice == "1":
            cholesterol_analysis()


def fever_check(temp_list):
    fever = False
    for temperature in temp_list:
        if temperature > 98.6:
            fever = true
        

if __name__ == "__main__":
    interface()
