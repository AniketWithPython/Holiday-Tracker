#Calendarific™ API
#Copyright © 2022 HATCHSQUARE Technologies LLC, All rights reserved. All other domain, brand information and trademarks are the registered trademarks of their respective owners.

import requests
from tkinter import *
from datetime import datetime
import json

year,month,day=datetime.now().year,datetime.now().month,datetime.now().day
#year,month,day=2022,1,26

try:
    response=requests.get("https://calendarific.com/api/v2/holidays?&api_key=<redacted>&country=IN&year={}&month={}&day={}".format(year,month,day))
    #response=requests.get("https://calendarific.com/api/v2/holidays?&api_key=<redacted>&country=IN&year=2022&month=1&day=26")
    code=response.status_code
    data=response.content.decode()
    data=json.loads(data)
    yay=[]
    for i in data["response"]["holidays"]:
        yay.append(i["name"])
    yay=", ".join(yay)
    if len(yay)==0:
        yay='<no holiday>'
except:
    yay='<Unexpected Error>'
    try:
        code
    except NameError:
        code='NA'

date='/'.join([str(day),str(month),str(year)])
app=Tk()
photo=PhotoImage(data=b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00@\x00\x00\x00@\x08\x02\x00\x00\x00%\x0b\xe6\x89\x00\x00\x00\x01sRGB\x00\xae\xce\x1c\xe9\x00\x00\x00\x04gAMA\x00\x00\xb1\x8f\x0b\xfca\x05\x00\x00\x00\tpHYs\x00\x00\x0e\xc3\x00\x00\x0e\xc3\x01\xc7o\xa8d\x00\x00)\xf1IDAThCeywT\x9by\x92-g\xcf\xdb\xd97\xf3vB\xf7t\xcfvv\xbb\xbb\xdd\xc19g\x82\x01\x93l\x93\x931\x98\x8c\xc1\x18\x8c\xc9Y\xe4\x9c\x11A\x02I\x80\x84\x02B\xa0\x9cs\xce\x89\x9c\x8c\tN\xdd\x9eNo\xf7\xffW\x9f\x99\xd9\xd9\xddwN\x9d\xef|\x08\xa1\xef\xde\xfa\xd5\xad\xba%<\x1c\x924\xb74uI\x96\xbd$\xcbXU\xa6\xad\xca37\x14\xb9O\xb5\x85\x1b\xea\xc7\x8b\x92\xecMA\xb6\x95\xece\xa7\\\xdd\xe0\x06\xacsn\xae0}\xf6e\xf7^\x1a\x0b\x9e\xc9+\xb7\xf8\xc5\xb6\xd1 E\xc7U\xeb\xe4\xdd%^\x95K\xde\xb9\xa8Ao:\xc8\xcf\xd7\xb8\xfb\xeb\xfc\xfd5\xe1\xf3\r\x1er\xb3\xce\x85\x9b\xbdM$\xf6\xb7D\xff\x19{\x9b\x82\xfd-\x88\x7f\xbc\xf2|C\x00\xef\x84\xeb\xcbu\xc1\xebU\xf6k\xd7\xd4\x9e\t\xbdc\xec\xffa\t>\x93\xfd|\x8d\x7f\x10\xf0\xdb\xbf\x7f,\xbc_\xe0\xe1\x16\xa59D\xc9Nq\xc6\xb2$mY\x96\xb8"K[Sd\xad*3\xd6\xa4)\x0e\xee\xbd%A\x86\x8d\x11\xb4%\xb9\xbb)\x89\xde\x96\xc4\xec(\xee\xfdh+|\xb3P\xbb\xad\xae\xde\x10\x15Y\xb1\xc1\xfc\xdaS\xfc\xc6svR\xda\x8a\xb4yI;\xb8\xe7\xa4\xc13\xe0\x01\xf0\xd1\xbb\x1b\x08\x93\xb7@\x0f\x10\xff7\x02\xbb\x00\xe2\xe0\xf5\x8d\x7f\xbc\x08\x01\xf8\xbe_\xe3,\xcb\x1a\x8d\xe4$\x1d\xfe\xaez$B:\x10\xf5\xe3"\x03>\x07~\xf57\x1ao\xa9\x1e\xd0\xf0X\x92e-J\xd3\x00\xbdK\x90\xb8*\x8a]\x14\'\xae)2V\xa4\x89\x0b\x9c\xf0\x15A\x1a\x9c\xc6\x86\xf2\xc1Ks\xc1\xae!\xfd\x8d=\xefWw\xd5\xbfo4\xfd\xb8\xd8\xb2\xafo\xdc\x10VX\'\xc2\x04\rg\xf8\xb5gXu\xe7VXE\xab\x9a\xfe\xe7\xee\xb9\xbf?\xe0 8\xf0\xe0\xbfs\x80\x9b\xff\xc6\xe1\xff\x0fx\xc3\xabu\xd6\xb6e\xcc6\x977\xdb\x1a\xc0j\xf6e\xd4\\\x9a\xca?k \x17>_\x15\xbez\x8b\x1b>\xf6 Aoo\x80\x80(qE\x98\xb8"JX\xe2\xdf^\xe6\x85\xae\x08bV\x85\t\xcb\xbc\xdb\xf69\xaf-u\xee\xb6\xaed\xc7\\\xfc\xd2^\xb0o~\xf4\xe3r\xf5\xcf+\r\xffw\xbd\x11N`W]\xb3\xc9\xce7\x8f\xdf\xe6\xa2\xce\x88jN(jO\x89;\xbdVx\xa8}7u\x7f\xe5\x1f\x0fx[9\x82\xff\x91\xe3\xff\x11/\x9e\x8a\xff\xf3\xfe\xd5:g\xcb\x886\xcd\x17Ip\t\xfc\xa1\x18q_8\xb9\xecRW\xcc!\xfc\xa3\xb3?,L\xefn"\'\xf0\x9f\x1f\x8e\x10\xd8\x12y,\nb\x97\xb8w\x96\xb8\xb7\x90\xe0\x87\xae\x8a\xa2WD\xb1\xc0d\x95\x17\xbdm\xac\xd8\xb3\xa0^\xd8\xca\xe1\x04^\xdbK~\xddl\xf9e\xb3\xe5\xd7\xcd\x86W\x8e\xeamY\xe9:\xfb\x81\r\x1f*\xa8;-\xa8<%G]P\xb6\\R\xf7\x07?\xd5u\xee\xad\xf2v6\xf8\x10P$\xbb[\xbc\xbf\x05\xd0\xf8/\xa0\x0f\xe2o/n\x03\x01\x04\xca\x8b-\xce\x96~\xd0\xc9*R\x8c\'\xcdv\x05r\xd0\xd1\x82\xde\xb0\xe9\x8a\xab\x1d\xf1\x9f\x8d\xa5|\xa7\xc2\xa6\xbf^G\x94\x83@\x87\x9b\r\x11\xf2\x88M\x81\xc7*?\x1c\xa0/\xb2\xc3\xd7\xf8q\xcf\x94i\xcf49\x1b\xda\xf4-u\xda\xb6!\xf7\xa5\xab\xfd\x95\xb3\xf1{w\x15\xa0\xffq\xa9\xee\x97\xcd\xb6\x7f\xdfl\xf8i\xa9\xf2\xb5\xa5|[\x9c\xb3BO0\x8d\xdfT\xb5^\xe6\x94\x1d\xe3\x94\x9e\x90U\x9f\xd6t\\\xd0\x0c\x87<7\r\xfd\xb4<\xfb\xfd\xfa<\xa8\xf9m\xf0_\xae\x1d\x08\x14\xe2m\x01\xbcE\x7f\xf0\xca\x8bM\xd1[\x9d\xf0^n\xb0^\xb9\'\x9c\xf3\x85j|,\xb3\xc3\x975\x18\xc6\xe8\x8b\x9ai\xbf5\xd3\xe0O.\xf5\xc6\xa4\x1d\xc7\xe5\x9c~\xb3\xc2<\xf8\xa8\x17\x1b\x92\x83?\x84\xf0\xd8\x14%nI\xd3\x9f\xaa\x1f\xec\x1a\x1e=w\x94\xbd^\xa8z\xbdP\x01\xd5\xf2\xd3R\xf3\x9b\x85\xae7\xcb\xb5\xbf\xac\xd7\xfc\xb2Q\x0f\xe9GN`\xbd\xe6\xaf\x0b\xe5\xcfUe+\xcc\xe4\xc5\xa9\x08\x17\xe6\x86\xa1\xe7\xb2\xbc\xf5\x9c\x08uR\xdaxZ\xd5yA\xd1v\xd1\x86\x0fw\x13\x13\xd7\x05\xe5;\xba\xde\x976\xdc\x0f\xcbS\xdf\xaf\xcd\xbc\\\x9b{\xb51\xffr\x15\xa1\xf4r\x83\xf3j\x8d\xf7r\x1d\xc8\xf0\x00\x07\xa4\xf3\xf92s\xdf6\xae\x99N\x93\x0fE\x91\xca\xae\xcd\xb5\x04\xb0\x06"\xa6\x9bC\'\xab\x83\'*\xfc\xf1\x85\xde\xd8\xcc\x93\xc3IG\x9e\x9b\x07_\xac )@\xfe\xe4-\x7f\x84\xc0\x0f\xf6\xd2\xd7\xce\xaa\xef]5\xdf/\xd4\xbeY\xae\xfbe\xa3\xf1\x97\xb5\x06\x88\x1f\x97\x1a\xde\xb8\x9a~\\\xaa\xfde\r\xf5\xebf\xd3\xcfkM\x7f]\xa9\xffi\xa5f\xdf\x98\xb7\xcc\xcd]\xa2\'J;.\xb2\xab\xbfv\x8f\x05\xafM\x87o\xd1\xa2\xd7\xa9QK\xe4\xb0%j\xe8"\xe5\x8e\x8br\xdb=q\xcb9y\xcb\x82\r\xb6\xe0\xc2\xac\x93q\x0ej\x96\x8d\x9c\xee\xa4?t\xcd\xe6\xae\x0bk\xb6\xd4\xad\xafm#o\xdc\xb8\x1f\x97&~X\xa2n(\xdaU\xe3\xf7\xa4\xc3A\xf3\xcd\x01C\xd9\xc7\xd9\x1dw\xc8\xf5\xbe\x84r\xbf\x81\x07\x97G\xf3| H\x05>\x93\x99\'\xf5\xe4\xfc\xd7\x9b\xac\xffJ\x00R\xe0\x01\xc8~\\G\xc0\xc1\r\x00\xfdi\xad\xf6\xa7\xa5\xda\xe7\xa6\x82g\xda\x92g\xfa\xf2\x17\xb6\xd2\xef\x17J\x7fZA\xfdu\xb1\xe6\xcdb\xf9\xf7\xceB\x18\x02\xf6\x99\x14\xcb\xc4mU\xbf\xf7")ry:~}.i\x9b\x95\xbaLIX\x99\x89Y\xa6E\xae\xccF\xbb\xa9w\x1c\x13\x81\x8b\x13\x81n\x82\x9f\x9b\x10\xb88}{\x95\x1c\xba0\x15\xb2L\nu\x11\x82m\xe3\xfe\xd61?\'.\xd4\x8e\x0b_\x98\x88\xb6O&:\xf0\xb1\x8a\x81`V\x8b\x17\xae\xe0<\xbd\xd6\x97\xd9\x12L\xae\xf2\xc6?\xf1\x1b\xc9\xf1m\x8c;\xd5\x9b\xe5\x89\x7frc\xb6\xe8\x1a\r\xe5\xffr\x81\xfab\x13)<$\xb6\xe048\x1eou\t\xb5\xd1\xfc\xd7\xd5\xaa7\x0b\xd5\xfb\xf6\xe2\x1ds.\x10\xf8\xc1V\xfb\xc2R\xf7\xc2R\xf6\xd2P\xf8B\x97\xbf\xad\xcc\xd8\x10\xdf\xdf\x95\xa5/1\x93]\xf4\xa4MN\xea\x1e;s\x87\x9b\xbd\xc5\xc9^\x9eM]a\xa4-R\x13\x1c\x93a\x16| \x84\x01\xe7g\xc3\xdf\x04\xf4N\xdc\x8d\xe5) \x13\xbcJ\x8e\\\xa6\x84\xafP#\x81\x03\x1c\x94m<\xc0<|\xc3\x82\xf6\x95\xd4\x9fS\xa1.\n[.\xc8:\xfd\xa6\x8b\xcf5\xc7\x1c\xa6Vx\xd1k\xbcI\xc5>mI\xe7\x9a\xef\x9ekM\xba\xd2\x93|}8\xe7\xf2l\x85\'\xe9\xc9\xd9m\xed\x08\xf4\xd9\xbf\xa7\x1f9\n\x0f$\xfd\x8b\xa87\xae\x9a\x97\x8e\xa2\xe7\xa6G/\x8d\x8f^\x99s\xf7M\x05O\x95Ek\xd2Bd\x90\xcd\xc5\xd9hQ:R\x80\n\x1f\xa0\x9d\x08q\xd0Rv\xc4\x8fv%y\xbb\xfc\';\xbc\xe2U\xd6\xa3%f\xba\x8b\x9e\xbc@\x89\xb7\x11B\x8cc\xfe\xfa\x11\x1f\xc3\xa8\xb7a\xf0\xba\r\xebe\xc1\xf8\x1bF\xfc\xcc\xe3\xa1NJ\xdc\xe2\xcc=\x175~u&q\x8d\x9e\xb4H\x8c\xb6\x8e\x87\xd8p\xc1\xea^/j\xf6\x97\xea&?N\x95WW\xc2\xd7\x03)\xdf\xce\xa1\xbc!z\xee\x1f\xcd\xf7\xff<\xcb\xf7H\xaa\xe7\x17\xb97\xbfjI<A-\xbeL,8e\x9a\xa9\xf8~\x8d\xf5\xb7\x13\x00\xfd\xc0$\x86\x1c\xef\xe8\xb2!\xc1k\x92\x84%v\xcc\x02;\xda1\x17\xa3\x98\xb8\xc5\x1d\xbd\x05\xcd\x983\x1c:\xdf\xe7\xcf\xef\x0b\x90\x8d\x06\x02\xf4un\xf6si\xc9\x8e\xb8hOZ\xbe+\xab\\\xe1\x14\xaf\xb1\x1e\xbbgS\xec\xd3\t\x0bS1v|\x88\x1d\xebgA\xfbX\xd0^\xe6\xa1\x9b\xa6\x11o\x80h\xc1\xdf2\xe0BmS\t\xe6\xa9\x18\xd3d\x94\x9d\x96`\xa3\xdeuLD\xe9G\x02\r\x98 \xeb\xd8mc_\x00\xee\xfe\xe1\x81\xe8\xcf\xbac\xbe%\x15^\xe6\xb7\xddd5\xfbO\x94x\x96\xdf9\x1eq\xe6\xa3\xa8\xd3G\xb2\xfc\xbeE?\xb8F/\xf3"\xe6\x9e\xe4\x0f&\xbf\xda\xe4\xfc\xe3\x04\x80\x80\x83\x9d`\xa2\xdd2N\x07+\t\xbeb\x8c\x17\xb3\xff:\xbd\xfb:\xa5\xd9\x8b\xd2\xecCm\xf6g\xf5\x06\xf3Gn\x19\x89q\x00}_^\xb1/\xab\xda\x11\x97\xedJ\xca\x9f\xc9j\xb7\xe4uk\x82\xcae\xf6#\x1b-\xd9F\x8c5`\x02\x8cho#\xda\xd38\xe0e\x1a\xf2\xb1`\x02\\\xc4(5&X;\x1e\xa6\x1a\x0f\xd7M$\xe8\xf0q*\\\x8cr,\xcc0\x15e\x9e\x88\xb2\x13\xc2L\xb8\xdb0\n\xdd\x840n\xcd\x95\xa6;\xef\xa3\xe3\xbe\x9d||i\xbe\xdek\x1e\xe5\xc9l\x08nI\xf1\x8e\xb8\xfcY\xe0w\x87\xb2\xfc\x8e\x0e\xe7\xf92\xaa\xbdI\x0f\x8f\xcfu\xc6\xec-\xd3\xff\x1b\x01\xe1\xf0\rf\xb7\xe7l\x877\xa9\xf9\x1a\xb1\xd9\x9b\xdaz\x93\xdc\x16Hk\t\xe4\xf4\xdc\x82\xa7.\xceel\t\n!\xe5/\x14\xa5\xcfD\xc5\xcf\x84\xa5\xbb\xe2\xca\xa7\xe2\xaa\xa7\x8az \xb0,([`\xe5\x1a\x08\x11\x90K\xf5\xa0\xa7a\xd0K\xdbw\xcd\x88\r\xb0\xe0\x83!\xeb:B\x8c\x16\x17\x0b\xb8%\x98H\xd5\xe4}\xe5D\x92\x82\x10\xaf\x9b\x8c\xd5\xe1\xa2M\x93\xb1\x16R\xa4i"\xd4\x88\x8f\xd0a\x03l\x13A\xc2\xe6K\xb8\xac/F\xb3N\xcfTy\xd1j\xae\xe3\x8a}j\x93\xfc=\x8f\xbc\xeb\xf7\xed\'\xd9A\xc7\xfb\x1e^c6\xdedV\\\x98m\ty\xbdB?(\x9e\xb7S\x85\xe71]\xe79\xd9\xe8\x0b\xd0\xa7[\xfd)\xed\x01\xb3=\xb7\xe8]\xb78\xe8\x10+%\xf5\x85\xbczWZ\xbc\'+\x81\xc4\xef+\xaa\x81\xc0\xb6\xf0\xc96\xbf\xe2\x99\xbcy[\xd9\xb2.kpq\n\xad\xd4$\xc0j\xe8\xf7\x975_Tu_6\r\xfb\xe9\xb1!\xca\xd1\x10\xc0\xad\'$\xe8\xf1\xf7ecqR\xc2]\t.Q6\x99,\xc4\xc4\x8b\xc6\xe2\x0c\x93\tJl\x84\x16\x0f\xc7\x12\xa1\x19\x0b5L\xdc\x01&nR\xac\xba\xc7\x7f\xf4\xc1\xb9\xe9r/b\xe9\xd5\xf1\x82[^\x87\x7f\xef\xfd\xf5Ga\xe7\x8ef\x07};Q\x19Bk\xf0\x14\xd4]fu\x86=_\x9d\x81\xe6\x03.\xe8\xc0\xe7zP\x9b\x03(\xedA\x94\xce\xe0\xd9\xdePF\xff\x9d\xb9\xbe;\x9c\xa1p\xd7|\xd63i\xe9\xbe\n\xf5\\S\xfd\\\x89z\xa9\xa8\xdf\x93\xa1\x00\xfa&\xafd_\xd3\xb8\xab\xeb\xde\xd1\xb6\xafH\x1b\xdd\xac\xc7:\\\xa4r\xe0\x86\xb0\xf5\xb2\t\xedo\xc2\x04\xe9\xb1\xb7\xe5CarL\x0c\xe0\x16\x8f\xdf\xd5\x8e\'*11\x16R2XK\x15!V;\x95\xa0\xc6%\xa8\xc6b\xe5#\xe1PK@@\x87\x0f\xd7OFj`VL\xc7\xd9\'\xe3g\xab/R\xab\xbca\x02D\x9c\xfd\xcb\xc5/\xde\r:\xf5y\xc4\xf9\xcfk\x12/\xcd\xb5F\x8a\xfa\x82\x85\xf5W\x94\xd8\xfb\xaf\x91\x99\x08\'\xf0v\x08\x02\x01Z[\x08\xbd;\x98\xd6\x13\x0c\xe8\xe7\x07\xc3$\xa3\xb1&r\xda\x0bm\xcd\xbe\x16\x05\x8e\xed\x85\xa6\xf1\xa5\xbaq_V\xb3\xc1}\xbc\xce\xc9\xdf\x16W\xbc0t\xef\xe9{\xb6\xb5\x9dO\x15\x8d6\xfa\x03\xa8\x01I\x87\x17\xbb\xe1\xac\x05\x13\xa6\xc0\x00\xa6D\x1d!E\x85KQ\xe3S\x15\xc44\x05\xee\x9eb2I7\x95*\x1b\x8b2\x90b @\xc7\x06|\x94v<J?\x11\x0bb0NDZ\xa6\xe3\xa0\xa8,\xc4\x04\xa8\xab\x05Z<\xb3\xc1\xa7?\xeb\xe4\x9dc\xef\xde8\xf2Q\xd8\xc9\x7fK\xf5\xfc|\xb8\xe0\x86h0\x86\xd3\xe1\xc7\xaa=\xef\xe6T\xc0 \x07\xe80\x83\xc1P \x93\x18\nf\xbe?\x14\xa03\x87\xc2\xf9\xd8X;-{WZ\xfd\\\xd5\xb0\xabBA\xb2_j\x9b_)\x1b\x9e\t\xcb\xd7\xd9\xc5\xf0\xfa\xae\xaa~[\xd1\x06\x8e\r\x08\x80\x06\xac\x94d9\xfa&\xab\xe1\xbc\xb2\xdfO\x83\x8bRN\xdd\xd7\xd1r\xb4\xf4B%)_M\xc9\x97O\xa5\xa9\xa8\x99zJ\x96\x9e\x94f$\xa6\xd9(\xc9\x80\x15\x08(0w\xa0+@\x15A\xe2\xe1G\x08\xf3\xe4=\xcb\xf4=\xe3\xd4]#)\xc2A\t\x97\xf5\xde <\xb9\x11\x7f\xea\xbd\xca\xf0\xe3\xcdw\xcf\x90\xca<\x99\xad7\x19\x8d\xfe\x94\x92\x136F\xc9\x8b\xd5\xf9\x03\xf9\x1e8"\x8f\xb9\xfeH\x06\x1aA\xcf\xc3\xc4\xe8Hi \xd0\x1dy\xcd\xae\xa2\xee\x99\xb8\x16\xd2\xffB\xd5\xb0\'\xad\\b>v\xd2\x1fY\xe6\x8aLs%\xcb\x92\x86UE\xcb\xa2\xa8n]T\x05\x1a\x95\xf6\xf8H\xba\xbc%\xa0\x81\xe10=5\x03\x9c\xb0\x99Ui\x136\x99\xb8\rrj\x1e\x1f\x9b\xa0\x9a\xca\x90\xe2\x93\xa0\x1f8\xe8\xa9\x96\xe9\xbb\x86)H|,\xc0\xb5\x92\x13\x8d\xc4\x188\x04(\xa1\x83\x1f\xb5\xf8h\x07-\r\xc4\xe0\x9c\x0e\x93u_\xc1\xe5\x9e\xc1\xe7]\xa1U\xdcd\xd5yM\x16_.\x08\xf8\x0b!\xff\x8cb\xe4\xdek\'\xe9o\xee\x101\x14<\x8f\xb9\x01\x80\x1e\xc7\x1d\x8d\xe5c\xe3]\xec\xf2\xe7\x86\x96gj\xd4Kc\xd7\x0b}\xefs]\xcf>\xf4Jn\x91}\xae\xd4\xcdk\xd2\xb2\xea\xe5\xf4\n\x17\xa7fE\xd6\xe6\xe0V\x99gs\xa5\xc3\xb7\xd9\x8d\x17Y\xad\x97\xd9\xdd7\xa4\xa3\xd16V\xc1\xa2\xa0\xca-\xaa3\xf3\x1a-\xdcZ=\xb3DM\xcc\x94b\x93\x04\xe8\x18 \x00Y7\x93\xe2!\xa0\x11\x81\x8e\xe1@\x1c3\x89\xae\x99T+L@\xca=3)\x01^\\\x98\xcd\x84\xb9\xbe\xc9HZ\xa2\x86\xeb\xd1~\xcc\xeassU\x17\xf9MWe=\x81\x84\xc2+\x92\xfe\x00\xc5\xc0\x9dmU\xe7\x8b\x15\x18\x05o]\x1d\xb4Q@/\xc0%\xf1\xf0\x19\xc2\xa9\x07\xf0\xbb]c\xcb\x9e\xbe\xeb\x87\x05"\xc4k\xeb\xc0\x8a\xa0V<]\x94\x12v<\xd2\xf7\x1b\x02\xba\x9c:Rl\xe5T/\x08P\xb6\xb9\xc7j\xc2=\xdd\xd8mI\xaf\x17\xbf\xd3[\x8a\xbee\xa1g-K\xea\x96$M.A\xb3\x91U\xbb"\xaaw0\x8b\xcdT\xa8\xfe\x18a\xffm\xd90R\xf4Z\xfcA\xb2\x13@\xd9\xd0\xa3\\3\xe9nz\xc6\xd2l\xbaa2^?\x11\r\x8d\x0b~\x84\xc6\rneu>i\x85\x16g\x1b\x0f\xe3\xd4\x9d\xe1\xa2N\xc1\xd2\xc7\xac8\xc7o\xf0\x14\xb5yn\x89j_.Q\xa0\x11\x1dp\xf0\x10\xe2\xd2\xc4\x13\xb9\x80\x12\xd2\xb6c\xe9{n\xed\xfbq\x9d\xf8\xd3\x86\xe8\x97m\x0e\xd8W\x0b\xb3\xd5\xff\xc2\xfb\x01\xde\x17\x0f\x7f\xfc\xde\x17\x9f\xfckkY\x92\x9b\x8f\x82\xdcCG\x87\xae\x02\x9dD>\x18,\xe8\x0b\x96\x8c\x84\xd9\xd9EvQ\xe3\x82\xac\xdd\xc0\xa84q\xeb\x9c\xbcZ\xf7\\\xa1\x8d\x9c\n\xf3[5\x16\xcd\xef\r\x02\xd0Jl\x14p@\x02\x87\x1c\x82i:\xc99\x9b\xb1\xc0H\x87s0\x92\x12Mp%\'Y\xe9)\xf6\xf9\xf4%v\xfa:\'}\x99\x1a\xeb\xc0\x05\n\x1aN\xf0\xab\xce\xe3R>\'\xa4\x1e\xa3<9\n\xa7\xb4c\xc1\xec\xafr\xa0\x17!\x1aP1\xeb\r\x82\x0e\x93\xa8w]\x8fy\xe5\x1c~\xb3J\xfdi\x97\xff\xe3\xbe\xe2\xc7\xa7\xdc=\x0bv\xa23_H\x1b\xc9\xbc\x17q\xe9\xcc\xd1\x9c\xb4\xb8p\x9f\xc3\x16F\xbe\x99\x92h\xa7&\xbbg\xd3\xe0FC\xb8k\x9cN\x85L\x9b\x19\x05fn\xb3\x89\xd7\xaa\xa6\x96kgk\xd4\x8c\n\xf3L\x91\x8e\x98\x0c\xd2\x84\xe2\x86\x1d\x85X}\x85Z\xef\x05R\x81L\x03\\\xfb|\xa6~*a\x85\x93\xeb\x9aKw\xce\xa6-\xce?\xb21\xb2\x80\x83\x83\x99\x0576f\xfa\x1a?w\x93\x9d\xb9:\x93 \xef\xbd\xc8\xab;?Sxn\xf4\xee\xd1\xa9\x07\x9f\xdb\x08\xb7\xd7\x15M\xcf\x17\xe7\x0f\xc6\x99\x87S;\xb9`&-[I\xb0J\xef;0??\xe3\xfd\xbc\xaf\xf8yK\x08[\xc8\x9em\xa2\xa7*\xad\xab.7"\xe0\xdc\xc9/\xde;\x7f\xe4\xcf5\xa9\xde\x0er\xf2\xca\\\xe6&\xbb\xe0)\xa7\xccJIw\xb3\x9e\x98gsL\xa4t\xcb\xccC\xfd|\x99z\xb6\x9e?U2\xd5\x91\x19\x17r\xbc$\xc3\x8f\xd4\x93\xc4\xc5\xa4H\x86\xa3@\xb8\xbc\x9e@f\xbb?\xb7/\x04\xd2\x0fk\x97\x99\x9cb\xa7e\xd8f\xd3A\xdc\x90\x0b\x1b5\xd3:\x93a\xa2eZ\xe9i\x16Z*\xbc\xee\xe2\xe6;\xe8\x99\xab\xcct\')J\xd4~e4\xed\xcb\xde\xd0Cc\xc9\x87\xd4}\xd7\xd7\xd8y\xaf\\$\xe8\xa7\x08\x81e+u\xc5\xceX\xb5\xd3\x9e;\xf1?lQ\x7f\xda\x13\xff\xb2\'\xfbu\x87\xfdz\x91\xb0m\xc2\xe2Z3\xe9#Uy\t7\xee\x05\x1cK\xf6yG2\x1c\xe7$\xc6,\xd2\x80C\xb6\x13\xd0\xd3\xb3\\s\x8f`f\x1b\t\xf1\x1ab"\x1f\x9f6;\x94\x1by\xe3\xbb3_\xbf\xef\xe7s\xf9\x0f\xbf\xff\xed\x87\xef\xfc\xf6\xd8g\xbfe\xf6g\xb2;\x03\xc5\xe8[rL\x14\x7f8B:v\xd7HL\x81\x16\xec\xa0\xa7\xeb\xa7\x13\xa1\xc6@\xdf\x0b\x8cT($\xe4~\xea.\x88\x04\xb9RR]\xd4\x8c5V\xc6"9\xca8\xea/n\xb9^\xef\xfd^o\xc4\x87\xd2\xd6K.J\xf2\x9e\x05\xf7r\x05\x0eA\xe0\xb1`\x9d]s\xccm8\xa8\xfbv\xdc\xeb\xadY\xa8\x9f\x9fw\xc5\xbf<c\xfcua\xe4\xa5\xb9W<\x993\xda\x10Wx\xf7\xf4`\xb1\x9fc:\xd5=}\xcfN\x88\xb2\x13\xef\xda\x89\xf7\xc0`.\xd3\xd3]\xd44\x90\xb2b\xd0\x0f\x06\xcddST\xa4\xcfW\x19\xf7n\x8b\xf93\x9e\x9eW\x8e\x9f8\xfa\xf1\'\xef\xbf\xf3\xa7\x7f\t:\xff\x17R\xad/L_\xe9h\xa4b"YM\xcePM\xa59\xe6\x1f:g\xb3\x90\xda\xa3$\xc0\x86\x04\x96\x04\xd0\x83\x88m\x94$3)\x16\x02\xf8XHI\x8e\x99\xfb\x0eJ\x1c\xec\x18\xaa\xde+\xe4\xac3#\t\x87\x84\r\x97\xe0\x95-M\xcf\xde\x02\x19i\xa3Kf\xda\x8a\x85\xbca\x19\xdf\xb7\x13~Xc\xfc\xba+\xfci\x97\xfb\x1f\xbb\xf3\xaf\xac]/\x95U\x0bs\xd9\xfa\x89\x14\xc5\xc8\xdd\x85\xe9T\x1b\x0c\x1d\xec\x1d3.\xc26\x15o\x87\xcc\x91\x93\xe0j\xc5\'\xaa\xd1\xbe\xd0L\xc7\nO\xe7\x04}}\xf6\xf3w\xb9\x94\x91\xb1\x81\xc6#\x87?\xf9\xe8\xa3\x0fN\x9f>y\xf4\xbb/\x8f\x7f\xf6\xeeXy\x00\xb7/H\x83\xbf\xa7\x99J\x83\t\xad\x9f\xc9\xb1\xcf\xe7\xdb\xe7r\xf5\xd4\x14\xe7\xdc\x03\xd3t2\xe4\xdbLI\xb7\xd02\xa1\xa2@`\x00\x1d\xae\xb0f\x00\x1fp\x19\x96\x89 \x0b\xd6g\xae\xf0,>\xe53>\xea\x04,\x1e+\xb2\xfa=d;\x13y,[f\x96\x0c\x93k\x96\x91]\xd7\xc4\x9b-\xe6\xaf{\x9c_v\xd9\xff\xf1l\xeeGG\xff\x96\xb8tM\xf8hK\x90\xff\x8c\x93\xbbBK\xb3M\xdc\xd5c"\r\xf8\x18\xeb$r\x02:l\xa4\t\x1b\xa1G\xdf\xd6\x0f\x06\x82\x9b\xa0\xa3\xbc\x1e\x86\x1c\xf6=\xf5\x11\xa6\xe5IM~\xbc\xef\xb5\x13\x1f~\xf0\xce\xe1/>\xfe\xfa\xc8\'wC\xcfj\xa7K\xb5\xd39\xa6\x99GFF\xb1\x95_e\xe7U\xb9y\xe5vV\x99\x99\xfe\xd8\xc9*Y\xe4\x96\xdb\xd9%6f\xb1i&\xdf@}`\xa5\xe7\x80$\xec\x94L\xf3t\x1a\xe8\xc4N\xbfo\x86\xb5\x0e\xe7\'n:\xc9,\xfbJ\xd1q\xd9\x8c\x0b\x80\x81\xf3\xc2M\xfa\xbb\x06\x0c\xb8\x15#f\xcbNx\xbe0\xf3\xfd:\xe3\xf5\n\xed\x87%\xd2\x9a\xb8v]X\xbc\xccy\x0c\x87`!\xa5\xda)\xe9\xd0\x13\xc1\x8a\xd1\x1a}\xf9=\xa1\xe2\xa1H\xf1`\x84\xb4\'P\xda\xee\xa9\xe9\xf3S\xf7\xf8\xaa:}\xa7Q~\x19\x01\x9f=\x8e>\xdfY\x12\xebw\xe1\xf0\xc5c\x9f\xf8\\\xfe*7\xfd\x8e\x96\xdbc\xe6\xd4\xd8\xb9(\x1b\xbf\xce\xad\xea[\xd6\r/j\x06\x1c\x8a\xf6eU\xafC\xdc\x02c\xdb.l\xb5\xf2\x9bl\xbc&\xab\xa0\xce.D\xd99\xe5\x8b\xec27\xb3\xc4B\xcb7\xd1rL\xb4\x07N\xf2]\x13\xd6_\x87\xbe.\xe9:\xaf\x18\xbaf\x1a\xbf\xb9)F\xbdp\x93\x91\x13X5QV\x8d\xf8\xa76\xc2\xba\x11\xbf\xef\xa6\xee\xd8)\x9bV\xc2\xb2\xaa{A\xdc\xb8\xa7m|\xa6lw\xcc\x97\x1b\xc8\x85\xd3\xcd\xe1\xd8\xea\x80\xf1\xda\xe0\xbeb\x9f\xe9\xd6\x08fw\x1c\xb3\'J\xd8\x15,j\xbf\xa1\x1f\nQ\r\xdcT\x0f\xdc\xd0\xe2\xeeH\xc7\xee1\xba\xe3\t\x8d\x11C\xa8ptM\x84h\xf2\x89n\xbe\xca\xc6.\xb3r+\xed\x82\x06\xbb\xac\x0b\x9e\x05\xb1d\xc4-\xe8\x87\x97\xf4h\x97\xb2\xdb"\xea\xb4\xc8:\x9d\xea\x9eeu\x9fK\xda\xe1\x106\xc3\xd4\xb7\xf1kM\xdcZ#\x07\xe5\xe0W\xbb9ef\xf2};xA\x8c\xbf\xa2\xef\x92n\xd8\x13V\x0ep\xf2;v<\xa2\x81E\xfd\x94K=d\x97\xf6YEh-\xabk\x1eS\xae\xe1\xb4\xdbx-k\xaa\x1e\x98k.YwW\xf9\xad\xa4\xa0CI\x81_f\x85\x1f\xcf\x8c>\x95\x15\x7f\xa2 \xfdRu\x81\xe7`\xcd\x1dF{\xe8|s\x80\xb4+\xc88\x1an\xc4\x84\x82<\xa0\xc7kq\t`?\xc1\x17A1@S\x87\x9e\xe8d>r\n\xab`\xc6\xad\xeaG\x97\x8cc\x8b\x06,\\\x9d\x9a!\x9b\xa4W\xc3\xaa7Kz,\xf2\x1e\xa7j\xc0\xa1\xec_P\xf6,\xca\xda\x1d\xe26\x9b\xb8\xc3\xa5\xe9\x87W\x1c\xd2V\x0b\xbb\xca6\x97\x07*\x87\t`\xc5\xbd\xdd\xb91\x016z\xce3\xe3\x10\xd2\x85\xdc\xeaq\xbb\xa2W\xc7i\x16\xd3\xaa\x85\x135#u\t#u\xf1\x82\x89"\xc3|=\x10+\xcc\xbaq\xfb\xc6\x97\xa17\x8f\x86\x06\x9c\x0c\xbfu&"\xe4T\xcc\x9d\x131a\xa7\xc2B\x8e\xdc\xf6\xfb\xb4:\xf5<\xa1\xfc\x06\xb9\xe6\n\ruV=z\xcbD\x886\x12ba\x11\x03c\x03\x06\x01\xe4\xb80\x9f\xb1\xc8y\xe8\xe2\x14,\xcb\x1a]\xf2\xf6e\xf5\xc0\xb2ax\xc5\x8c]\xb5\xe0\x96\xf5X\x93\xb8[\xc5i1\n\xbb\xac\x8a^\xb7f\x18`8\x14\x9dnE\xb7M\xda\x0e\xdc,\xd2n81\xb8w\x88\x9b\xcc\x8cB\x98nfb\x94\x19\x17\xa4E\x08\xf8\x1b\xa6\x92\x9e\xaa{\x9e\xafq=\x0c\xe2n\xb7\xa2wA\xd9\xe7\x14\xf5\xab\x19M\xcdy7[\x1e\x07\x1aY\xedrr\xad\x96\xd3\x17\xee\xff\xed\x99o\xff\xed\xebO\xdf=\xfa\xf5\xfb\xa7\x8f}z\xf6\xe4\xc7~\xd7\xbe\x0b\xf4>v\xfd\xca\xa1\xebW>\xf1\xbb\xf0\x87\xfc\xf8c\xd3-A\xf2\x91HI_\x088d5\x01\xb14p\xe20\xa7t\xc4$\xfb\\\x8e\x83\x95o\xe7\x16\x02\x81eE\x07\x14\xfd\xa2\xaa\xd7\xad\x1bZ3\x13\xd6\xac\xf8u\x1ba\xc5<\xfe6\xb0n\xdd\xc8\xa2vd\xd90\xeaV\xa2]\x8a^\xbbz\x00j\xcc!\xef^\x94w\xbbd-N^\xb5\x93\xfd\xc41\x9bl\x9b\n3\x8e\xf9\xc3>\rmjS\xda\xb0\xbf6\xef\x01\x7f\xf6\xd4<\x0e3k\xc3<\xe6\x94\xa0\xc5S(\xd4\x03\x7f\xc6p\xbe\x80XI\xc3Vy\x9d\xfd\xf4\xcc\xb7\x1f\x1ez\xff\xf7_}\xf2\xce\xd1\xcf\xffr\xfc\xc8\xfb\'\x8e\xbc\xf3\xcd\xe1?|\xf3\xf5{\xc7\x8e\xbes\xf9\xd4{\x97N\xfcn\xb4\xe56\x07\x1d\r;\xb4\x14\x1d\xc9\xee\x0cV\x8e\xc5\xab\xf0\t\x96\xb9l\x1b;\xdf\xca*\x06\x07\x0e\xf5c\xe1V\x9ay\xf56q\x9bC\xd2\x0e\xb0\x16\xf4\xd8\r\xcb\xc4\xa6u\x12\xf4\x00L\x9c\xfa! \xb0\xa0\x1f\x85\xb0\xc9\xfa\xb4\x82N\xb3\xac\x1b8\xc0;]\xf2N\xa7\xac\x03\xfc\xaf[\\m\x9f{\xb00\x9bh\xc1\xdfr\x93c\xac\xa4\xbb\xee\xf9\xfc\xe7K\x0c\x84\x00\xc8\xf9\x99ur]\x8bvJ{d3\xf5\xd8\xe6dTN\x08\x07WED\x97\x84\xf9\x1d\xbbp\xfc\xd3\x0b\xc7\x0f\x7f\xf7\xc5\xbf}\xf1\xf1\x9f\xbe\xf8\xe4w_\x1e\xfa\xd7\x0f\xdf\xff\xa7O?\xfa\xcdG\x1f\xfe\xf3\xe9o\xfe|\xf9\xf8?\xd7>\xba0\xd1\x18D\xae\xf3\xa7\xa0\xbc%\xc31\xfc\x9ep\xd1h\xbc|*\x05\xb4\xeb\x14V\xc0\x83A\xc1&f\x85v\xb6\xc2\xc8\xa9\xb1\t\x1b\xec\xc2\xf6\x05\xd5\xe0\x92\x06\xb3j\xc2.j1.\xed\xb0\x0b\x1e\xad\x19\\\xd2a\x9d\xcaa\x84\x92\x19\x07\x8d\xf1-\xa5a\x97zpA\xdd\xeb\x96\xd4\xbb\xa5(\'#\x17\\\xd3\x02%\xde:\x15\xb58\x93\x04\xaen\xd79\xe5\xb1\xe3 \xee\xbb\xc9[\x16\xc2\xa6\x1ec\x17v\xaaf\xea\xc0\x0eT\xa6y3\xb1Uc\xdd\x85y)\xa1^\x17\x8e|\xf9\xd1\xff\xf9\xe6\xf3\xf7\x0e\x7f\xf4\xfb\xaf>\xfd\xe3\xd7\x87\xde\xf9\xfc\xa3\x7f\xf9\xe4\x83\x7f\xfe\xf0\x83\x7f\xfa\xfa\xd0o<O\xfe\xae&\xf7\\O\xc15l\xd9\rl\xb9\xf7T]\xe0D\xbd\x1f{0v\xa25\x92\x81I\xe3\xe2\xd2U\xd4|\xd8\xd1\xc0&if\x9ehf\x8b\r\x1cd\xddq\x88\xba\\\x8a~\xbb\n\r\xe8A\xcd\x90o\x90\x81E\xda\x8f\x94\x96\x99\xb0\xed\x98\x062\x07\x04@\xdc\xa0\x04\x97\xb8\x01\xba\xa2\x9b[\x04\xa0\xed\x14\xd8?c\x97\x18\xc9.Z\xca\x96\x11\xed\xb1\xbbD\xddvOmYq\x1b\xbaa\xa7\xb8\x1b\x1c\xa5\x84R\xd1V\x14\xd4\xfc$\xac\x0f\xf5 7\xe9Nl\x98\xf7\xf1/\xdf;\xfc\xf9\x1f\x0e\x1fz\xf7\xc8\xa7\xef~}\xe8\xcfo\xe3\x8fG\x0e\xfd\xee\xecw\x7fL\x8b>Y\xfd\xe0B\xfb\xc3K\ri\xe7\xd1%\x81\x98\xca[\xadEW\x1b\xf2\xaeTe\\\xaf\xcc\xf6\xe9,\xbfIh\x8e`\x8e\xde\x07\x9b$\x9a\xc8R\xd0\xf2\xa1?:%\xcd.i\x9bM\xda\t\xaa5\n\xda@\xac6y\x8fU1\x08\xa7\x01%\x04W@\xefR!\x15\x05j\x81\xc3\xb1\xcbz\x1c0(x(\'\xa7ta\xf6\x81\x85\x14i\xa3\xc6\xb9\xe8\x88\xe3X\x125zl\xbbI0\xc5\xd6\x0c\x98\x15m?\x14\xa8\x89\xd3\xa4\x98\xad\x9d\xecN\xa9\xc9\t,L\x0b\x89\x0b\xbe\x1e\xe0s\xda\xef\xfa\xf1\x93\'>\x06\x19\x1c\xfe\xe8\x8f\x9f\x7f\xf8\x87\xc3\x9f\xfc\xe9\xe4w\x1f\xfa^\xfd*\xfe\xce\xa9\xc7\xc9WJ\xd3\xcf5=\xba\xd2V\xe0;P\x11\x96\x13\xfema\xca\xf90\xaf\x0f\x03\xce\xbf\xefs\xec\xdd\x88\xeb\xef\xa3\xb2\xaeb\xebC\x88\x1d\xe1\xb3\x83wy\xe3\xe9ZF\x11L+\xe0\x80\xf4Ja\x93Y\xd0\xa4\xe7\xb7\xdb\xe5\xfdP*6\xe5\x10\xe0\x86\x00\x0e6U?\x14\x95M\xda\xed\x10u\xc0\x98s\x89Z\x80\x00\xec!\xd0\x1b\xb4\xf8@\xd8Bm\xd4\xbb\xb0a\xc3b\xe8\x01b\xdau\x13\xc1G<5\x8d@\x1b\x86Qb\xe27J)eL|\xf1\xe3d\xff\xcb\'?\x82\xb6\xe3u\xf5\x1b?\xdf\xd3\xdf\x1dz\xef\xea\xd9o</\x1e\x83\xf0\xbdv,\xc0\xeb\xdb\x98\x90o\x9e\xa4{\x96\xa5_E\xe5\xdd\xa8\xcb\xf7-\xcb\xbc\x96\x1aq\xec\xd2\xd1\xdf\x9d\xfd\xf27\xa7?\xffM\xe0\xb1?\xe7G\x9fj~\xe8=V\x17H\xeb\x8f!v\x84\xd2\x07\xe2\x81\x00l\x9b \x06X\x9a\xe1\xb4\xcd\xc2\x0e($\x1b2\x98\x07\x0f@C\xef\x87\xb1\x00R6\x8a:`<;\xb8-\x0en\x93q\xbe\xcc:_j"ghp\x11\x9a1\x7f#\t\xf9\x8a\xd2L\x8d]d\x15z \x9en\x99\xf2\xcc=\xf1\xcc\x86[5\xa0\xb7\r\xc3\x9b\xfa!\xf8K(\xa4\xe1\xa6\x0c\xff\xb3\x87\xaf\x1d\xff\xe4\xc2\x89\x8f\x8f}\xf3\x97#\x9f\xbew\xfe\xf8a\xef\x0b\xc7\xfc\xae\x9f\x0c\xb8\xfem\xd0\xb5o#\x03\xbf\xcbK\xbcT\x96\xea\x93\x19\xf5]\xc4\x8d\x8f\xaf\x1f\xfb\xdd\x85\xaf\xff\xd7\xd9\xcf=\xbc\x8e\xfe\xef\xa4\x9b_T\xa7]\xeb*\xf4\x81\xf9\xcd\x18\x8cSRr\xcd\xecR))\xdb)\xa8\xb1\x0b\x90\x95\xdf\xc0\xaa\xd3q\x1ba\x97\x02\xb8\x07b\xb0\x83\x18$]\x16q;T\x17\x84E\xdcj\xe14\x18\x195:Z\x89\x96\x9co\xa0\xe7\x83\xe7\x93\x8f\x04\x8a\xfbn \x03a*\x06\x94\xb0\xcc\xcc\xf5x\xe6"\x83\x0cv\x17&\x9f\xdap[\x86\xe1-\xd3\x08\x1c\x85S\xd2n\x15vJ\x88M\x85\xc9A\xe1\xbe\xdfA\xb7\x01\xed\x1e\xff\xe2\x83c\x87?\x045\x1f9\xfc\xa7\xa3\x87\xfep\xf5\xd8\x87\xbe\x97>\x82R\t\xbc\xf8\xae\xf7\xc9\xdf\xf8\x9f\xff\xd7\x90\xab\xefE_\xfb4\'\xecxi\xe2\xa5\xda\xcc+\x9d\x85\x9e\xf8&\x7fZ\xf7-1\xece0\x89\xd8e\x16N\x99\x89U\x0c\x1b\xb3\x8e\t\x1d\xa9^\x0b\xf8\x84]0\xce,\xf2>P0\xd4\xba\x95\xdfba\xa1,\x9c:\xc0m\xe7\xd6\x1b\xe6Q:z\x05\xf4\x005\xf5\x91\x9e\x92-\x1b\x8b\x03\x02\xb2\x81\x00\xcd\xf8m@\x0fU\x04\xe3\xd9c\xcbF\xdc_\xa4B\x15\x1d\x10\xd86\x8f\x1e\xc4\x8ee\xcc\xc0l\xe3L\xd4\x8dv\xe6f\xc6y\x9d\xfe\xea\x8f\x00\xfa\xd4\x17\xef\x9e\xfe\xf2\x9d3\xdf\xfc\xf9\xe2\xb1\x0f<O~\xe0s\xfe\x8f\xdeg~\x9f\x12\xfemv\xec\xd1\')g\x1e\xdf;\xdd\x9e\x7f\xa3>\xfbtS\xee\xf9\x8e\xc2\x8bS-\xfe\xac\xa1h\xd9d\xb2\x9a\xfa\xd04_\x04\x01\x04t\x8c\'\x06F\xa9\x96Q\x06\xd5o\x14\xb4\x18\xf9\x1d\x88\x8b\x11\xc3\xc4\xed6\xf1\x9a\xad\xdcF\x1d\xa3\x12i\xb8\xf3e\xda\x19XM+4\xf4r\xe3\\\x05\xfc\x89\x86\xfc@:\x14.A\xfb\x01\x01\x1d>\x1c\xf9\x82\x8c\x18\x06\x1c\xe0\x04H\xb0\xe4?s\xe0\xb7\x0cX\xc8=\x04\xa0\xdf\xb5b\x81\x00\xdc\x8b\xa8\x15,B\x11\xba>\xa1\xa10&!\xe4Dr\xd8\xf9H\xdfo\xe2\x83\xbeK\t?\x93\x12z\x1a\xf4\x8a\xca\xf7\xac~x\xb59\xf7Z\xfb\xa3\x1bu\x99\x97\x1a3O\xb5?<9\\v\x89\xdc\x11\xc0DG"\xe8\xc9\x19\x06F\x9e\x95[\xee\xe4W\x82\xab1\xcdA?-\x02\x87\x07\xfd\x07\xfc\x02\x100\xf0\xda\xf5\xf3\x8d`E\xcd\xeczH< VP\x8b\x81\x86~\xbeJ7_\x03\xef40\xabL\xf4"\xd5D\x8ax8T\xd4\x7f\x83\xdf\xeb\xa9\x9f\x0c7\x10\xc2\xb4\xe3a\xc6\xe9x\x8f]7eg\x91\xbc\xeb$=5b\x0e\x08<\xb5\x8cn[1O-\xc3\xeb\x86!00Fa\x13w\xa2x\xac5\xa7\xad,\x1aU\x10\x86\xca\xbd\xd5\xf48\xb8\xab\xf0N\x7fID_I\x10@\xaf\xc9<_\x97v\xa6.\xfdXK\xd6\xf1\x9e\xc2\x0bCU\xd7\xa8\x1d\xc1\xf3\x83a2b\x8a\x92\x94\xae$e\xea\xe9\xf9\x16v\x85\x95Sma\xd7\x00\x1a\r\xbd\xd2 l\x03\xe8fa\x97M\xd2o\x13\xb4\x01tH\xb6\x92^\x06\x04\x8c\xac:\x08P\x88E\xd8b\x15\xb5\xda$-`\xc5\xd5\xd3\xd9\xe2\x91\x181\xfa\x8ex\xc0\x9f\xdb\xe5\xad\xc2\xdcRco\xcb\x86\x03\xac\xd4{\x1e{\xcb\xf4g\x0b\xd3 \xe5\x1d\xc7\xe4\x8e\x05\x03\x1aX7\x8d"W\xc3\x10\xf8[h\xac6A\x8b~\xaeS8Q\xc5\x1d\xaf\x98\x19x\x8ckN\x1bF\xc5\xf5\x16\x85\xb4\xe5\xfaT&\x9fA\xa5\x9d\xabI?\xd3\x90z\xa63\xf7\xfc@\xd1\x95\xc9\xfa\x10r\xfb\xed\xb9\xfeh\x0e\x1a\x86q\x9a\x96\xf2PKC\xe4kfU\x02th>zV\x8dQ\x0c\x06\xae\xc9*\xee\x01\x02`"!\xcd\x90l$\xe6j@\x03\xc0\x07Z\'4Y\xa81\x08\x90\x81\x92\xfcXI\xccUN\xdc\x93\x8c\xde\xe1\xf4\xdd\x80*\x82\xfa\x91\x0c\x06\xc8G\x82a\x14x\xec\xaf1\x00=\x04\x0c\x84\r\xeb\xe8\x86qx\xcb0\n\xa7\xb1\x06f]\xde\t-U\xc7\xae\xd3\xcf\x81\xb7k\x04\xaf\xca\x1c)\x9bh\xcf\xec\xaf\x8c\xec)\x08\xe8\xc8\xf3k\xcd\xf1nL\xbf\xd4\x9b\xe7\xd3\xf3\xe8:\xa6"\x00_\x1bLi\x8f\xe0\x8f$\xf11\xf7\x05\xd8d\xd5d\xb6a\xa6\x00j\x06\x84\x08\xa95\xb3Q\x90T\xa4\xff\xf0\x9b\xa1\xc9\x00z\xa4xx-jF\x15\x14\x8c\x86Yc\xe6\xb79d\xfd\x0b\xaa!\x87l\xd0!\xef\x85\xe9\x06\xefG\xb6\x1cN\xb5\x9a\x92/\x9dL\x10\xa2o\x0b\x06\xfc@\xc7\xd2!?H\xbfr4H\x8b\x0f\xf7x\xb3%\x02\x11\x03\x01\xa8%\xb0\x16{\xb6q\xd0\x00\xf8\xa2e5b\x8d,\x82\x0e=\xa7Y3\xdb$#\xd6\xb1GK\x99C%\x94\xae|\\}\x02\xba*l\xa00\x08]\x12<T\x14\x84\xab\n\x1d\xaf\x0c\x99n\x8a\xa4w\xc4\xcf\xf5\xc5\xf3GS$\xb8L\xf9d\x96\x9a\xf4PG+\xd2\xcc\x94\xa8f\xcb!\xbbP\x18\xca\x99\n\x18\x94\x90c\x10\x00\x94\x10\xdck\x18\xb5rz\x85f\xae\xda,l\x83\xdeoS\x0e\xc2 s\xaa\xd0\xd0\x97\x9c\xaa>\xf0\xc8\x8b@\x95Uic\x15\x82A\x94\x0c\x06I\xd1\x81&B\xe4\x01z\x15&\xd8JN\xf0\xf8iG\x08\x9d\x14\x08\x1c\xf4"hD\xeb\xda\x81%E\x1f\xa0_\x94\xf5\x9b\xb9\xad@\x00\xdc\xb5r\xaar\x1e\x9dK\xef\xcdb\xf4\xe7R\xbb3(]\xa9\xe4\xc6$Bm\xdctc\xc2L[\xfcl\xe7=FW\x02\xbb?Y\x80M\x93\xe2\xb3d\x84\x07rJ\x96\x92\x92\xa7\xa5\x16k)\xa5\xea\x99\x12@\x0f\xe5a\xe2\xb5\xc2\xe4\xb2\x81pYMP<zv\xab\x91\xdd\x08|\\\xe2\x01\xbb\x14\r\x9d\x14|\x11\xf8\x0bd\x0e\x80B\xb8\xb0g\xbe=\x01V\xa9\x0c\x17+\x1d\x0e\xd2\x8d\xdd\x86\xadC2\xe0\x0bR\x06\xf4\xea\xb1\x10\xd5x\xb8\xc7\xcf{|@\xffb\x8d\x0e46,\xe30\xc5V5\xbd\x0b\xb2N\x18\xe0\x0b\xd2^\xf8\x14x\x98\x96^/\xc4\x16\xf3\xb1\xc5<L\x91`\xbc\x843\x92\xcf\x1cz\xc4\xec\xcb\x99\xeb\xc9b\xf5d2\xfbS\xf9\xc3\xe9\xa2\xd1,\xc9x\xce\x01\x01\xc5\xd4C\xe5\xf4C\x05\xf1\xb1\x94\x98\xaf\x9a\x06\x0fW\n2\x85D@\xaf\x840\xf0[\x81\txR\x8b\xa8\x1b\xd61\xbd\xa0\xd5&\xef\x82\x80\xc5\x12*\xd6\xcck\x84E\x19\xc2)\x01\x02\r07\x90N0\x1e\xa9\xc3\x87\xb2\xdb\xae(\x86\x02\xd4C\x81\xc0\x01N\x00\xc28\x11\xe9\xf1\xd7=\xee\x8b\xe5\xd9\x1d\'a\xd7A\x00\x01\xacj\xfaW\xd4}K\x8a\x1e\xb8\x82gt\x8b\xba\xed\xfc65\xadFN\xac\x94MU@H\x08e"\\1\\\x05#\x05<t\x1e\x7f8\x9f7\x9c\xce\x1d\xcd\xe0c3\x04\x18\x84\x83\x0c\x9f\xa7\x98\xcc\x97O!\xd0U\x94B\xf9t\x01\x94\x90\x81\xd5\x00\xa0\xa1\xe2\x01=\xd4:\xa4\x16\xeea\x12\xab\x98\xf5p\xa3\x99\xaf\x07mX\xb9\xf5H3\xe5!\x1cL\\\x98e\xc5\x1a\xfac\x1d-\xc7\xc1\xc8\x92\x0f\xdf\x91\x8d"\xb8a\x0c\xcb\xfa}\x91\xef\xf4{\xbd\x94#7\x8d\x13\xe1\x08\x81\xef\xd7\x19\xfb\xce\thA\x90\xfe\r\x1d\x1aJ\x08h\xb8$]\x8b\xf2^;\xbf\xc5%h\x05\t\xaa\xc8\xa5rr\x89l\xbaX=]\xa9$UH\'\x8bE\xf8|\x08)._4\x96-\xc2\xe5\xf0\xb1Y\x82\xb1\x07bB\xb6l2\x17~T\x10\x9f\xa8\xa9\xe5\x16\x16\x82\x0c\x00\xc1\xdc5\xf2\xea\x90\xe1\xc5k\x00i\xc2\x08\x83\xc4C\x15i\xd9Mo\x0f\xa4\x19\xfa&\xbc\x13~\x0b\x9d\n\xcc\x92\x96^\xac!\xe7hH\xd9zR\x8a\x18}K8\xe8\x0bu/\xea\xf5\x11t_\x17w]\xe54_\xe0\xb7]\xe5\xb4_\x05V\x1eov9?\xac\xd3_/\x10\x91\xf6o\x1e\xdd\xd4\xa2!`\xf7\x83CXT@-\xd6\xda\xb95\xd0\x07`#\xd1\xcfW\x18\x985zj\xad\x86Z%\x99|"\xc6\xe5\x0b\xf0\xb9"\xc2#\xc0-\xc5=\x94L\xe6\x89\x08\x0f\x85\xe3Y\xb0\x00@\xee\xd5\xd4b\xa4\xb1\x88Z,\xc260m@@\xcfD\xa9\xe7J\xf4,h\xa6\xf5\x90{ `\x96\xf5\x82j5\xdcV\r\x1fN\x06\xb2\xde`fU#f\x89[ca\x16#\xff\xef!&\x1b&\x13\x00%4~(z%&@\xda\xe7)j:\xcfo\xbc\xc4n\xbc\x08\x07\x02\x9e\xc2\xe3\x87\x1d\xf6\x9b5\xf2\x0b+vS\xd3\xbe\xa9\xef\xde\xd0uli\xbbV4\x1dK\xaa6\x97\xac\xc9%D\xb9%\x95\x86\xf9\x02\xc4\xc3\xcc\xc3\xa0)\xd5Q\xcb\xe4\xa4B\xe9\x14\x12\x12B\x1e\x1f\x97-\x9e\xc8\x95\x91\x1e\x8b\'sd\xd3\x10\xb9\xa0]5\xb9\x10\xa8Z%\x1d*&\n\xb2\xeb\x14w\xc2!\xa8ga\xcaVB\xc7\x04A\x83\x94\xd5\xbcV\x1d\x08Z6\x00a\x90t\x1a`2\xf0[\xec\\\x14T\x8e\x92\xfa@EL1\x92\xef)\xc7n\xcb1\x01bPm\x9f\x97\xb0\xc7S;\x1a\xa8\xe8\xf7\x127\x9ee\xa2\xcer\x9a.\x89:\xbc\x95\xc3p\x02[\xccW\xee\x89\xef\x9d\x985I\xe5\x96\xbau\xf9 T\x9d\x8b\x8a6\xd8\xc4\xdd\xe2Z\x97\xa8\xca8W\x00V\x0c>\xda@/\xd1Q\xf3\xa0?"\xdb\t1OI\xca\x87\xab\x84\x90+\x99\xca9\x08p]o\xa3\x18\xf2\r\xe9\x07S\x08\x05\x03G\x81\x94\x104".R*p&&i\x97[3\xfav\x17\xeb\xb5\xcb\x07\x8d\xdc&x?\xcc2\xd3|\r\xa4\x00\x0c\x88l\xea\x1e\xf4x\xe83\x1al\x08\x08W\xd6\xe7\xa9\x1d\xf4\x17\xb5_\x115^\x16\xd6\x9d\x174]\x16uxJ\xba\xbc5#A\x1e\xafWh\xfb\x0e\xcc\x8e\xa9wKT\xb9&\xa9^R4\xad\xcaZ\x96\xd5\xed\x8b\xb2\xd6\x05I\xfd\x82\x04e\xe5\x96:\xf9\xe5\x0en\x05\xb2\xa1\xcf?\x01\x02\x8a\xa9l\t1KB\xcc\x80\x94+\xc9\xd9\xb2\xa9\x0c\x05)GE\xce\x95\x13\xb3\x01=p\x03\xb7\x03c\x0bJB\x0f\x96\x93\x85\x82Y\x8b|\xf1&\xee\xb0\x89z \xeb\x10\x80\x1b1\xa1\x82.\x1b\x1fl\x1c\x0c\xb56#\xafV7_l\x98+\xd6\xd2\xf2\xb4\xe4L\xe5T\xa2\x1c\x13"G\xdf\x04\x94\x8a>_E\x9f\x8f\xa4\xed\x8a\xb0\xee"\xb7\xe24\xb7\xe2,\xb7\xee<\x10P\x0f"\x1d\xc9\xe3\x87%\xd2K\xfb\xc8\x8e\xa9{SZ\xb7*-\x87\xeb\x9a\xb8vE\xd1\xb0"o\x02\xf4.Q\r\x10\xb0sK\xe1\x04\xec\x9cr\xe0`\x98}\xa2\x9by\xac\x9e\xc9S\x90\x1e@\xaf\x04\xa3/%e\x01\r\xedL\x0e\xf4~\xf1T*\xdcC\xf7P1\x8a\xa1\xfd+\xe9%\xa0K\xbd\xa0Q\xcd\xadC\xbc>\xd8fy\x1f\xac`\x80\x1e\x06\x19\x1c\x8bj\xb6R=_m\xe4\xa0`\xd9W\xce>QQ\x1f\x81\xeb\xd4\x12\xd3e\xb8x\x05\xf6\x96\x06\x1b\xa4\x18\xbc\xa9\xec\xf7\x83\xa2\xe7W\x9f\x85\xe0U\x9e\x11\xd6]\x16\xb6_\x93\r\xdePc\x02\xb5\xa3\xc1\x1e\xaf\x17\t/\x9d\xd8m\xc3\xc0\xa6\xbasU\\\xb1"*_\x16\x94-\xf2\x8a\xa1~\x96\xa4u`\x80\xed\xfc2\x07\xaf\x0c\xa6\t\xa4\xdf\xc0x\x0c\xce\x1e\xaejj6\xf2$Z\xae\x9e\xf6DJ|(\'f\xc1+\xea\xb7\x1c\x94\xe4,\xc8"\x1c\x8e\x8aZ\xa0\x9b+\x87C\xb0\x89\xdb\xc0\xf9\x98D\xbdZ^\x1b\x10\xb0*\xfa\x81\x83\x96\x89\x94\x13\xec\xf8\xca\xd9"pr`\x98\xc1/@j\xb4\xd4l\xfdt\xa6\x9a\x10\rV\x07d\xaaF\xfbC\xb2YU\xa7\xd9e\'\x98\xa5\xc79\xe5g\x04u\x97\xa1\x8d\x8a\xfb\xbd\x15C\xfeP]\x1e\xaf\xdd\xf8\x17v\xcc3\xc3\x00\xc8wCZ\x05Jp\xf3\x8b\xdd\xdc\'NN\xb1\x9b_\x03\x04\x1c\x82r `\xe3\x14\xd98OL\xcc\\\xfd\xec#\xb0\xc7pUO#\xa0\xa1\xd9\xc9\xc9\xd9rJ\x06\x02\x9d\x8a\x0c`\xc5t\xa6l\xfa\x01\xd4\x95\x8eQddU#\x92\xe5\xd5;\xe4\xddf9\xf2\x1d(T\x8b\x96Uo\x15\xb5\xc3\xa0\x84\xc4\xab\x19e\x9a\xf9r\x03\xa3R7[\x82|\x7fA\xcb\xb5\xcc\xe7\x9a)\xe9\xd0|\xa4\x98\xdb\xaa\x91 \xc0\xaa\xe8\xb9\xc1\xaf=\x07\xc5#\xa8\xbe\x00\xc5\xc3o\xf7\x84\x93\xd1\x81<\xc6Bu\xa4\xbb\x1e/\x1d\xe3{\xd6\xd1m\x03\x1a\x9a\xcf\x86\xb2yUZ\xb9$*ws\x8bl\xac\x02\xc0\x8d|\x1f\xc6/r\xf0J\xec\xdcb+\xbb\x00BG\xcf\x01\x02\x10\xe0\x93U\xb4l\xd5T\x9a\x9a\x94\xae \xa6\x81\xef\x87\x00\x02\x82\x89$\xd1d\x8a\x8c\x98\x06\xed\x08\x94\x00\xd3\x14<\xbd\x8eWc\x157\x9a\x045\x06v\xadY\xd0\x00\x1dYF\xce\x97\x90\x0bA\xbb0\xbf\xc0lkf\x9e(H\xb9FZ\xae\x14\x7fOAH\xd0\x13\x12t\x84(\xc5P\x10h\x80U\x8b\x14=\xaf\xe1<\xab\xe1\xa2\xa0\xdb\x076z\x15>B\x81\x8f2QRl\xb3\x8f<^9\t{v\xec\x96\x11\r=tS\xd3\n\x1cV\xe4U\x0b\x82\x127\xef\xb1y>[O\xcf41r\x01=\xa4\xdf\xc2\xca70rML@\x9fk`>TL\xa7\xc3\x8d\x96\x9a\xa5 \xa5\x88p\xf7\x81\x0f\x14\x0fP\x92\x913\xe1W\xb0\x0c\x80H\xa0\x8a \xafPc\xc8"6\x87h\x14\xc4\xa3\xa6\x15"\xb3\x82Z \xa7\x16C\x15\xe9\xe7\xcb\x90\xd7i\x85\x16f\xa1\x83Y`a<t\xccfkq\xb1\xca1\xa4\xff\x88;\xbd\xc4\x1dW\xc5\xed\x9e\x82\x96+\xb0\x0ch\xf1\xd1\xd0^U\x93\x89\x86\xd9l3#\x1fZ\x8b\xc7\x0b\x17\xe1\xb9\x13\x0f&\x148l\xe9\xfb\xd7\xd5-\x1b\xca\xc6Eq%p\xb0s\x1e\x1bf\xb3t\xb4\x07\xc8\xbf\xe0\x99\xb9\x00\x17\xd2\xaf\x9f}\x087\xfa\x99\x1c\xcdt\x06\xe4^7\x93)#\xde\x97M&\xc9\xe1JL\x91\x90 \xf7)2r:\xec\xc1@CI\xcd\x84J\x93\x10\x92\x80\x9ed2\x15\xceG4\x91!\xa7\xe6\xc1X4\xc1R6W\x05\x95\x03\xe9W\xd3\n`g\xd0\xce\xe6\x9b\xe8\x0fe\x84\xfb\x1a<L\x800A\x9f\x17T\xb9\xa8\xc7S\xd4y\x95\xdb|\x19\x1c\x84\x0e\x17-\x1d\x8bSN%@\x99\xe9\xe9\x05\x0en\x15,z\x1e\x80\x1e\xe6\x00\xd0@\xb6\x19\xfd\xd0\xba\xb6oE\xdd\xb5$iZ\x964A\xf7\xb4\xb0\nL\x8c\x1c\xa8\r>6V\x8c\x8b\x81PL\xdeU\x92\x934\xe4\xfb0k\xa4\x84\xbb\xd2\x89D\xfex\x9cr:\x15P\nqq@\x83?z\x977\x12+\xc4\'\xf2\xf0\xf7\xf8\x84D\xb8\x99\x1f\n\xe7`\xe3$\x93\xe9\xd0\xaf\x001b\x13fK\x81\x83\x9d\x07\xdb\xd9\xe3\xb7r\x7f\x047\x86\xb9B \x00y\xd1\x11\x93\x90\xaf\xe9\xf1\xe1\xb0\xaf(0w \xebPQ\n\xfc}$_@~\xbe\xc8\xc9.\xb7\x0b\xab\x9co\xc3\x03p\x7f\xbfH|\xb10\xb1c\x1f\xdf\xb4`a\x11\x03;\xe4\x96\x80\xcb\xadv\xf0+A\x06vn\xa1\x1e*{<\x865x\x8b=\x18\x0c\xc1\xc5\x84\xf31\x11\xb04\xb2\xd1\xe1\xb3=\xb7\xe6\xfa\xee\xf0G\xe3\x18\xfda<L\x1c\x00\x05\xc4\xfc\xf1\xbbp\xc3\x1d\x8b\xe7\xe1\x93\x98Cp\xbd\'"f\xe9X%rZ!\xa8\x02\xc6\x1c\x88\x9b\x8fCL\x07ta@\x0f\x98`\xf5\xd1P2\xe1\xa8\x91\xff\xa0Q\xb2\xa0H\x84\xa3\x11\x1c\xd8`F"msy6f)\xe4\xdb\xc2\xadt\x08\x1b]\xa2\x16\xbb\xa0\xc9%jZ\x947.\xcb\xea=\xc0\xff\xbc\\\xa3<_\x9d\xd9_"o\xda\xc6\x16\x8d\xb0\xca\xf4\xad\xab\xfb\x17\xa4Mva\x8d\x9d]\r\x89\xb10\x1e\xa9\xc9i"|<\x0f\x13\x03\x9f\xc8\x1d\x8d\xe6\x0c\x85\xb3G\xa2h=\x81\xb3\xbd\xa1\x94N\xe4\n\x04 \xe6\x87"\xd9\xa3\xb1s\x9886.\x89\x8dO\x17\x10\x1f\x08`<\xd3\x8b\xc0A \xab#\x13\x05E\x8f,\xef\xacj+\x0f\x05\'\x00\x0e\x05\x1a\x1d\xd4\x03\xd2\x9dg\x8b\xac\xcc\x02)!E\x80M\x92\xe0S\xc1\x93[\xe7K\x9d<\xe4\xbba\x1d\xa3\xda\xccj\xd4sQ`\xab\xde\xae\x9d\xb0\xd9\xd5\xb9\xc4ufn\xd9\xff\x03\xa6%\t\xe6\x8f\xa0\x8a\x9f\x00\x00\x00\x00IEND\xaeB`\x82')

app.iconphoto(False,photo)
app.title("Holidays OP")
app.attributes('-topmost',True)
app.geometry('300x200+830+370')
app.configure(bg='#404040')
btn = Button(app, text = 'Close',font=("Times New Roman",15),bg='#363636',fg='white',command=app.destroy)
btn.pack(side='bottom',pady=20)
label=Label(app,text='Today is',font=("Times New Roman",15),bg='#404040',fg='white').pack(pady=5)
label1=Label(app,text=date,font=("Times New Roman",15),bg='#404040',fg='white').pack()
label2=Label(app,text="And also today is",font=("Times New Roman",15),bg='#404040',fg='white').pack()
label3=Label(app,text=yay+f" ({code})",font=("Times New Roman",15),bg='#404040',fg='white').pack()
app.mainloop()
