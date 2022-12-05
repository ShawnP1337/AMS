import glob
import os

path = "C:\\Users\\awyat049\\OneDrive\\Documents\\Coding\\2022_11_26_Cleaned_Twitter_Data\\inflation"
os.chdir(path)

f = open("inflationfilelist.csv", "w")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

for i in all_filenames:
    f.write('"' + i + '"\n')

f.close()