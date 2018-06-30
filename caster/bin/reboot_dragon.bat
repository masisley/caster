taskkill /IM natspeak.exe /f /s localhost
taskkill /IM dgnuiasvr_x64.exe /f /s localhost
taskkill /IM dnsspserver.exe /f /s localhost
taskkill /IM dragonbar.exe /f /s localhost
timeout 3
start "" "C:\Program Files (x86)\Nuance\NaturallySpeaking15\Program\natspeak.exe"