# Day 1 
What is python ? 

Python is interpreted language 
python is indented language
python is having its own zen  "ZEN of python"  
python is dnamically  type programming  
python does not mandate data types
Python does not need main and file extions of python.py
Python file does not need to be compiled .py can directly run 
        using the standard command :- 
        python <filename.py>
Python  being itepreted has a drawback on memory every line is parsed in the memory
        how python also becomes fast as everything in memory 
Python is functional language --> 
         has lot of built in function/ modules and support 3rd party \
Python has external modules and libraries  
Python was written using c as the base and it extends the function c in python 
Python has it framework 
            Flask / Django 
            Numpy
            Scipy 
            Seaborn 
            ....... 

CMD : 
1.   python -V 


What is a REPL : 
R-ead 
E-val 
P-rint 
L-oop

print("Hello World")

print('Hello World')


How do i exit the REPL 
exit()


Data Types in pyton :- 
a = 10 
a = 20 
a = "Nilesh" 
a = True 
a = None 
a = 10.2 

Data Type in python 
=-----------------------------------
int
float 
str
boolean
None 
------------------------------------------------
Python 32 bit  [Python 32 allow max 1.5 gb resident memory]
Python 64 bit  [Allwos  256 GB resident memory]

Python download : 
   Python 

------------------------------------------------------------------------
a = 10 
b = 20 
if a > 10: 
    print(a)

-----------------------------------------------------------------------
REPL : 
Read Eval Print Loop 
Python : cmd prompt without a file name it goes in the python repl mode 

Python allows you to run both stand alone script 
interactive scripts 
python --> REPL 
python file_name -- Standalone 

----------------------------------------------------------------------------
Python has varibles and varaibles are dymically types 
a = 10 
a = True 
a = "" 
a = None 
a =  xxxxxxx // anything 
------------------------------------------------------------------------------

# how to install packages or tools for python w
we use pypi via pip 

int 
float 
string
boolean 
none 

list
A collection of values which allows duplicates and is mutable /index list   

tuple 
a collection of values that is allowing duplicate but sealed and immutable 4

set 
a collection values that are non duplicate but mutable 

dict 
A dictionary is a value  name value keypair 
---------------------------
list = []
.append
tuple = ()
set = {1,2,3,4}
add
dict = {'key': 'val'}
---------------------------

int
float 
boolean
string 
none
list
tuple
set
dict 

input  ;;where u can read comand 
print  ;; write to console 
operatio 
append 
add 
pop 

inbuilt function 
sum 
min
max 
len 
print
open 
input 

Indentations 



Review : 

Flow control 
if elif and else 
while 
for 
range 


--------------------------------------------------------------------------------
1. Python is intrepreted 
2. REPL 
3. Installing python 32/64 linux/windows 
4. documented 
5. Python Interactive Shell 
6. Python  .py files 
7. everything is varaible stored in the globals 
    a) is a variable 
    b) data is a variable 
8.  String and datatypes 
    int
    float 
    boolean 
    str 
    none 
9.  set 
    list
    tuple 
    dict 

10.  indentations block identified by : empty enter ends the block 
11.  there inbuilt functions 
     len()
     sum()
     min()
     max()
     input()
     print()
     range()

12.  for / if / elif / while  and related things 
     we have no straight functions we range ()
     for loops with steps 
     identation is the key to everything 

13.  code assig py readine 
     pip  install 
     pip  freeze 
     pip  ..... 


14,  list append 
     set.add 
     dict[''] = value 
    clear. remove, 

15.  object run story 
    del if we declare something its our responsibility to do removal 
    del :- is removeal of variable 

16.  globals() // locals()

17.  python file .py 
     run the file we have 
     python  filename.py 

18. Editor  + Debugger + Auto Complete + linter + +++++++ 

19.  dir()


--------------------------------------------------------------------------------------
# Day-2 
Python introduction 
Syntaxes 
this is comment in python #
""" 
    docstring 
""" 
variables 
DataTypes (int, float, other types of varaibles dict, list, tuple, set )
python strings booleans 
If Elif Else 
For 
While 
Range 
using built in functions 
----------------------------------------------------------------------------------------

Working with files P:


open();
python functions cann be called in two ways 
a) Named Parameters 
b) Positional Parameter 

open

##### 
file = open(file="d:/airports.csv" , mode="rt" , encoding="utf-8")
line = file.readline()
while line: 
    line = file.readline()
    print(line)
