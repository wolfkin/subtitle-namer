import json, re, time, pyperclip

#######################################
###  Cleaning Using variables      ####
###  Pt 1: Variables               ####
#######################################
##regex1=	{
##		"note": "Fix Carriage Returns",
##		"regex": "<br>",
##		"replace": "</p><p>"
##	}
##regex2= {	
##		"note": "Fix Elipsis...",
##		"regex": "(\.\s?){3,}",
##		"replace": "… "
##	}
##fixes = {             
##    "1": regex1,
##    "2": regex2}
#######################################
###  Cleaning Using variables      ####
###  Pt 2: Function                ####
#######################################
##def clean_text(dirty):
##    print("Lefty")
##    for x in fixes.values():
##        print("Preparing: ", x["note"])
##        clean = re.sub(x["regex"], x["replace"], dirty)
##        dirty = clean
##        time.sleep(.3)
##    return clean
#######################################

#######################################
###  Cleaning Using JSON Files     ####
#######################################
json_file = open('regex.json',)

fixes = json.load(json_file)
print("Fixes Type is: ", type(fixes))               #Test Code, ToBeDeleted
print("Fixes Values is: /n", fixes.values())        #Test Code, ToBeDeleted
print()                                             #Test Code, ToBeDeleted
print("Fixes Keys are: ", fixes.keys())             #Test Code, ToBeDeleted
print("Fixes Value for Notes: ", fixes.get("note")) #Test Code, ToBeDeleted

def clean_text(dirty):
    print("Lefty")
    for x in fixes.values():
        print("Preparing: ", x["note"])
        clean = re.sub(x["regex"], x["replace"], dirty)
        dirty = clean
        time.sleep(.3)
    return clean
#######################################


synopsis = pyperclip.paste()
trim_synopsis = int(round(0.1*len(synopsis),-1))  # 10% of synopsis for a preview
print("Processing text: ", len(synopsis))
print("Triming to 10%, New Length: ", trim_synopsis)
##print("Trim is ", type(trim_synopsis))  #Test Code, ToBeDeleted
##print("1 is ", type(1))                 #Test Code, ToBeDeleted
##print("Syn is ", type(synopsis))        #Test Code, ToBeDeleted
print("New Text ","\n************************\n", synopsis[0:trim_synopsis],"\n************************")

print("Cleaning")
clean_synopsis = clean_text(synopsis)
print("Cleaned")
pyperclip.copy(clean_synopsis)
