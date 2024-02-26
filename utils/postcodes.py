# postcodes.py

# Define a set of post codes
POST_CODES = {
    "N1",
    "N6",
    "N7",
    "N19",
    "NW1",
    "NW2",
    "NW3",
    "NW5",
    "NW6",
    "NW8",
    "EC1",
    "WC1",
    "WC2",
    "W1",
    "W9",
}


def is_valid_postcode(postcode):
    """Check if a postcode is in the set of post codes."""
    return postcode in POST_CODES
