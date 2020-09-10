import cx_Oracle
import os
import numpy as np
from tkinter import *
master = Tk()

startprogram = "starting"

def var_states():
   print("Operations1: %d,\nOperations2: %d,\nOperations3: %d,\nOperations4: %d,\nOperations5: %d,\nOperations6: %d,\nOperations7: %d,\nOperations8: %d,\nOperations9: %d,\nOperations10: %d,\nOperations11: %d,\nOperations12: %d,Operations13: %d,\nOperations14: %d,\nOperations15: %d,\nOperations16: %d,\nOperations17: %d,\nOperations18: %d,\nOperations19: %d,\nOperations20: %d,\nOperations21: %d,\nOperations22: %d" % 
   (var1.get(), var2.get(),var3.get(), var4.get(),var5.get(), var6.get(),var7.get(), var8.get(),var9.get(), var10.get(),var11.get(), var12.get(),var13.get(), var14.get(),var15.get(), var16.get(),var17.get(), var18.get(),var19.get(), var20.get(),var21.get(), var22.get()))

os.environ['TNS_ADMIN'] = r"C:\Users\nll1kor\Desktop\RFID\Wallet_DB202005021424"

db = cx_Oracle.connect('ADMIN', 'Prudhvi@1997', 'db202005021424_low')

cursor = db.cursor()

read1 = "SELECT * FROM PRODUCT_A_PICK_PLACE order by id ASC "
read2 = "SELECT * FROM PRODUCT_A_SOLDER order by id ASC "
read3 = "SELECT * FROM PRODUCT_A_PARTS order by id ASC "
try:
   
   cursor.execute(read1)
   results1 = cursor.fetchall()
   cursor.execute(read2)
   results2 = cursor.fetchall()
   cursor.execute(read3)
   results3 = cursor.fetchall()
#   print(results) 
#   for row in results:
#      ID = row[0]
#      OPERATIONS = row[1]
#      RFID = row[2]
#      EXECUTED = row[3]
      # Now print fetched result
 #     print ("ID=%d,OPERATIONS=%s,RFID=%s,EXECUTED=%d" % (ID, OPERATIONS, RFID, EXECUTED))

 
   db.commit()
except:
   
   db.rollback()


db.close()
# print("--------------------------------------------------------------")
print(results1)
list = np.array(results1)
list1 = np.array(results2)
list2 = np.array(results3)
print(list2)
# print(list[0,1])
# print(list[1,1])
# print(list[2,1])
# print(list[3,1])
# print(list[4,1])
# print(list[5,1])
# print(list[6,1])
# print(list[7,1])
# print(list[8,1])
# print(list[9,1])
# print(list[10,1])
# print(list[11,1])
# print(list[12,1])
# print("---------------------------------------------soldering--------------------------------")
# print(list1[3,1])
# print(list1[4,1])
# print(list1[5,1])
# print("---------------------------------------------soldering done --------------------------------")
# print(list[13,1])
# print(list[14,1])
# print(list[15,1])
# print(list[16,1])
# print(list[17,1])
# print(list[18,1])
# print(list[19,1])
# print(list[20,1])
# print(list[21,1])
# print("---------------------------------------------soldering--------------------------------")
# print(list1[6,1])
# print(list1[7,1])
# print(list1[8,1])
# print("---------------------------------------------soldering done --------------------------------")


Label(master, text="operation done:").grid(row=0, sticky=W)
var1 = IntVar()

if list[0,1] == list[0,1]:
   var1.set(1)
   print("picking",list2[4,1],"code")
else:
   var1.set(0)
Checkbutton(master, text=list[0,1], variable=var1).grid(row=1, sticky=W)
var2 = IntVar()

if list[1,1] == list[0,1]:
   var2.set(1)
   print(startprogram)
else:
   var2.set(0)
Checkbutton(master, text=list[1,1], variable=var2).grid(row=2, sticky=W)
var3 = IntVar()

if list[2,1] == list[0,1]:
   var3.set(1)
   print(startprogram)
else:
   var3.set(0)
Checkbutton(master, text=list[2,1], variable=var3).grid(row=3, sticky=W)
var4 = IntVar()

if list[2,1] == list[0,1]:
   var4.set(1)
   print(startprogram)
else:
   var4.set(0)
Checkbutton(master, text=list[3,1], variable=var4).grid(row=4, sticky=W)
var5 = IntVar()

if list[2,1] == list[0,1]:
   var5.set(1)
   print(startprogram)
else:
   var5.set(0)
Checkbutton(master, text=list[4,1], variable=var5).grid(row=5, sticky=W)
var6 = IntVar()

if list[2,1] == list[0,1]:
   var6.set(1)
   print(startprogram)
else:
   var6.set(0)
