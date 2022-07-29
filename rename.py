############################
#
#
#
#
#
############################

############################
#           Notes
#os.path.abspath('spam.png')  <-- converts to absolute Path (video 30)
#
############################

# ********* Sample Data ********* #
contents_test = '''['10_German.srt', '11_Greek.srt', '12_Spanish.srt', '13_Spanish.srt', '14_Spanish.srt', '15_Spanish.srt', '16_baq.srt', '17_Finnish.srt', '18_fil.srt', '19_French.srt', '20_French.srt', '21_French.srt', '22_glg.srt', '23_Hebrew.srt', '24_hrv.srt', '25_Hungarian.srt', '26_Indonesian.srt', '27_Italian.srt', '28_Japanese.srt', '29_Korean.srt', '2_English.srt', '30_may.srt', '31_Bokmal.srt', '32_Dutch.srt', '33_Polish.srt', '34_Portuguese.srt', '35_Portuguese.srt', '36_Portuguese.srt', '37_Portuguese.srt', '38_Romanian.srt', '39_Russian.srt', '3_English.srt', '40_Swedish.srt', '41_Thai.srt', '42_Turkish.srt', '43_ukr.srt', '44_Vietnamese.srt', '45_Chinese.srt', '46_Chinese.srt', '4_Arabic.srt', '5_cat.srt', '6_Czech.srt', '7_Danish.srt', '8_German.srt', '9_German.srt']'''
# ********* Sample Data ********* #

# ********* Sample Data ********* #
Path = r'R:\Videos\Bebes.Kids.1992.1080p.BluRay.x265-RARBG'
# ********* Sample Data ********* #


import os, pyperclip, re, time

print('Finding Sub folder')
print('Locating Current Directory')
current = os.getcwd()
print('Getting contents of Clipboard')
#Path = pyperclip.paste()
print("**** Pause %s seconds ****" % ('One'))
time.sleep(.2)


if os.path.isabs(Path):   # Testing if path is an absolute path
    print('Contrats we have an absolute path')
    print('----> ' + Path)
else:
    print("We didn't copy a path properly")
    time.sleep(4)


assert os.path.exists(Path)
print('Path is real')
time.sleep(.2)

if os.path.isdir(Path):
    print('The path is a directory')
    print('----> ' + Path)
else:
    Path = os.path.dirname(Path)
    print('The path is not a directory')
    time.sleep(5)
    print('----> ' + Path)

print('Checking for Subs Folder')
SubPath = Path + r'\Subs'
print('SubPath -->' + SubPath)
Subs_Is_Present = os.path.exists(SubPath)

print('Checking English Sub file')
print('List of contents in Sub folder')
#print(os.listdir(SubPath))
#folder_Contents = os.listdir(SubPath)

### Test Data ###
print('******* Contents *******')
print(contents_test)
print('******* Contents *******')
### Test Data ###
print()
print()
print()
print()

##########   Notes for Reference   ##########
# good_filenames = [name for name in filenames if name.startswith("GSE") and name.endswith("_series_matrix.txt")]
##########   Notes for Reference   ##########
# https://stackoverflow.com/questions/27302238/regex-in-python-to-match-all-the-files-in-a-folder
##########   Notes for Reference   ##########

print('List of English in subfolder')
englishRegex = re.compile(r'\d{1,2}_[E|e]nglish.srt', flags=re.IGNORECASE)
matched = englishRegex.findall(contents_test)


print('******* Contents *******')
print(matched)
print('******* Contents *******')

print()
print()
print()
print()

print('''****************************
Status:
Currently in      :   %s
Clipboard contains:   %s
Clipboard is Path?:   %s
Dir Contains Sub:     %s
folder_Contents type: %s
****************************''' % (current,  Path, os.path.isabs(Path), Subs_Is_Present, type(matched)))


print('End')
