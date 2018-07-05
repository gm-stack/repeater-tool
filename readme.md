# Repeater Tool

Reads the WIA's [published list of repeaters](http://www.wia.org.au/members/repeaters/data/), parses it and outputs some more useful formats.

The WIA has a download of some VBScript to do this, but it doesn't export to any of the formats I'm after.

# Currently Implemented

icom_output - Suitable for import into CS-7100, for the Icom 7100. May work on other Icom models.

# Usage

`./repeaters.py /path/to/Repeater\ Directory\ 180318.csv` (or whatever's the latest version)

Alternatively if you just want to get the resulting files, I've checked them into the git repository.

# Todo

- Amateur TV repeaters are ignored, as they don't all have a simple in/out frequency.
- D-Star repeater CSV needs to be turned into a different set of columns to be usable in CS-7100
- KG-UV9D+ support - however this software doesn't have CSV import...
- Just export to JSON for whatever else.

 # Repeater Names

 Callsigns are abbreviated to 3 characters - they all start with VK, and have R after the number, so we can lose those bits.

 Location is then appended.