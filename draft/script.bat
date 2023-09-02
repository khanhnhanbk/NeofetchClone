@echo off
setlocal enabledelayedexpansion

:: Define an array of Registry keys to query
set "keys=HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall HKLM\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"

:: Set the output file path
set "outputfile=./output.txt"

:: Clear the output file if it already exists
if exist "%outputfile%" del "%outputfile%"

:: Loop through the Registry keys and append results to the output file
for %%k in (%keys%) do (
    for /f "tokens=*" %%a in ('reg query "%%k" /s') do (
        set "regkey=%%a"
        
        :: Check if the Registry key contains DisplayName, DisplayVersion, and Publisher values
        reg query "!regkey!" /v DisplayName >nul 2>&1 && (
            reg query "!regkey!" /v DisplayVersion >nul 2>&1 && (
                reg query "!regkey!" /v Publisher >nul 2>&1 && (
                
                    :: If all values are present, extract and append them to the output file
                    for /f "tokens=1,*" %%b in ('reg query "!regkey!" /v DisplayName ^| find "REG_SZ"') do (
                        set "DisplayName=%%c"
                    )
                    for /f "tokens=1,*" %%b in ('reg query "!regkey!" /v DisplayVersion ^| find "REG_SZ"') do (
                        set "DisplayVersion=%%c"
                    )
                    for /f "tokens=1,*" %%b in ('reg query "!regkey!" /v Publisher ^| find "REG_SZ"') do (
                        set "Publisher=%%c"
                    )
                    
                    :: Append the extracted information to the output file
                    echo DisplayName: !DisplayName!>>"%outputfile%"
                    echo DisplayVersion: !DisplayVersion!>>"%outputfile%"
                    echo Publisher: !Publisher!>>"%outputfile%"
                    echo.>>"%outputfile%"
                )
            )
        )
    )
)

endlocal
