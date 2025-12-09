import pandas as pd
import os
from datetime import datetime

class FitnessTracker:
    def __init__(self):
        self.filename = "activities.csv"
        if not os.path.exists(self.filename):
            df = pd.DataFrame(columns=[
                "date", "steps", "distance", "workout_minutes",
                "calories", "activity_type"
            ])
            df.to_csv(self.filename, index=False)

    def add_activity(self, date_str, steps, distance, workout_minutes, calories, activity_type):
        df = pd.read_csv(self.filename)

        df.loc[len(df)] = [
            date_str,
            steps,
            distance,
            workout_minutes,
            calories,
            activity_type
        ]

        df.to_csv(self.filename, index=False)

        print("\nActivity Saved Successfully!")
        print(f"Date: {date_str}")
        print(f"Steps: {steps}")
        print(f"Distance: {distance} km")
        print(f"Workout Minutes: {workout_minutes}")
        print(f"Calories: {calories}")
        print(f"Activity Type: {activity_type}\n")

    def show_weekly_summary(self):
        df = pd.read_csv(self.filename)

        if df.empty:
            print("No activities found.")
            return
        
        df['date'] = pd.to_datetime(df['date'])
        df['week'] = df['date'].dt.isocalendar().week
        
        current_week = df['week'].max()
        week_df = df[df['week'] == current_week]

        print("\n--- Weekly Summary ---")
        print("Total Steps:", week_df['steps'].sum())
        print("Total Distance:", week_df['distance'].sum(), "km")
        print("Workout Minutes:", week_df['workout_minutes'].sum())
        print("Calories Burned:", week_df['calories'].sum())

    def visualize_weekly_report(self):
        import matplotlib.pyplot as plt
        
        df = pd.read_csv(self.filename)
        if df.empty:
            print("No data available.")
            return
        
        df['date'] = pd.to_datetime(df['date'])
        plt.plot(df['date'], df['steps'])
        plt.xlabel("Date")
        plt.ylabel("Steps")
        plt.title("Weekly Steps Trend")
        plt.savefig("weekly_report.png")
        plt.show()

    def save_weekly_summary(self):
        df = pd.read_csv(self.filename)
        if df.empty:
            print("No data to save.")
            return
        
        df['date'] = pd.to_datetime(df['date'])
        df['week'] = df['date'].dt.isocalendar().week
        
        current_week = df['week'].max()
        week_df = df[df['week'] == current_week]

        with open("weekly_summary.txt", "w") as f:
            f.write("Weekly Summary\n")
            f.write(f"Steps: {week_df['steps'].sum()}\n")
            f.write(f"Distance: {week_df['distance'].sum()} km\n")
            f.write(f"Workout Minutes: {week_df['workout_minutes'].sum()}\n")
            f.write(f"Calories: {week_df['calories'].sum()}\n")

        print("Summary saved to weekly_summary.txt")
