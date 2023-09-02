import subprocess
import platform

def get_cpu_info():
    try:
        system_platform = platform.system()
        if system_platform == "Linux":
            cpu_info = subprocess.check_output("lscpu", shell=True, text=True)
        elif system_platform == "Windows":
            cpu_info = subprocess.check_output("wmic cpu get caption, NumberOfCores", shell=True, text=True)
        else:
            return "N/A"
        
        return cpu_info
    except subprocess.CalledProcessError:
        return "N/A"

def parse_cpu_info(cpu_info):
    model_name = ""
    core_count = ""

    if platform.system() == "Linux":
        for line in cpu_info.splitlines():
            if "Model name:" in line:
                model_name = line.split(":")[1].strip()
            elif "CPU(s):" in line:
                core_count = line.split(":")[1].strip()
    elif platform.system() == "Windows":
        lines = cpu_info.strip().split("\n")
        for line in lines[1:]:  # Skip the header row
            parts = line.strip().split()
            if len(parts) >=2:
                model_name = " ".join(parts[0:6]) 
                core_count = parts[7]

    return model_name, core_count

