# Windows 開機自動更新系統時
用於同一台電腦,兩個不同OS之間切換後,windows時間的不準確問題

    要有win32api, 現在看回來要安裝的是
    pip install pywin32

    另外要在[工作排程器]加入任務,注意有安裝不同版本的python 時要看清楚pip安裝到哪一個版本的python去,
    還有[工作排程器]使用admin運行此任務
---------------------------------------------------------------------------------------------
    
    the prohram is use to sync your windows OS on every turn on,
    if you are a developer you may own 2 OS, linux and windows.
    when you from linux to windows the whindows-system-time will be change
    
    you must own [win32api]
    pip install pywin32
