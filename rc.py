COUNT = 0
SMALL_AIRPORTS = []
MED_AIRPORTS = []
LARGE_AIRPORTS = []
HELIPADS = []
OTHERS = []

def process_airports(file):
    myfile = open(file=file, encoding='utf-8', mode='rt')
    row = myfile.readline()
    while row:
        row = myfile.readline()
        row = row.replace("\"", "")
        if len(row) != 0:
            col = row.split(",")
            if col[2] == "small_airport":
                SMALL_AIRPORTS.append(col[3])
            elif col[2] == "large_airport":
                LARGE_AIRPORTS.append(col[3])
            elif col[2] == "medium_airport":
                MED_AIRPORTS.append(col[3])
            elif col[2] == "heliport":
                HELIPADS.append(col[3])
            else:
                OTHERS.append(col[3])

process_airports('d:/airports1.csv')
print(len(SMALL_AIRPORTS))
print(len(LARGE_AIRPORTS))
print(len(MED_AIRPORTS))
print(len(HELIPADS))
print(len(OTHERS))
