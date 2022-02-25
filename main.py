import sys

print ("Welcome to Scientific-Tools v0.1.0\n\n")

while True:
    print("Please select an option from the following menu:\n")

    print("1. Clausius-Clayperon Equations")
    print("2. Arrhenius Equations")
    print("3. About and More Information\n")

    try:
        menu_one_choice = int(input())
        if menu_one_choice == 1:
            while True:
                print("Please select an option from the following menu:\n")

                print("1. Clausius-Clayperon Equation Single Point Form (ln P = -Hvap/RT)")
                print("2. Clausius-Clayperon Equation Dual Point Form (ln P2/P1 = -Hvap/R * (1/T1 - 1/T2))\n")

                try:
                    menu_two_choice = int(input())
                    if menu_two_choice == 1:
                        while True:
                            print("Please select an option from the following menu:\n")
                            
                            print("1. Solve for Pressure")
                            print("2. Solve for Temperature\n")

                            try:
                                menu_three_choice = int(input())
                                if menu_three_choice == 1:
                                    while True:
                                        print("Please enter the temperature in Kelvin:\n")

                                        try:
                                            klvn_temp = int(input())
                                        except:
                                            print("Incorrect or broken input. Please try again.\n")
                                            continue
                                else:
                                    print("Incorrect or broken input. Please try again.\n")
                                    continue
                    else:
                        print("Incorrect or broken input. Please try again.\n")
                        continue
                except:
                    print("Incorrect or broken input. Please try again.\n")
                    continue
        else:
            print("Incorrect or broken input. Please try again.\n")
            continue
    except:
        print("Incorrect or broken input. Please try again.\n")
        continue
