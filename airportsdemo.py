"""
Airport Parsing Application
@author Nilesh D
"""
# sys inbuild module name sys which i am importing 
import sys

##### declaration ####
SMALL_AIRPORTS = []
MED_AIRPORTS = []
LARGE_AIRPORTS = []
HELIPADS = []
OTHERS = []
##########################


def process_airports(file):
    """
     Functiont to parse
    """
    myfile = open(file=file, encoding='utf-8', mode='rt')
    row = myfile.readline()
    while row:
        row = myfile.readline()
        # replacing a " with blank
        #row = row.replace("\"", "")
        if len(row) != 0:
            cols = row.split(",")
            if cols[2] == "\"small_airport\"":
                SMALL_AIRPORTS.append(cols[3])
            elif cols[2] == "\"heliport\"":
                HELIPADS.append(cols[3])
            elif cols[2] == "\"large_airport\"":
                LARGE_AIRPORTS.append(cols[3])
            elif cols[2] == "\"medium_airport\"":
                MED_AIRPORTS.append(cols[3])
            else:
                OTHERS.append(cols[3])
    print("Small Airports ")
    print(len(SMALL_AIRPORTS))
    print("Med  Airports ")
    print(len(MED_AIRPORTS))
    print("Large  Airports ")
    print(len(LARGE_AIRPORTS))
    print("Helipads")
    print(len(HELIPADS))
    print("others")
    print(len(OTHERS))

filename = sys.argv[1]
print(filename)
process_airports(filename);
