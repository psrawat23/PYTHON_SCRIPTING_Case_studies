import pkgutil
import inspect
import re
import sys
from collections import defaultdict

#path variable
path=sys.argv[1]
#appending path in sys.path
sys.path.append(path)
all_my_sub_classes={}
#importing all files from the given directory
for (module_loader, name, ispkg) in pkgutil.iter_modules([path]):
    exec('import ' + name)
    #storing all classess from each file into clsmembers 
    clsmembers = inspect.getmembers(sys.modules[name], inspect.isclass)
    #Storing all classess and subclasses of given directory in all_my_sub_classes={} dictionary
    for i in clsmembers:
        all_my_sub_classes[i[1]] = {cls for cls in i[1].__subclasses__()}    

all_my_derived_class = defaultdict(dict)

#Assigning Dictionary Key as Base class and Value as list of Derived class
for parent,subclass in all_my_sub_classes.items():
    for derived in subclass:
        all_my_derived_class.setdefault(derived, []).append(parent)

#Printing the Base class and derived class along with file name (seprated by regular expression)        
for base,derived in all_my_derived_class.items():
    #Using regular expression to separate file name nad class name
    pattern=re.search('\'(\w+)\.(\w+)\'',str(base))
    print(pattern.group(2),"["+pattern.group(1)+".py]")
    #printing all derived classess of base class
    for cls_file in derived:
        pattern=re.search('\'(\w+)\.(\w+)\'',str(cls_file))
        print("\t",pattern.group(2),"["+pattern.group(1)+".py]")
