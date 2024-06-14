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

import requests
import configparser

class AutoLogin:
  LOGINSUCCESS = 3667
  EXISTEDUSER = 479
  LOGOUTFAILED = 421
  
  def __init__(self):
    self.__config = configparser.ConfigParser()
    self.__config.read("config.ini")
    self.username = self.__config["DEFAULT"]["username"]
    self.password = self.__config["DEFAULT"]["password"]

  def login(self):
    data = {
      "username": self.username,
      "password": self.password,
      "pwd": self.password,
      "secret": "true"
    }
    res = requests.post("http://10.99.92.1/webAuth/", data=data)

    return int(res.headers["Content-Length"])

  def logout(self):
    res = requests.get("http://10.99.92.1/logout")
    
    return int(res.headers["Content-Length"])

  def getUsername(self):
    return self.username

  def getPassword(self):
    return self.password