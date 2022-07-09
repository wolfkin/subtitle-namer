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

contents_test = '''['10_German.srt', '11_Greek.srt', '12_Spanish.srt', '13_Spanish.srt', '14_Spanish.srt', '15_Spanish.srt', '16_baq.srt', '17_Finnish.srt', '18_fil.srt', '19_French.srt', '20_French.srt', '21_French.srt', '22_glg.srt', '23_Hebrew.srt', '24_hrv.srt', '25_Hungarian.srt', '26_Indonesian.srt', '27_Italian.srt', '28_Japanese.srt', '29_Korean.srt', '2_English.srt', '30_may.srt', '31_Bokmal.srt', '32_Dutch.srt', '33_Polish.srt', '34_Portuguese.srt', '35_Portuguese.srt', '36_Portuguese.srt', '37_Portuguese.srt', '38_Romanian.srt', '39_Russian.srt', '3_English.srt', '40_Swedish.srt', '41_Thai.srt', '42_Turkish.srt', '43_ukr.srt', '44_Vietnamese.srt', '45_Chinese.srt', '46_Chinese.srt', '4_Arabic.srt', '5_cat.srt', '6_Czech.srt', '7_Danish.srt', '8_German.srt', '9_German.srt']'''


import os, pyperclip, re

print('Finding Sub folder')
print('Locating Current Directory')
current = os.getcwd()
print('Checking Clipboard')
CopyPath = pyperclip.paste()
CopyPath = r'R:\Videos\The.Sea.Beast.2022.1080p.WEBRip.x265-RARBG\The.Sea.Beast.2022.1080p.WEBRip.x265-RARBG.mp4'


isPathAbs = os.path.isabs(CopyPath)
if isPathAbs:
    print('Contrats we have a good path')
else:
    print("We didn't copy a path properly")

isPathReal = os.path.exists(CopyPath)
print('The path is %s' % (isPathReal))

print('Checking for Subs Folder')
DirPath = os.path.dirname(CopyPath)
SubPath = DirPath + '\\Subs'
Subs_Is_Present = os.path.exists(SubPath)

print('Checking English Sub file')
print('List of contents in Sub folder')
print(os.listdir(SubPath))
folder_Contents = os.listdir(SubPath)


print('List of English in subfolder')
englishRegex = re.compile(r'\d\d')
matched = englishRegex.findall(contents_test)
print(matched)

print('''****************************
Status:
Currently in      : %s
Clipboard contains: %s
Clipboard is Path?: %s
Dir Path is:        %s
Dir Contains Sub:   %s
****************************''' % (current,  CopyPath, isPathAbs, DirPath, Subs_Is_Present))


print('End')
