import time
import traceback
import win32api
import ctypes, sys
import ntplib
import time
try:
	x = ntplib.NTPClient()
	# timeStamp = x.request('uk.pool.ntp.org').tx_time
	timeStamp = x.request('uk.pool.ntp.org').tx_time  # get the time in uk server
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
		print((year,mouth,3,day,hour,minutes,second,0))
		if hour<8: # hong kone time zone is +8
			hour = hour + 16  # 16 is = 24 - 8
			day = day - 1 # you may change here too , if your time zone >= +1 use -1 day, if your time zone <= -1 use +1 day ?
		else:
			print('else')
			hour = hour - 8
		win32api.SetSystemTime(year,mouth,3,day,hour,minutes,second,0)
		# win32api.SetSystemTime(year,mouth,3,day,hour-8,minutes,second,0)
	else:
		ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
except:
	traceback.print_exc()
finally:
	time.sleep(3)
