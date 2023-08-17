import os
import json


high_risk_warning = """
------------------------------
|  THIS PATIENT IS AT HIGH   |
|       RISK OF OPIOID       |
|         DEPENDENCY         |
------------------------------
"""

FILENAME = "patient_data.json"

patient_data = {}
with open(FILENAME, "r") as json_file:
    patient_data = json.load(json_file)
for key in list(patient_data.keys()):
    patient_data[int(key)] = patient_data[key]
    del patient_data[key] 


def search():
    valid = False
    while not valid:
        os.system('cls')
        print("Please enter the Health Card Number of the patient's data you wish to view\n")
        try:
            card_num = input("Health Card Number: ").strip(" ").strip(",").strip()
            card_num = int(card_num)
            
            if len(str(card_num)) != 10:
                placeholder = input("The Health Card Number must be exactly 10 digits long.\nPress enter to enter the Health Card Number again.")
            else:
                valid = True
        except ValueError:
            placeholder = input("The Health Card Number must contain Digits only.\nPress enter to enter the Health Card Number again.")
    
    try:
        os.system('cls')
        patient = dict(patient_data[card_num])

        print("Please find below the corresponding patient's data:")

        # if opioid_risk == 1:
        #     print(high_risk_warning)

        for key, value in patient.items():
            print(f"{key}: {value}")
        placeholder = input("\nPress Enter to Continue")
    except KeyError:
        placeholder = input("A patient with that Health Card Number does not exist.")


def update():
    valid = False
    while not valid:
        os.system('cls')
        print("Please enter the Health Card Number of the patient's data you wish to update\n")
        try:
            card_num = input("Health Card Number: ").strip(" ").strip(",").strip()
            card_num = int(card_num)
            
            if len(str(card_num)) != 10:
                placeholder = input("The Health Card Number must be exactly 10 digits long.\nPress enter to enter the Health Card Number again.")
            else:
                valid = True
        except ValueError:
            placeholder = input("The Health Card Number must contain Digits only.\nPress enter to enter the Health Card Number again.")

    try:
        os.system('cls')
        patient = dict(patient_data[card_num])

        updated_patient = modify(patient)
        patient_data[card_num] = updated_patient
    except KeyError:
        placeholder = input("A patient with that Health Card Number does not exist.\nPress Enter to Continue.")


def modify(patient):
    done = False
    while not done:
        os.system('cls')
        print("Which item would you like to update?\n")
        counter = 0
        for key, value in patient.items():
            counter += 1
            print(f"{counter} - {key}: {value}")
        counter += 1
        print(f"{counter} - SELECT TO CANCEL")
        selection = input("\nPlease enter the number corresponding to the item you would like to modify: ").strip()
        try:
            selection = int(selection)
            if selection not in range(1, len(list(patient.keys())) + 2):
                placeholder = input("Please only enter one of the digits above.\nPress enter to try again.")
            else:
                bypass = False

                if selection == 1:
                    name = input("Please enter the updated full name: ")
                    patient["Full Name"] = name
                if selection == 2:
                    valid = False
                    while not valid:
                        age = input("Please enter the updated age: ").strip()
                        try:
                            age = int(age)
                            patient["Age"] = age
                            valid = True
                        except ValueError:
                            print("Please enter a number for the age.")
                if selection == 3:
                    conditions = input("Please enter the updated diagnosed conditions: ")
                    patient["Diagnosed Conditions"] = conditions
                if selection == 4:
                    medications = input("Please enter the updated current medications: ")
                    patient["Current Medications"] = medications
                if selection == 5:
                    valid = False
                    while not valid:
                        history = input("Does the patient's family have a history of substance abuse? Enter Y for yes, or N for no: ").strip()
                        if history.lower() != "y" and history.lower() != "n":
                            print("Please only enter Y or N.")
                        else:
                            if history.lower() == "y":
                                patient["Family History"] = "Yes"
                            elif history.lower() == "n":
                                done = True
                                patient["Family History"] = "No"
                            valid = True
                if selection == 6:
                    location = input("Please enter the updated geographic location: ")
                    patient["Geographic Location"] = location
                if selection == 7:
                    done = True
                    bypass = True
                
                valid = False
                while not valid:
                    if bypass:
                        break

                    os.system('cls')
                    print("Which item would you like to update?\n")
                    counter = 0
                    for key, value in patient.items():
                        counter += 1
                        print(f"{counter} - {key}: {value}")
                    selection = input("\nWould you like to modify another item? Enter Y for yes, or N for no: ").strip()
                    if selection.lower() != "y" and selection.lower() != "n":
                        print("Please only enter Y or N.")
                    else:
                        if selection.lower() == "y":
                            valid = True
                        elif selection.lower() == "n":
                            done = True
                            valid = True
        except ValueError:
            placeholder = input("Please only enter one of the digits above.\nPress enter to try again.")

    return patient


def save():
    with open(FILENAME, "w") as jsonfile:
        jsonfile.write(json.dumps(patient_data, indent=4, separators=(',',': ')))
    



while True:
    os.system('cls')
    print("Please enter one of the below numbers below corresponding to a menu choice:\n1 - Search Patient\n2 - Update Patient\n3 - Add New Patient\n")
    selection = input("Enter selection here: ").strip()

    try:
        selection = int(selection)
        if selection not in [1, 2, 3]:
            placeholder = input("Please enter only 1, 2, or 3. Press Enter to continue.")
        else:
            if selection == 1:
                search()
            if selection == 2:
                update()
                save()
    except ValueError:
        placeholder = input("Please enter only 1, 2, or 3. Press Enter to continue.")