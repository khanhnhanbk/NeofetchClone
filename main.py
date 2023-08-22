import platform
import os
from tabulate import tabulate

from cpu_info import get_cpu_info, parse_cpu_info
from ram_info import get_ram_info

# Get and parse CPU information
cpu_info = get_cpu_info()
cpu_model, cpu_cores = parse_cpu_info(cpu_info)

# Gather system information using platform library
system_info = {
    "OS": f"{platform.system()} {platform.release()} {platform.architecture()[0]}",
    "User": os.getlogin(),
    "CPU": f"{cpu_model} ({cpu_cores})",  # Formatted CPU info
    **get_ram_info(),
}

# # Print formatted system information
# print("System Information:")
# for key, value in system_info.items():
#     print(f"{key}: {value}")

# Convert system_info to a list of (key, value) pairs
system_info_list = [[key, value] for key, value in system_info.items()]

# Print formatted system information as a table
table = tabulate(
    system_info_list,
    headers=["Attribute", "Value"],
    tablefmt="pretty",
    colalign=("left", "left"),
)
print("System Information:")
print(table)
