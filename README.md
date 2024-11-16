# Rhino 5 Auto installer

The point of this application is to automate the install and setup of the application.

## Installation & Requirements
- Google Chrome
- Python3
- Pip3
- Selenium
- Webdriver-manager
 
---

Windows:
```
invoke-webrequest -Uri "https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe" -OutFile "C:\temp\python-3.9.6-amd64.exe"
Start -Wait -FilePath "C:\temp\python-3.9.6-amd64.exe"
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
py -m pip install selenium
py -m pip install webdriver-manager
```

Set User Access Control(UAC) to 0:
```
Set-ItemProperty -Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System -Name ConsentPromptBehaviorAdmin -Value 0
```

---

Linux:
```
N/A
```

---

