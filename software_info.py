import platform
import subprocess

def get_installed_software_linux():
    try:
        dpkg_output = subprocess.check_output(["dpkg", "--list"], text=True)
        dpkg_lines = dpkg_output.strip().split("\n")[5:]  # Skip header lines
        software_list = []

        for line in dpkg_lines:
            columns = line.split()
            if len(columns) >= 3:
                package_info = {
                    "Package": columns[1],
                    "Version": columns[2],
                }
                software_list.append(package_info)

        return software_list
    except subprocess.CalledProcessError:
        return []

def get_installed_software_windows():
    try:
        powershell_command = "Get-WmiObject -Class Win32_Product | Select-Object Name, Version"
        powershell_output = subprocess.check_output(["powershell", "-Command", powershell_command], text=True)
        powershell_lines = powershell_output.strip().split("\n")
        software_list = []

        for line in powershell_lines[2:]:  # Skip header lines
            columns = line.split()
            if len(columns) >= 2:
                package_info = {
                    "Package": columns[0],
                    "Version": columns[1],
                }
                software_list.append(package_info)

        return software_list
    except subprocess.CalledProcessError:
        return []

def get_installed_software():
    if platform.system() == "Linux":
        return get_installed_software_linux()
    elif platform.system() == "Windows":
        return get_installed_software_windows()
    else:
        return []
