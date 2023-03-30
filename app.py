import os
import win32com.client as win32 
import schedule

# criar um novo arquivo Excel
def ab_o_opera():
    opera = os.startfile("C:\\Users\\anaes\\AppData\\Local\\Programs\\Opera GX\\launcher.exe")
    opera.write("https://www.google.com.br")


ab_o_opera()