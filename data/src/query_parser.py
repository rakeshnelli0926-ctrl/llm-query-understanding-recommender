import re

def parse_query(query):

    price_match = re.search(r'under (\d+)', query)
    price = int(price_match.group(1)) if price_match else None

    feature = None
    if "noise cancelling" in query:
        feature = "noise cancelling"

    return {
        "price": price,
        "feature": feature
    }

query = "cheap wireless headphones under 50 with noise cancelling"

print(parse_query(query))
