def HDL_analysis(HDL_level):
    if HDL_level >= 60:
        return "Normal"
    elif 40 <= HDL_level < 60:
        return "Broderline low"
    else:
        return "Low"

def cholesterol_analysis():
    print("Cholesterol Analysis")
    HDLinput = input("Enter test results: ")
    test_info = HDLinput.split("=")
    if test_info[0] =="HDL":
        answer = HDL_analysis(int(test_info[1]))
        print("the level is {}".format(answer))



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
       
       
       
if __name__ == "__main__":
    interface()
    