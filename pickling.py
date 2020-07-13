# import stands for importing modules
import pickle

# name = ['nilesh', 'ramesh', 'jayesh', 'abhishek',
#         'satish', 'parag', 'amit', 'saheen']

# # writing the object to the file so that you have all you file state storing object values

# outfile = open('d:/names.ser', 'wb')
# pickle.dump(name, outfile);

readfile = open('d:/names.ser', 'rb')
names_from_file = pickle.load(readfile)
print(names_from_file)

