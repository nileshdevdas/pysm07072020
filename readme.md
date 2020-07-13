# day 1 
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
















































































































