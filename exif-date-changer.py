    # EXIF Date Changer to modify EXIF dates using the filename
    # Copyright (C) 2011 Afzal Najam.

    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.

    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.

    # You should have received a copy of the GNU General Public License
    # along with this program.  If not, see <http://www.gnu.org/licenses/>. 


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
	
