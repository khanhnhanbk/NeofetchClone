import subprocess


def get_cpu_info():
    try:
        cpu_info = subprocess.check_output("lscpu", shell=True, text=True)
        return cpu_info
    except subprocess.CalledProcessError:
        return "N/A"


def parse_cpu_info(cpu_info):
    model_name = ""
    core_count = ""
    for line in cpu_info.splitlines():
        if "Model name:" in line:
            model_name = line.split(":")[1].strip()
        elif "CPU(s):" in line:
            core_count = line.split(":")[1].strip()
    return model_name, core_count
