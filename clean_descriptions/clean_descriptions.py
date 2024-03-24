import json, re, time, pyperclip

######################################
regex1=	{
		"note": "Fix Carriage Returns",
		"regex": "<br>",
		"replace": "</p><p>"
	}
regex2= {	
		"note": "Fix Elipsis...",
		"regex": "(\.\s?){3,}",
		"replace": "… "
	}
fixes = {             
    "1": regex1,
    "2": regex2}
#######################################
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
trim_synopsis = int(round(0.1*len(synopsis),-1))
print("Processing text: ", len(synopsis))
print("Triming to 10%, New Length: ", trim_synopsis)
print("Trim is ", type(trim_synopsis))
print("1 is ", type(1))
print("Syn is ", type(synopsis))
print("New Text ","\n************************\n", synopsis[0:trim_synopsis],"\n************************")

print("Cleaning")
clean_synopsis = clean_text(synopsis)
print("Cleaned")
pyperclip.copy(clean_synopsis)
