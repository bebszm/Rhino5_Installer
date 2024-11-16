## This script will install Rhinoceros 5 and edit the ini file.

# Edit these
$userName = "USER_NAME"
$companyName = "COMPANY_NAME"

# Rhino 5 Key
$key = "0000-0000-0000-0000-0000-0000"

# CHANGE ME
$installPath = "C:\temp\Rhino 5"

$msiName = "rhino5setup_en-us_x64.msi"

function Edit_Setupini {
# Setup ini location
$file = Get-Content -Path $installPath\src\Setup.ini -Raw

# regex Username and Companyname to whatever the variable is
$str = $file.Replace("# USERNAME=Joe Smith", "USERNAME=" + $userName)
$str = $str.Replace("# COMPANYNAME=Acme Construction, Inc.", "COMPANYNAME=" +$companyName)
$str = $str.Replace("# RMA_CDKEY=RH50-____-____-____-____ # Your CD-Key", "RMA_CDKEY=" +$key)

# Save file
$str | Set-Content -Path $installPath\src\Setup.ini
}
 
function Register_app {
# Setup Rhino 5
Start-Process -FilePath "msiexec.exe" -ArgumentList "/i `"$installPath\src\$msiName`" INSTALLDIR=`"C:\Program Files\Rhinoceros 5`" RMA_CDKEY=$key INSTALL_EN=1 INSTALL_DE=1 INSTALL_FR=1 /qb" -Wait
}

Register_app
Edit_Setupini


