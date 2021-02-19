import time
import traceback
import win32api
import ctypes, sys
import ntplib
import time
try:
	x = ntplib.NTPClient()
	timeStamp = x.request('uk.pool.ntp.org').tx_time
	dateData = time.strftime("%Y %m %d %H %M %S", time.localtime(timeStamp))
	year = time.strftime("%Y", time.localtime(timeStamp))
	year,mouth,day,hour,minutes,second = dateData.split()
	year,mouth,day,hour,minutes,second = int(year),int(mouth),int(day),int(hour),int(minutes),int(second)
	def is_admin():
		try:
			return ctypes.windll.shell32.IsUserAnAdmin()
		except:
			return False
	if is_admin():
		win32api.SetSystemTime(year,mouth,3,day,hour-8,minutes,second,0)
	else:
		ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
except:
	traceback.print_exc()
finally:
	time.sleep(10)