#####

####################################################################################
Writing functions in python :- 

def function_name()

# using the functions to read file 


===================================================================================
# Assignment ~ 1 ~ 
You have the airports.csv 
using the python you will need  to read all the airport and seperate it and give me the count 
of the airports of each type 
Step 1 : 
Create function that accepts a file name 
Step 2 : 
Read the file 
Step 3 : 
WHile Each line : 
    Read the line and 
    split the row by , 
Step 4 : 
    Compare the Value of the aiport_type 
Step 5: 
    Add it to the required array 
Step 6: 
    Proint the the counts 

import sys 
sys.argv[0] // the prigram name 
sys.argv[1] // what ever your parameter 


#####################################################################################################
how to writing functions 
how to pass parameters to functions default params , keyword params , varargs params , function to functiojn 
how does a function retunr a function 
function return types anything function , number

Function Patching (Monkey patches)
Too much Flexibility in the system makes it more dangerous 


##########################################
1.  pip install virtualenv 
2.  virtualenv  projecta
3.  virtualenv  projectb 
The above 2, 3 create 2 different folders or projects :- 

what we do is we go in the first project 
4.  cd projecta\Scripts
    the scripts folder contains a activate.bat which activates this environment 
    Telling the Path that when someone does pip install your LIB


How to create virtual evironments :  
1. To create  virtualenv you will need the virutalenv tool : 
    pip install virtualenv 

2. using virtual env either a existsing project can be virtualized or 
    a new project can be created 
    virtualenv <yourproject> (Whether existing or not matter)
        if does not exist it will create a new 
        if exist it will augment the existing 

    virtualenv projecta 
    virtualenv projectb 

3.  there are two different project and one root python installation however we want each 
    project to act individually
        cd projecta\Scripts 
        activate 
    This activate or fools the python that its Lib directory is projecta\Lib 
    when i do pip install request 
    pip install lxml 
    this isntalls only in the Lib of the project and while compiling and running only refers this Lib 
    when is say pip lsit which is activate projecta i will see only libraries for project A 
    you can verify 
    switch to project b : 
    in another prompt 
    cd projectb\Scripts
    activate now b gets activate 
    pip list andh check the packages that you installed in a are not visible here 
    

try : is to try single or set of statements 
except : multiple blocks to define thtat a exception has occured and when excption occurs   
        it will enter in the matching except block 
else : optional but if there are no exception then the else blcok wil get called 
finally : whether there is exception or no exception it will steil get called 

how to raise an exception we raise and exception using raise : 

# can i write my own exceptions # yes but for that for a day to write classes 

# modules 
Every python file module 
a) modules  (Is anhy single file)
b) package (a directory with other python module imported as single library collection modules)

Every single python is module 
its not only operations that get imported byt thestatemt also get excuted


what is module ?
Any python file is module 

how can i import a module 


a special file __init__.py































how is a module different from a package 
1. A module is different from a package because 
a module is just file and only covers what the file exhibits 

2. A package is very different because the structure is not a file its folder with special file inside it 
    __init__.py 
    the above is the actually the package however for visibility purpose the name of the folder acts as the 
    package : 
    Now a package is collection of modules : which means many python libriary files when bundled togerther 
    and bound in the __init__.py to group as one named collection then we call it as a package 

3. in our case we want to create a package named parsers 
    create a new folder parsers 
    however its manadatory to note that a package is package only and only and only as per python 
    if it has  a __init__.py

4. What am i supposed to do in the __init__.py aggregate the collection of modules in  your folder 
    csvparser.py
    xmlparser.py
    jsonparser.py






Step 1 : Create a folder 
Step 2 : __init__.py 
Step 3 : create other py files that you wish to have your functions
Step 4 ; import them in the __init__.py 
Step 5 : now import your package anywhere and call the funtions that you have imported 
            in the __init__.py

            







|----- parsers 
           |--- __init__.py  (from .m1 import * ) (from .m2 import *) from (.m3 import *)
                             (from .writer import *)
           |--- m1.py  // p1 
           |--- m2.py  // p2 
           |--- m3.py  // p3
           |--- writers 
                  |----__init__.py  (from .demowriter import *  from .dummyhelper import *)
                  |--- demowriter.py  (Module) //x1  , x2 
                  |--- dummyhelper.py (Module)  // y1 , y2 




parsers.p1
parsers.p2
parsers.p3
























    


















































































