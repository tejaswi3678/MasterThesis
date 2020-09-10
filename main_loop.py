import cx_Oracle
import os
import numpy as np
from tkinter import *
import time
import getpass
from machine1 import *
from machine2 import *
from machine3 import *
from machine4 import *
from machine5 import *
from machine6 import *
from machine7 import *

username = getpass. getuser() 
print(username)

# master = Tk()
os.environ['TNS_ADMIN'] = r"C:\Users\%s\Desktop\RFID\Wallet_DB202005021424"%(username)
db = cx_Oracle.connect('ADMIN', 'Prudhvi@1997', 'db202005021424_low')

startprogram = "starting"
while True:
    
            master = Tk()
            os.environ['TNS_ADMIN'] = r"C:\Users\%s\Desktop\RFID\Wallet_DB202005021424"%(username)

            db = cx_Oracle.connect('ADMIN', 'Prudhvi@1997', 'db202005021424_low')

            cursor = db.cursor()
            PRODUCT_A_PICK_PLACE = "SELECT * FROM PRODUCT_A_PICK_PLACE order by id ASC "
            PRODUCT_A_PICK_PLACE_EXECUTED = "SELECT PRODUCT_A_PICK_PLACE.ID,PRODUCT_A_PICK_PLACE.EXECUTED FROM PRODUCT_A_PICK_PLACE order by id ASC "
            PRODUCT_A_SOLDER = "SELECT * FROM PRODUCT_A_SOLDER order by id ASC "
            PRODUCT_A_PARTS = "SELECT * FROM PRODUCT_A_PARTS order by id ASC "
            PRODUCT_A_PICK_PLACE_UPDATE="update PRODUCT_A_PICK_PLACE set executed='1' where id = list[0:1]"
            try:
            
                cursor.execute(PRODUCT_A_PICK_PLACE)
                results1 = cursor.fetchall()
                cursor.execute(PRODUCT_A_SOLDER)
                results2 = cursor.fetchall()
                cursor.execute(PRODUCT_A_PARTS)
                results3 = cursor.fetchall()
                cursor.execute(PRODUCT_A_PICK_PLACE_EXECUTED)
                results4 = cursor.fetchall()

                db.commit()
            except:
            
                db.rollback()
            db.close()
            list = np.array(results1)
            list1 = np.array(results2)
            list2 = np.array(results3)
            list4 = np.array(results4)
            # print(list4)

            # def var_states():
            #     print("Operations1: %d,\nOperations2: %d,\nOperations3: %d,\nOperations4: %d,\nOperations5: %d,\nOperations6: %d,\nOperations7: %d,\nOperations8: %d,\nOperations9: %d,\nOperations10: %d,\nOperations11: %d,\nOperations12: %d,Operations13: %d,\nOperations14: %d,\nOperations15: %d,\nOperations16: %d,\nOperations17: %d,\nOperations18: %d,\nOperations19: %d,\nOperations20: %d,\nOperations21: %d,\nOperations22: %d" % 
            # (var1.get(), var2.get(),var3.get(), var4.get(),var5.get(), var6.get(),var7.get(), var8.get(),var9.get(), var10.get(),var11.get(), var12.get(),var13.get(), var14.get(),var15.get(), var16.get(),var17.get(), var18.get(),var19.get(), var20.get(),var21.get(), var22.get()))


            Label(master, text="operation done:").grid(row=0, sticky=W)

            var1 = IntVar()
            # print(list[0,0],list1[0,0])
            if list[0,1] == list[0,1]:
                var1.set(1)
                print("picking",list2[4,1],"code")
                os.environ['TNS_ADMIN'] = r"C:\Users\%s\Desktop\RFID\Wallet_DB202005021424"%(username)
                db = cx_Oracle.connect('ADMIN', 'Prudhvi@1997', 'db202005021424_low')
                cursor = db.cursor()
                try:
                    cursor.execute('''UPDATE PRODUCT_A_PICK_PLACE SET EXECUTED = 1 WHERE PRODUCT_A_PICK_PLACE.ID = %s''' %(list[0,0]))
                    db.commit()
                except:
                    db.rollback()
                db.close()
            else:
                var1.set(0)
            Checkbutton(master, text=list[0,1], variable=var1).grid(row=1, sticky=W)
            var2 = IntVar()

            if list[1,1] == list[1,1]:
                var2.set(1)
                print(startprogram)
                os.environ['TNS_ADMIN'] = r"C:\Users\%s\Desktop\RFID\Wallet_DB202005021424"%(username)
                db = cx_Oracle.connect('ADMIN', 'Prudhvi@1997', 'db202005021424_low')
                cursor = db.cursor()
                try:
                    cursor.execute('''UPDATE PRODUCT_A_PICK_PLACE SET EXECUTED = 1 WHERE PRODUCT_A_PICK_PLACE.ID = %s''' %(list[1,0]))
                    db.commit()
                except:
                    db.rollback()
                db.close()
            else:
                var2.set(0)
            Checkbutton(master, text=list[1,1], variable=var2).grid(row=2, sticky=W)
            var3 = IntVar()

            if list[0,1] == list[0,1]:
                var3.set(1)
                print(startprogram)
                os.environ['TNS_ADMIN'] = r"C:\Users\%s\Desktop\RFID\Wallet_DB202005021424"%(username)
                db = cx_Oracle.connect('ADMIN', 'Prudhvi@1997', 'db202005021424_low')
                cursor = db.cursor()
                try:
                    cursor.execute('''UPDATE PRODUCT_A_PICK_PLACE SET EXECUTED = 1 WHERE PRODUCT_A_PICK_PLACE.ID = %s''' %(list[2,0]))
                    db.commit()
                except:
                    db.rollback()
                db.close()
            else:
                var3.set(0)
            Checkbutton(master, text=list[2,1], variable=var3).grid(row=3, sticky=W)
            var4 = IntVar()

            if list[0,1] == list[0,1]:
                var4.set(1)
                print(startprogram)
                fun1()
                os.environ['TNS_ADMIN'] = r"C:\Users\%s\Desktop\RFID\Wallet_DB202005021424"%(username)
                db = cx_Oracle.connect('ADMIN', 'Prudhvi@1997', 'db202005021424_low')
                cursor = db.cursor()
                try:
                    cursor.execute('''UPDATE PRODUCT_A_PICK_PLACE SET EXECUTED = 1 WHERE PRODUCT_A_PICK_PLACE.ID = %s''' %(list[3,0]))
                    db.commit()
                except:
                    db.rollback()
                db.close()
            else:
                var4.set(0)
            Checkbutton(master, text=list[3,1], variable=var4).grid(row=4, sticky=W)
            var5 = IntVar()

            if list[0,1] == list[0,1]:
                var5.set(1)
                print(startprogram)
                fun2()
                os.environ['TNS_ADMIN'] = r"C:\Users\%s\Desktop\RFID\Wallet_DB202005021424"%(username)
                db = cx_Oracle.connect('ADMIN', 'Prudhvi@1997', 'db202005021424_low')
                cursor = db.cursor()
                try:
                    cursor.execute('''UPDATE PRODUCT_A_PICK_PLACE SET EXECUTED = 1 WHERE PRODUCT_A_PICK_PLACE.ID = %s'''%(list[4,0]))
                    db.commit()
                except:
                    db.rollback()
                db.close()
            else:
                var5.set(0)
            Checkbutton(master, text=list[4,1], variable=var5).grid(row=5, sticky=W)
            var6 = IntVar()

            if list[0,1] == list[0,1]:
                var6.set(1)
                print(startprogram)
                fun3()
                os.environ['TNS_ADMIN'] = r"C:\Users\%s\Desktop\RFID\Wallet_DB202005021424"%(username)
                db = cx_Oracle.connect('ADMIN', 'Prudhvi@1997', 'db202005021424_low')
                cursor = db.cursor()
                try:
                    cursor.execute('''UPDATE PRODUCT_A_PICK_PLACE SET EXECUTED = 1 WHERE PRODUCT_A_PICK_PLACE.ID = %s'''%(list[5,0]))
                    db.commit()
                except:
                    db.rollback()
                db.close()
            else:
                var6.set(0)
            Checkbutton(master, text=list[5,1], variable=var6).grid(row=6, sticky=W)
            var7 = IntVar()

            if list[0,1] == list[0,1]:
                var7.set(1)
                print(startprogram)
                fun4()
                os.environ['TNS_ADMIN'] = r"C:\Users\%s\Desktop\RFID\Wallet_DB202005021424"%(username)
                db = cx_Oracle.connect('ADMIN', 'Prudhvi@1997', 'db202005021424_low')
                cursor = db.cursor()
                try:
                    cursor.execute('''UPDATE PRODUCT_A_PICK_PLACE SET EXECUTED = 1 WHERE PRODUCT_A_PICK_PLACE.ID = %s'''%(list[6,0]))
                    db.commit()
                except:
                    db.rollback()
                db.close()
            else:
                var7.set(0)
            Checkbutton(master, text=list[6,1], variable=var7).grid(row=7, sticky=W)
            var8 = IntVar()

            if list[0,1] == list[0,1]:
                var8.set(1)
                print(startprogram)
                fun5()
                os.environ['TNS_ADMIN'] = r"C:\Users\%s\Desktop\RFID\Wallet_DB202005021424"%(username)
                db = cx_Oracle.connect('ADMIN', 'Prudhvi@1997', 'db202005021424_low')
                cursor = db.cursor()
                try:
                    cursor.execute('''UPDATE PRODUCT_A_PICK_PLACE SET EXECUTED = 1 WHERE PRODUCT_A_PICK_PLACE.ID = %s'''%(list[7,0]))
                    db.commit()
                except:
                    db.rollback()
                db.close()
            else:
                var8.set(0)
            Checkbutton(master, text=list[7,1], variable=var8).grid(row=8, sticky=W)
            var9 = IntVar()

            if list[0,1] == list[0,1]:
                var9.set(1)
                print(startprogram)
                fun6()
                os.environ['TNS_ADMIN'] = r"C:\Users\%s\Desktop\RFID\Wallet_DB202005021424"%(username)
                db = cx_Oracle.connect('ADMIN', 'Prudhvi@1997', 'db202005021424_low')
                cursor = db.cursor()
                try:
                    cursor.execute('''UPDATE PRODUCT_A_PICK_PLACE SET EXECUTED = 1 WHERE PRODUCT_A_PICK_PLACE.ID = %s'''%(list[8,0]))
                    db.commit()
                except:
                    db.rollback()
                db.close()
            else:
                var9.set(0)
            Checkbutton(master, text=list[8,1], variable=var9).grid(row=9, sticky=W)
            var10 = IntVar()

            if list[0,1] == list[0,1]:
                var10.set(1)
                print(startprogram)
                fun7()
                os.environ['TNS_ADMIN'] = r"C:\Users\%s\Desktop\RFID\Wallet_DB202005021424"%(username)
                db = cx_Oracle.connect('ADMIN', 'Prudhvi@1997', 'db202005021424_low')
                cursor = db.cursor()
                try:
                    cursor.execute('''UPDATE PRODUCT_A_PICK_PLACE SET EXECUTED = 1 WHERE PRODUCT_A_PICK_PLACE.ID = %s'''%(list[9,0]))
                    db.commit()
                except:
                    db.rollback()
                db.close()
            else:
                var10.set(0)
                Checkbutton(master, text=list[9,1], variable=var10).grid(row=10, sticky=W)
            var11 = IntVar()

            if list[0,1] == list[0,1]:
                var11.set(1)
                print(startprogram)
                fun8()
                os.environ['TNS_ADMIN'] = r"C:\Users\%s\Desktop\RFID\Wallet_DB202005021424"%(username)
                db = cx_Oracle.connect('ADMIN', 'Prudhvi@1997', 'db202005021424_low')
                cursor = db.cursor()
                try:
                    cursor.execute('''UPDATE PRODUCT_A_PICK_PLACE SET EXECUTED = 1 WHERE PRODUCT_A_PICK_PLACE.ID = %s'''%(list[10,0]))
                    db.commit()
                except:
                    db.rollback()
                db.close()
            else:
                var11.set(0)
            Checkbutton(master, text=list[10,1], variable=var11).grid(row=11, sticky=W)
            var12 = IntVar()

            if list[0,1] == list[0,1]:
                var12.set(1)
                print(startprogram)
                fun9()
                os.environ['TNS_ADMIN'] = r"C:\Users\%s\Desktop\RFID\Wallet_DB202005021424"%(username)
                db = cx_Oracle.connect('ADMIN', 'Prudhvi@1997', 'db202005021424_low')
                cursor = db.cursor()
                try:
                    cursor.execute('''UPDATE PRODUCT_A_PICK_PLACE SET EXECUTED = 1 WHERE PRODUCT_A_PICK_PLACE.ID = %s'''%(list[11,0]))
                    db.commit()
                except:
                    db.rollback()
                db.close()
            else:
                var12.set(0)
            Checkbutton(master, text=list[11,1], variable=var12).grid(row=12, sticky=W)
            var13 = IntVar()
            fun10()

            if list[0,0] == list[0,0]:
                var13.set(1)
                os.environ['TNS_ADMIN'] = r"C:\Users\%s\Desktop\RFID\Wallet_DB202005021424"%(username)
                db = cx_Oracle.connect('ADMIN', 'Prudhvi@1997', 'db202005021424_low')
                cursor = db.cursor()
                try:
                    cursor.execute('''UPDATE PRODUCT_A_PICK_PLACE SET EXECUTED = 1 WHERE PRODUCT_A_PICK_PLACE.ID = %s'''%(list[12,0]))
                    db.commit()
                except:
                    db.rollback()
                db.close()
                Label(master, text="soldering").grid(row=25, sticky=W)
                var23 = IntVar()
                if list[0,1] == list[0,1]:
                    var23.set(1)
                    print("start code here for soldering")
                    solder1()
                else:
                    var23.set(0)
                Checkbutton(master, text=list1[3,1], variable=var23).grid(row=26, sticky=W)
                var24 = IntVar()
                if list[0,1] == list[0,1]:
                    var24.set(1)
                    print("start code here for soldering")
                    solder2()
                else:
                    var24.set(0)
                Checkbutton(master, text=list1[4,1], variable=var24).grid(row=27, sticky=W)
                var25 = IntVar()

                if list[1,1] == list[1,1]:
                    var25.set(1)
                    print("start code here for soldering")
                    solder3()
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
                fun11()
                os.environ['TNS_ADMIN'] = r"C:\Users\%s\Desktop\RFID\Wallet_DB202005021424"%(username)
                db = cx_Oracle.connect('ADMIN', 'Prudhvi@1997', 'db202005021424_low')
                cursor = db.cursor()
                try:
                    cursor.execute('''UPDATE PRODUCT_A_PICK_PLACE SET EXECUTED = 1 WHERE PRODUCT_A_PICK_PLACE.ID = %s'''%(list[13,0]))
                    db.commit()
                except:
                    db.rollback()
                db.close()
            else:
                var14.set(0)
            Checkbutton(master, text=list[13,1], variable=var14).grid(row=14, sticky=W)
            var15 = IntVar()

            if list[0,1] == list[0,1]:
                var15.set(1)
                print(startprogram)
                fun12()
                os.environ['TNS_ADMIN'] = r"C:\Users\%s\Desktop\RFID\Wallet_DB202005021424"%(username)
                db = cx_Oracle.connect('ADMIN', 'Prudhvi@1997', 'db202005021424_low')
                cursor = db.cursor()
                try:
                    cursor.execute('''UPDATE PRODUCT_A_PICK_PLACE SET EXECUTED = 1 WHERE PRODUCT_A_PICK_PLACE.ID = %s'''%(list[14,0]))
                    db.commit()
                except:
                    db.rollback()
                db.close()
            else:
                var15.set(0)
            Checkbutton(master, text=list[14,1], variable=var15).grid(row=15, sticky=W)
            var16 = IntVar()

            if list[0,1] == list[0,1]:
                var16.set(1)
                print(startprogram)
                fun13()
                os.environ['TNS_ADMIN'] = r"C:\Users\%s\Desktop\RFID\Wallet_DB202005021424"%(username)
                db = cx_Oracle.connect('ADMIN', 'Prudhvi@1997', 'db202005021424_low')
                cursor = db.cursor()
                try:
                    cursor.execute('''UPDATE PRODUCT_A_PICK_PLACE SET EXECUTED = 1 WHERE PRODUCT_A_PICK_PLACE.ID = %s'''%(list[15,0]))
                    db.commit()
                except:
                    db.rollback()
                db.close()
            else:
                var16.set(0)
            Checkbutton(master, text=list[15,1], variable=var16).grid(row=16, sticky=W)
            var17 = IntVar()

            if list[0,1] == list[0,1]:
                var17.set(1)
                print(startprogram)
                fun14()
                os.environ['TNS_ADMIN'] = r"C:\Users\%s\Desktop\RFID\Wallet_DB202005021424"%(username)
                db = cx_Oracle.connect('ADMIN', 'Prudhvi@1997', 'db202005021424_low')
                cursor = db.cursor()
                try:
                    cursor.execute('''UPDATE PRODUCT_A_PICK_PLACE SET EXECUTED = 1 WHERE PRODUCT_A_PICK_PLACE.ID = %s'''%(list[16,0]))
                    db.commit()
                except:
                    db.rollback()
                db.close()
            else:
                var17.set(0)
            Checkbutton(master, text=list[16,1], variable=var17).grid(row=17, sticky=W)
            var18 = IntVar()

            if list[0,1] == list[0,1]:
                var18.set(1)
                print(startprogram)
                fun15()
                os.environ['TNS_ADMIN'] = r"C:\Users\%s\Desktop\RFID\Wallet_DB202005021424"%(username)
                db = cx_Oracle.connect('ADMIN', 'Prudhvi@1997', 'db202005021424_low')
                cursor = db.cursor()
                try:
                    cursor.execute('''UPDATE PRODUCT_A_PICK_PLACE SET EXECUTED = 1 WHERE PRODUCT_A_PICK_PLACE.ID = %s'''%(list[17,0]))
                    db.commit()
                except:
                    db.rollback()
                db.close()
            else:
                var18.set(0)
            Checkbutton(master, text=list[17,1], variable=var18).grid(row=18, sticky=W)
            var19 = IntVar()

            if list[0,1] == list[0,1]:
                var19.set(1)
                print(startprogram)
                fun16()
                os.environ['TNS_ADMIN'] = r"C:\Users\%s\Desktop\RFID\Wallet_DB202005021424"%(username)
                db = cx_Oracle.connect('ADMIN', 'Prudhvi@1997', 'db202005021424_low')
                cursor = db.cursor()
                try:
                    cursor.execute('''UPDATE PRODUCT_A_PICK_PLACE SET EXECUTED = 1 WHERE PRODUCT_A_PICK_PLACE.ID = %s'''%(list[18,0]))
                    db.commit()
                except:
                    db.rollback()
                db.close()
            else:
                var19.set(0)
            Checkbutton(master, text=list[18,1], variable=var19).grid(row=19, sticky=W)
            var20 = IntVar()

            if list[0,1] == list[0,1]:
                var20.set(1)
                print(startprogram)
                fun17()
                os.environ['TNS_ADMIN'] = r"C:\Users\%s\Desktop\RFID\Wallet_DB202005021424"%(username)
                db = cx_Oracle.connect('ADMIN', 'Prudhvi@1997', 'db202005021424_low')
                cursor = db.cursor()
                try:
                    cursor.execute('''UPDATE PRODUCT_A_PICK_PLACE SET EXECUTED = 1 WHERE PRODUCT_A_PICK_PLACE.ID = %s'''%(list[19,0]))
                except:
                    db.rollback()
                db.close()
            else:
                var20.set(0)
            Checkbutton(master, text=list[19,1], variable=var20).grid(row=20, sticky=W)
            var21 = IntVar()

            if list[0,1] == list[0,1]:
                var21.set(1)
                print(startprogram)
                fun18()
                os.environ['TNS_ADMIN'] = r"C:\Users\%s\Desktop\RFID\Wallet_DB202005021424"%(username)
                db = cx_Oracle.connect('ADMIN', 'Prudhvi@1997', 'db202005021424_low')
                cursor = db.cursor()
                try:
                    cursor.execute('''UPDATE PRODUCT_A_PICK_PLACE SET EXECUTED = 1 WHERE PRODUCT_A_PICK_PLACE.ID = %s'''%(list[20,0]))
                    db.commit()
                except:
                    db.rollback()
                db.close()
            else:
                var21.set(0)
            Checkbutton(master, text=list[20,1], variable=var21).grid(row=21, sticky=W)
            var22 = IntVar()
            
            if list[21,0] == list[21,0]:
                var22.set(1)
                fun19()
                os.environ['TNS_ADMIN'] = r"C:\Users\%s\Desktop\RFID\Wallet_DB202005021424"%(username)
                db = cx_Oracle.connect('ADMIN', 'Prudhvi@1997', 'db202005021424_low')
                cursor = db.cursor()
                try:
                    cursor.execute('''UPDATE PRODUCT_A_PICK_PLACE SET EXECUTED = 1 WHERE PRODUCT_A_PICK_PLACE.ID = %s'''%(list[21,0]))
                    db.commit()
                except:
                    db.rollback()
                db.close()
                var26 = IntVar()
                if list[0,1] == list[0,1]:
                    var26.set(1)
                    import machine1
                    print("start code here for soldering")
                    solder4()
                else:
                    var26.set(0)
                # Checkbutton(master, text=list1[6,1], variable=var26).grid(row=29, sticky=W)
                var27 = IntVar()
                if list[0,1] == list[0,1]:
                    var27.set(1)
                    print("start code here for soldering")
                    solder5()
                else:
                    var27.set(0)
                Checkbutton(master, text=list1[7,1], variable=var27).grid(row=30, sticky=W)
                var28 = IntVar()

                if list[0,1] == list[0,1]:
                    var28.set(1)
                    print("start code here for soldering")
                    solder6()
                else:
                    var28.set(0)
                Checkbutton(master, text=list1[8,1], variable=var28).grid(row=31, sticky=W)
                print(startprogram)
            else:
                var22.set(0)
            Checkbutton(master, text=list[21,1], variable=var22).grid(row=22, sticky=W)


            # Button(master, text='Show', command=var_states).grid(row=23, sticky=W, pady=4)
            Button(master, text='Quit', command=master.quit).grid(row=24, sticky=W, pady=4)
            
            print("Reset")
            os.environ['TNS_ADMIN'] = r"C:\Users\%s\Desktop\RFID\Wallet_DB202005021424"%(username)
            db = cx_Oracle.connect('ADMIN', 'Prudhvi@1997', 'db202005021424_low')
            cursor = db.cursor()
            try:
                cursor.execute('''UPDATE PRODUCT_A_PICK_PLACE SET EXECUTED = 0 ''')
                db.commit()
            except:
                db.rollback()
            db.close()
            mainloop()


