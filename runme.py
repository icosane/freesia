import subprocess
import os
import sys

script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
print(script_directory+'\hello.exe')
# Use triple quotes string literal to span PowerShell command multiline
STR_CMD = """
$action = New-ScheduledTaskAction -Execute "$env:USERPROFILE\\Documents\\hello.exe" 
$description = "making sure you go to bed on time"
$settings = New-ScheduledTaskSettingsSet -ExecutionTimeLimit (New-TimeSpan -Hours 4)
$taskName = "good night"
$trigger = (0..4).ForEach({ New-ScheduledTaskTrigger -Daily -At "$(0+1*$_):00" })
Register-ScheduledTask -TaskName $taskName -Description $description -Action $action -Settings $settings -Trigger $trigger | Out-Null
"""

# Use a list to make it easier to pass argument to subprocess
listProcess = [
    "powershell.exe",
    "-NoExit",
    "-NoProfile",
    "-Command",
    STR_CMD,
    "Copy-Item -Path {} -Destination $env:USERPROFILE\\Documents\\".format(script_directory+'\\hello.exe')]

# Enjoy the magic
print('^₍ ˶ᵔ ᵕ ᵔ˶ ₎^ all done')
subprocess.run(listProcess, check=True)
