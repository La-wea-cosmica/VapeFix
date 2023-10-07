import ctypes
import ntplib
import datetime
import time
import os
from console.utils import set_title

set_title("No Bitches?")
print()
print("""
  vFix 1.0
   Script Made By @LaweaCosmica [Discord]
   s/@Haiers For The Method [Yotube]


""")

def sync_with_ntp():
    c = ntplib.NTPClient()
    response = c.request('pool.ntp.org', version=3)
    ntp_time = datetime.datetime.fromtimestamp(response.tx_time)
    return ntp_time

# Get Actual Date From NTP Server
print("[LOG] Starting Script...")
actual_date = sync_with_ntp()
original_date = actual_date

# get a new date
new_Date = datetime.datetime(2022, 10, 2)

# Def The SYSTEMTIME Struct for set the new date
class SYSTEMTIME(ctypes.Structure):
    _fields_ = [("wYear", ctypes.c_uint16),
                ("wMonth", ctypes.c_uint16),
                ("wDayOfWeek", ctypes.c_uint16),
                ("wDay", ctypes.c_uint16),
                ("wHour", ctypes.c_uint16),
                ("wMinute", ctypes.c_uint16),
                ("wSecond", ctypes.c_uint16),
                ("wMilliseconds", ctypes.c_uint16)]

# Create SYSTEMTIME with a new date
new_system_time = SYSTEMTIME(
    new_Date.year,
    new_Date.month,
    new_Date.weekday(),
    new_Date.day,
    actual_date.hour,
    actual_date.minute,
    actual_date.second,
    0
)

# Call SetSystemTime Func
kernel32 = ctypes.WinDLL('kernel32.dll')
kernel32.SetLocalTime(ctypes.byref(new_system_time))

print("[LOG] vFix is Applied! (Working)")
print("Press Enter To Unload vFix (Restore)")
input()
print("[LOG] Unloading vFix...")
actual_date = sync_with_ntp()

# Restore to original
new_system_time2 = SYSTEMTIME(
    original_date.year,
    original_date.month,
    original_date.weekday(),
    original_date.day,
    actual_date.hour,
    actual_date.minute,
    actual_date.second,
    0
)

# Call SetSystemTime Func For Restore Date to Original
kernel32.SetLocalTime(ctypes.byref(new_system_time2))

print("[LOG] vFix Unloaded!")
time.sleep(1.5)
print("[Warning] Closing vFix...")
time.sleep(2.5)
os._exit(0)