Checkbutton(master, text=list[5,1], variable=var6).grid(row=6, sticky=W)
var7 = IntVar()

if list[2,1] == list[0,1]:
   var7.set(1)
   print(startprogram)
else:
   var7.set(0)
Checkbutton(master, text=list[6,1], variable=var7).grid(row=7, sticky=W)
var8 = IntVar()

if list[2,1] == list[0,1]:
   var8.set(1)
   print(startprogram)
else:
   var8.set(0)
Checkbutton(master, text=list[7,1], variable=var8).grid(row=8, sticky=W)
var9 = IntVar()

if list[2,1] == list[0,1]:
   var9.set(1)
   print(startprogram)
else:
   var9.set(0)
Checkbutton(master, text=list[8,1], variable=var9).grid(row=9, sticky=W)
var10 = IntVar()

if list[2,1] == list[0,1]:
   var10.set(1)
   print(startprogram)
else:
   var10.set(0)
Checkbutton(master, text=list[9,1], variable=var10).grid(row=10, sticky=W)
var11 = IntVar()

if list[2,1] == list[0,1]:
   var11.set(1)
   print(startprogram)
else:
   var11.set(0)
Checkbutton(master, text=list[10,1], variable=var11).grid(row=11, sticky=W)
var12 = IntVar()

if list[2,1] == list[0,1]:
   var12.set(1)
   print(startprogram)
else:
   var12.set(0)
Checkbutton(master, text=list[11,1], variable=var12).grid(row=12, sticky=W)
var13 = IntVar()

if list[0,1] == list[0,1]:
   var13.set(1)
   Label(master, text="soldering").grid(row=25, sticky=W)
   var23 = IntVar()
   if list[0,1] == list[0,1]:
      var23.set(1)
      print("start code here for soldering")
   else:
      var23.set(0)
   Checkbutton(master, text=list1[3,1], variable=var23).grid(row=26, sticky=W)
   var24 = IntVar()
   if list[0,1] == list[0,1]:
      var24.set(1)
      print("start code here for soldering")
   else:
      var24.set(0)
   Checkbutton(master, text=list1[4,1], variable=var24).grid(row=27, sticky=W)
   var25 = IntVar()

   if list[0,1] == list[1,1]:
      var25.set(1)
      print("start code here for soldering")
   else:
      var25.set(0)
   Checkbutton(master, text=list1[5,1], variable=var25).grid(row=28, sticky=W)

else:
   var13.set(0)
Checkbutton(master, text=list[12,1], variable=var13).grid(row=13, sticky=W)
var14 = IntVar()

if list[0,1] == list[0,1]:
   var14.set(1)
   print(startprogram)
else:
   var14.set(0)
Checkbutton(master, text=list[13,1], variable=var14).grid(row=14, sticky=W)
var15 = IntVar()

if list[2,1] == list[0,1]:
   var15.set(1)
   print(startprogram)
else:
   var15.set(0)
Checkbutton(master, text=list[14,1], variable=var15).grid(row=15, sticky=W)
var16 = IntVar()

if list[2,1] == list[0,1]:
   var16.set(1)
   print(startprogram)
else:
   var16.set(0)
Checkbutton(master, text=list[15,1], variable=var16).grid(row=16, sticky=W)
var17 = IntVar()

if list[2,1] == list[0,1]:
   var17.set(1)
   print(startprogram)
else:
   var17.set(0)
Checkbutton(master, text=list[16,1], variable=var17).grid(row=17, sticky=W)
var18 = IntVar()

if list[2,1] == list[0,1]:
   var18.set(1)
   print(startprogram)
else:
   var18.set(0)
Checkbutton(master, text=list[17,1], variable=var18).grid(row=18, sticky=W)
var19 = IntVar()

if list[2,1] == list[0,1]:
   var19.set(1)
   print(startprogram)
else:
   var19.set(0)
Checkbutton(master, text=list[18,1], variable=var19).grid(row=19, sticky=W)
var20 = IntVar()

if list[2,1] == list[0,1]:
   var20.set(1)
   print(startprogram)
else:
   var20.set(0)
Checkbutton(master, text=list[19,1], variable=var20).grid(row=20, sticky=W)
var21 = IntVar()

if list[2,1] == list[0,1]:
   var21.set(1)
   print(startprogram)
else:
   var21.set(0)
Checkbutton(master, text=list[20,1], variable=var21).grid(row=21, sticky=W)
var22 = IntVar()

if list[2,1] == list[0,1]:
   var22.set(1)
   print(startprogram)
else:
   var22.set(0)
Checkbutton(master, text=list[21,1], variable=var22).grid(row=22, sticky=W)

Button(master, text='Show', command=var_states).grid(row=23, sticky=W, pady=4)
Button(master, text='Quit', command=master.quit).grid(row=24, sticky=W, pady=4)

mainloop()