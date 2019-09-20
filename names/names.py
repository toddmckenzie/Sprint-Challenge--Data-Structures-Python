import time
from lru_cache import LRUCache
from doubly_linked_list import DoublyLinkedList


start_time = time.time()

duplicates = LRUCache(20001)

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
for name in names_1:
    if duplicates.get(name) == None:
        duplicates.set(name, 1)
    else:
        values = duplicates.get(name)
        duplicates.set(name, (values + 1))

f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
for name in names_2:
    if duplicates.get(name) == None:
        duplicates.set(name, 1)
    else:
        values = duplicates.get(name)
        duplicates.set(name, (values + 1))
f.close()


# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


dupsList = []

for k,v in duplicates.storage.items():
    if k in dupsList:
        print(k)
    else:
        dupsList.append(k)

end_time = time.time()

print(f"{duplicates.duplicate_names}") #return number of names that are duplicates...
print(f"{duplicates.valueGreater()}") #returns the names with value greater than one.

# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")



# ***!Important!*** If you are running this using PowerShell by clicking on the green play button, you will get an error that `names1.txt` is not found.  To resolve this, run it, get the error, then `cd` into the `names` directory in the `python` terminal that opens in VSCode.

# Navigate into the `names` directory. Here you will find two text files containing 10,000 names each, along with a program `names.py` that compares the two files and prints out duplicate name entries. Try running the code with `python3 names.py`. Be patient because it might take a while: approximately six seconds on my laptop. What is the runtime complexity of this code?

# Six seconds is an eternity so you've been tasked with speeding up the code. Can you get the runtime to under a second? Under one hundredth of a second?

# *You may not use the built in Python list or set for this problem*

# (Hint: You might try importing a data structure you built during the week)