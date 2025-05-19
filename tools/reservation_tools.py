
import random
import sys
import os

# Ensure the parent directory is in the Python path for module resolution
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from data.restaurants import RESTAURANTS

def make_reservation(location=None, cuisine=None, num_people=None, party_size=None, time=None, restaurant_name=None):
    # Normalize synonyms
    if not num_people and party_size:
        num_people = party_size

    # Ask for missing parameters
    missing = []
    if not (restaurant_name or cuisine):
        missing.append("preferred restaurant or cuisine (e.g., SamBar Pub, South Indian)")
    if not location:
        missing.append("location (e.g., Andheri, Juhu)")
    if not num_people:
        missing.append("number of people")
    if not time:
        missing.append("reservation time (e.g., 7 PM, tonight at 8)")

    if missing:
        return f"🤖 Could you please tell me your {', '.join(missing)} so I can book a table for you?"

    # Prepare filters
    location = location.lower()
    cuisine = cuisine.lower() if cuisine else ""
    restaurant_name = restaurant_name.lower() if restaurant_name else ""

    # Filter by restaurant_name if provided, otherwise fallback to cuisine
    if restaurant_name:
        filtered = [r for r in RESTAURANTS if restaurant_name in r["name"].lower()]
    else:
        filtered = [
            r for r in RESTAURANTS
            if location in r["location"].lower() and cuisine in r["cuisine"].lower()
        ]

    if not filtered:
        return f"🔍 Sorry, couldn't find a matching restaurant for your request."

    selected = filtered[0]

    return (
        f"✅ Reserved a table for **{num_people}** at **{selected['name']}** "
        f"({selected['cuisine']}) in **{selected['location']}** at **{time}**. "
        f"(Seating capacity: {selected['seating_capacity']})"
    )
