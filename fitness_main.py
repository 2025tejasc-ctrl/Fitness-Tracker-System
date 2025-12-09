# fitness_main.py

from fitness_tracker_class import FitnessTracker
from fitness_utils import validate_int_input, validate_float_input


def add_activity_menu(tracker: FitnessTracker):
    """
    User se daily activity ka input lega
    aur tracker.add_activity() call karega.
    """
    print("\n--- Add New Activity ---")
    date_str = input("Enter date (YYYY-MM-DD) or leave blank for today: ")

    steps = validate_int_input("Enter steps: ")
    distance = validate_float_input("Enter distance walked (in km): ")
    calories = validate_int_input("Enter calories burned: ")
    workout_minutes = validate_int_input("Enter workout minutes: ")

    activity_type = input("Enter activity type (Walking/Running/Gym/Cycling/Yoga/etc.): ")

    tracker.add_activity(
        date_str=date_str,
        steps=steps,
        distance=distance,
        calories=calories,
        workout_minutes=workout_minutes,
        activity_type=activity_type
    )


def weekly_summary_menu(tracker: FitnessTracker):
    """
    Weekly stats compute karega aur summary print karega.
    """
    tracker.show_weekly_summary()

def visualize_menu(tracker: FitnessTracker):
    print("\nGenerating Weekly Chart...")
    tracker.visualize_weekly_report()
    print("Chart saved as weekly_report.png\n")



def save_summary_menu(tracker: FitnessTracker):
    print("\nSaving Weekly Summary...")
    tracker.save_weekly_summary()
    print("Summary saved as weekly_summary.txt\n")



def main():
    tracker = FitnessTracker()

    print("Welcome to the Fitness Tracker")

    while True:
        print("\n==== MAIN MENU ====")
        print("1. Add New Activity")
        print("2. Show Weekly Summary")
        print("3. Generate Weekly Charts")
        print("4. Save Weekly Summary to File")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_activity_menu(tracker)
        elif choice == "2":
            weekly_summary_menu(tracker)
        elif choice == "3":
            visualize_menu(tracker)
        elif choice == "4":
            save_summary_menu(tracker)
        elif choice == "5":
            print("Exiting... Goodbye! Stay fit 💪")
            break
        else:
            print("Invalid choice, please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
