"""
MIT License

Copyright (c) 2024 Nonpawit Pothinil

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from colorama import Fore
import configparser
from utils import AutoLogin

config = configparser.ConfigParser()
app = AutoLogin()

print(Fore.GREEN, """
==============================================
สวัสดียินดีต้อนรับสู่โปรแกรมล็อกอิน WiFi ของ มมส. อัตโนมัติ
            โปรดเลือกออฟชั่นของคุณ
              เวอร์ชั่นปัจจุบัน 1.0
1) เข้าสู่ระบบ
2) ออกจากระบบ
==============================================
""")

try:
  menuChoice = int(input("==> "))
except:
  print("โปรดกรอกเฉพาะตัวเลข")

match menuChoice:
  case 1:
    loginCode = app.login()
    if loginCode == AutoLogin.LOGINSUCCESS:
      print("เข้าสู่ระบบสำเร็จ")
    elif loginCode == AutoLogin.EXISTEDUSER:
      print("มีผู้ใช้งานอยู่เครื่องนี้อยู่แล้ว")
    else:
      print("เข้าสู่ระบบไม่สำเร็จ")
  case 2:
    logoutCode = app.logout()
    if logoutCode == AutoLogin.LOGOUTFAILED:
      print("คุณไม่ได้ใช้งานอยู่ในขณะนี้")
    else:
      print("ออกจากระบบสำเร็จ")
  case _:
    print("โปรดกรอกเฉพาะเลขที่ให้กรอก")