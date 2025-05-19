from datetime import datetime

def format_datetime(time_str):
    """
    Format time string to a readable datetime object.
    Example: "18:30" -> "06:30 PM"
    """
    try:
        dt = datetime.strptime(time_str, "%H:%M")
        return dt.strftime("%I:%M %p")
    except Exception as e:
        return time_str  # fallback if parsing fails
