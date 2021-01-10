    # EXIF Date Changer to modify EXIF dates using the filename
    # Copyright (C) 2021 Afzal Najam.

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
import os
import datetime
import pyexiv2
import click

folder = ""

def change_date(date, folder):
  filelst = os.listdir(folder)

  for i in range (0, len(filelst)):
    if "DS_Store" in filelst[i]:
      continue
    fullpath = f'{folder}/{filelst[i]}'
    print("Processing %s" % fullpath)
    image = pyexiv2.Image(fullpath)
    # data = image.read_exif()
    # print(data)
    image.modify_exif({'Exif.Image.DateTime': f'{date}'})
    image.modify_exif({'Exif.Image.DateTimeOriginal': f'{date}'})
    # image.modify_exif({'Exif.Image.DateTimeDigitized': f'{date}'})
    image.close()

@click.command()
@click.option('--folder', prompt='Folder name', help='The folder containing image files.')
@click.option('--date', prompt='New date', help='The new date for the EXIF data.')
def start(date, folder):
  try:
    datetime.datetime.strptime(date, '%Y:%m:%d %H:%M:%S')
  except ValueError:
    print("Incorrect date format, should be YYYY:MM:DD HH:mm:ss")
    return

  change_date(date, folder)


if __name__ == '__main__':
  start()
