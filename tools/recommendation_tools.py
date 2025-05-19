from data.restaurants import RESTAURANTS

def get_recommendation(location=None, diet=None):
    filtered = [
        r for r in RESTAURANTS
        if (not location or location.lower() in r['location'].lower())
    ]

    if diet:
        filtered = [r for r in filtered if diet.lower() in r['tags']]

    if not filtered:
        return "🔍 Sorry, couldn't find a suitable place."

    r = filtered[0]
    return f"🍴 Try {r['name']} ({r['cuisine']}) in {r['location']}. Highly rated for {diet or 'great food'}!"
