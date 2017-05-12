import argparse, os

count = 0
for filename in os.listdir('.'):
	if filename.endswith('.sav'):
		os.rename(filename, "Save{:04X}.sav".format(count))
		count += 1
