
import re
import dircache
import datetime
import pyexiv2

PATH = '/media/docs/Images/adjusted2/'
filelst = dircache.listdir(PATH)
regex = re.compile("\w+")

for i in range (0, len(filelst)):
	filename = filelst[i]
	filename = regex.findall(filename)
	filename.pop()
	
	metadata = pyexiv2.ImageMetadata(PATH + filelst[i])
	metadata.read()
	
	key1 = 'Exif.Image.DateTime'
	key2 = 'Exif.Photo.DateTimeOriginal'
	key3 = 'Exif.Photo.DateTimeDigitized'
	
	newdate = datetime.datetime(int(filename[0]), int(filename[1]), int(filename[2]), int(filename[3]), int(filename[4]), int(filename[5]))
	metadata.__setitem__(key1, newdate)
	metadata.__setitem__(key2, newdate)
	metadata.__setitem__(key3, newdate)
	
	metadata.write()
	
