import pyqrcode
from PIL import Image
import qrtools
def fixtuples((x,y,z)):
 if ((x + y + z) % 2) > 0:
  if x < 255:
   return (x+1, y, z)
  else:
   return (x-1,y,z)
 else:
  return (x,y,z)

def addtuples((x,y,z)):
 if x < 255:
  return (x+1,y,z)
 else:
  return (x-1,y,z)
print('           ____  _                 _                                 ')
print('          / ___|(_)_ __ ___  _   _| | __ _  ___ _ __ _   _ _ __ ___  ')
print("          \___ \| | '_ ` _ \| | | | |/ _` |/ __| '__| | | | '_ ` _ \ ")
print('           ___) | | | | | | | |_| | | (_| | (__| |  | |_| | | | | | |')
print('          |____/|_|_| |_| |_|\__,_|_|\__,_|\___|_|   \__,_|_| |_| |_|')
print('Welcome to Simulacrum!')
print('This program allows for the storage and retrieval of a signed tx from a given image.')
print('-----------------------------------')
print('Do you want to:\nConceal a signed tx? (Press "a")\nReveal a signed tx? (Press "b")')
print('-----------------------------------')
while True:
 user_input = raw_input('')
 if user_input == 'a' or user_input == 'b':
  break 
 else:
  print('Your input could not be understood.')

if user_input == 'a':
 while True:

  signed = raw_input('Please input your signed tx:\n')
  confirm = raw_input('Confirm that your signed tx is "' + signed + '"?[y/n]\n')
  if confirm == 'y':
   break
   
 
 print('Generating QR...')
 QR = pyqrcode.create(signed)
 QR.png('qrgenerated.png', scale=1)
 print('Generated!')

 QRt = Image.open('qrgenerated.png')
 list_qr_points = list(QRt.getdata())
 newlist = list()
 for i in range(0,len(list_qr_points)):
  if list_qr_points[i] == 255:
   newlist.append(0)
  else:
   newlist.append(1)

 
 image_to_conceal = Image.open('[file name + extension]')
 width, height = image_to_conceal.size
 conceal_points = list(image_to_conceal.getdata())
 cut_image = conceal_points[:14641]
 balanced_image = list()
 for i in cut_image:
  balanced_image.append(fixtuples(i))

 image_with_qr = list()

 for i in range(0,14641):
  if newlist[i] == 1:
   image_with_qr.append(balanced_image[i])
  else:
   image_with_qr.append(addtuples(balanced_image[i]))

 completed_image = image_with_qr + conceal_points[len(newlist):]
 hb = Image.new('RGB', (width,height))
 hb.putdata(completed_image)
 hb.save('output.png')
 print('Output ready!')
 
if user_input == 'b':
 picture = raw_input("Input the name of the image you'd like to extract the key from:\n")
 honeybadger = Image.open(picture)
 honeybadger_read = list(honeybadger.getdata())
 honeybadger_getpoints = honeybadger_read[:14641]

 combine = map(sum, honeybadger_getpoints)
 print(combine)
 newconstruct = list()
 for i in range(0,14641):
  if (combine[i] % 2) == 0:
   newconstruct.append((0,0,0))
  else:
   newconstruct.append((255,255,255))

 QRnew = Image.new('RGB', (121,121))
 QRnew.putdata(newconstruct)
 QRnew = QRnew.resize((242,242), Image.ANTIALIAS)
 QRnew.save('trueoutput.jpg') 
 print('Key extracted!')
 qra = qrtools.QR()
 qra.decode("trueoutput.jpg")
 print(qra.data)
 
 
 
 
 

