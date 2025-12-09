# fitness_utils.py

import datetime as dt

# --------- DECORATOR ---------
def notify(func):
    """
    Decorator jo function ka naam dekh ke
    user-friendly message print karega.
    """
    messages = {
        "add_activity": "Recording activity...",
        "compute_weekly_stats": "Processing weekly statistics...",
        "visualize_weekly_progress": "Generating visualization...",
        "save_summary": "Saving file..."
    }

    def wrapper(*args, **kwargs):
        msg = messages.get(func.__name__, f"Running: {func.__name__}...")
        print(f"\n{msg}")
        return func(*args, **kwargs)

    return wrapper


# --------- LOGGING HELPER ---------
def log_message(message, log_file="activity_log.txt"):
    """
    activity_log.txt mein time ke saath log likhne ke liye.
    """
    timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")


# --------- INPUT VALIDATION HELPERS ---------
def validate_int_input(prompt):
    """
    Integer input safely lene ke liye.
    Jab tak sahi int na mile, repeat karega.
    """
    while True:
        value = input(prompt)
        try:
            return int(value)
        except ValueError:
            print("Please enter a valid integer number!")


def validate_float_input(prompt):
    """
    Float input safely lene ke liye.
    """
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Please enter a valid number!")


# --------- LAMBDA FUNCTION (Calorie Efficiency) ---------
# c = total calories, w = workout minutes
cal_eff = lambda c, w: round(c / w, 2) if w > 0 else 0.0
