import datetime


def lock_data():
    user_inp = int(input("Press 1 to lock Exercise or 2 for lock Diet.\n"))
    if user_inp is 1:
        user_input_exercise = int(input(

            "press 1 to lock Exercise of Harry.\npress 2 to lock Exercise of Aditya.\npress 3 to lock Exercise of Mangal.\n"))

        if user_input_exercise is 1:
            exercise_data_harry = input(
                "Enter the Exercise you want to lock for Harry.\n")
            with open("harry_exercise.txt", 'a') as f:
                f.write(f"{exercise_data_harry} Done at {datetime.datetime.now()}\n")
                print("Exercise locked successfully\n")

        elif user_input_exercise is 2:
            exercise_data_aditya = input(
                "Enter the Exercise you want to lock for Aditya.\n")

            with open("aditya_exercise.txt", 'a') as alfa:

                alfa.write(f"{exercise_data_aditya} Done at {datetime.datetime.now()}\n")

                print("Exercise locked successfully.\n")

        elif user_input_exercise is 3:
            exercise_data_mangal = input(
                "Enter the exercise you want to lock for Mangal.\n")
            with open("mangal_exercise.txt", 'a') as file:
                file.write(f"{exercise_data_mangal} Done at {datetime.datetime.now()}\n")

                print("Exercise locked successfully\n")

        else:
            print("Something Wrong! Please check your input.")

    elif user_inp is 2:

        user_input_lock = int(input(
            "press 1 to lock diet of Harry.\npress 2 to lock diet of Aditya.\npress 3 to lock diet of Mangal.\n"))

        if user_input_lock is 1:

            diet_data_harry = input(
                "Enter the diet you want to lock for Harry.\n")
            with open("harry_diet.txt", 'a') as f:
                f.write(f"{diet_data_harry} ate at {datetime.datetime.now()}\n")
                print("Diet locked successfully\n")
        elif user_input_lock is 2:
            diet_data_aditya = input(

                "Enter the diet you want to lock for Aditya.\n")
            with open("aditya_diet.txt", 'a') as alfa:
                alfa.write(
                    f"{diet_data_aditya} ate at {datetime.datetime.now()}\n")
                print("Diet locked successfully\n")
        elif user_input_lock is 3:
            diet_data_mangal = input(

                "Enter the diet you want to lock for Mangal.\n")

            with open("mangal_diet.txt", 'a') as file:
                file.write(
                    f"{diet_data_mangal} ate at {datetime.datetime.now()}\n")
                print("Diet locked successfully\n")

        else:
            print("Something Wrong! Please check your input.")

    else:
        print("Something Wrong! Please check your input.")

    again_lock()

    


def retrieve():
    user_input_retrieve = int(input(
        "press 1 to retrieve diet of Harry.\npress 2 to retrieve diet of Aditya.\npress 3 to retrieve diet of Mangal.\n"))
    if user_input_retrieve is 1:
        with open("harry_diet.txt") as f:
            print("\t\t Recent Diets-\n")
            print(f.read())

    elif user_input_retrieve is 2:
        with open("aditya_diet.txt") as file2:
            print("\t\t Recent Diets-\n")
            print(file2.read())

    elif user_input_retrieve is 3:
        with open("harry_diet.txt") as file3:
            print("\t\t Recent Diets-\n")
            print(file3.read())
    again_retrieve()

def again_lock():
    user_again = int(input("Want to lock more?\nPress 1 to lock more or 2 to exit.\n"))
    if user_again is 1:
        lock_data()
    else:
        print("\t\t Thank You!")

def again_retrieve():
    user_again_2 = int(input("Want to retrieve more?\nPress 1 to retrieve more or 2 to exit.\n"))
    if user_again_2 is 1:
        retrieve()
    else:
        print("\t\t Thank You!")



print("\t\t **Health Mangaement System**\t\t")
user_input = int(input(
    "What you want to do. Lock data or retrieve data?\nPress 1 to lock and 2 for retrieve.\n"))

if user_input is 1:
    lock_data()

elif user_input is 2:
    retrieve()

else:
    print("Wrong input")
