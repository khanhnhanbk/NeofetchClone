import platform
import os
import subprocess
import psutil


# Gather CPU information using subprocess library
def get_cpu_info():
    try:
        cpu_info = subprocess.check_output("lscpu", shell=True, text=True)
        return cpu_info
    except subprocess.CalledProcessError:
        return "N/A"


# Parse CPU model and core count from CPU information
def parse_cpu_info(cpu_info):
    model_name = ""
    core_count = ""
    for line in cpu_info.splitlines():
        if "Model name:" in line:
            model_name = line.split(":")[1].strip()
        elif "CPU(s):" in line:
            core_count = line.split(":")[1].strip()
    return model_name, core_count


# Gather RAM information using psutil library
def get_ram_info():
    ram = psutil.virtual_memory()
    ram_info = {
        "RAM Total": f"{ram.total / (1024 ** 3):.2f} GB",
        "RAM Percentage Used": f"{ram.percent:.2f}%",
    }
    return ram_info


# Gather system information using platform library
system_info = {
    "OS": platform.system(),
    "Release": platform.release(),
    "Version": platform.version(),
    "Architecture": platform.architecture()[0],
    "User": os.getlogin(),
    "Home Dir": os.path.expanduser("~"),
    **get_ram_info(),
}

# Get and parse CPU information
cpu_info = get_cpu_info()
cpu_model, cpu_cores = parse_cpu_info(cpu_info)
system_info["CPU"] = f"Intel {cpu_model} ({cpu_cores}) @ 4.200GHz"  # Formatted CPU info

# Print formatted system information
print("System Information:")
for key, value in system_info.items():
    print(f"{key}: {value}")
