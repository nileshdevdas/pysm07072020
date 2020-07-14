COUNT = 0 
SMALL_AIRPORTS = [] 
MED_AIRPORTS = [] 
LARGE_AIRPORTS = [] 
HELIPORT = [] 
OTHER = [] 
def airports_process(file):
    myfile = open(file=file, mode='rt', encoding='utf-8') 
    row = myfile.readline() 
    while row: 
        row = myfile.readline() 
        row = row.replace("\"", "") 
        if len(row) != 0: 
            cols = row.split(",") 
            if cols[2] == "small_airport": 
                SMALL_AIRPORTS.append(cols[3]) 
            elif cols[2] == "medium_airport": 
                MED_AIRPORTS.append(cols[3]) 
            elif cols[2] == "large_airport": 
                LARGE_AIRPORTS.append(cols[3]) 
            elif cols[2] == "heliport": 
                HELIPORT.append(cols[3]) 
            else: OTHER.append(cols[3]) 


airports_process('d:/airports1.csv')
print("SMALL AIPORT") 
print(len(SMALL_AIRPORTS)) 
print("LARGE AIPORT") 
print(len(LARGE_AIRPORTS)) 
print("MEDIUM AIPORT") 
print(len(MED_AIRPORTS)) 
print("HELIPORT") 
print(len(HELIPORT)) 
