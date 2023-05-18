Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "run_main.bat" & chr(34), 0
Set WshShell = Nothing
