import platform
import os
from tabulate import tabulate

from cpu_info import get_cpu_info, parse_cpu_info
from ram_info import get_ram_info
from disk_info import get_disk_info
from software_info import get_installed_software

cpu_info = get_cpu_info()
cpu_model, cpu_cores = parse_cpu_info(cpu_info)

system_info = {
    "OS": f"{platform.system()} {platform.release()} {platform.architecture()[0]}",
    "User": os.getlogin(),
    "CPU": f"{cpu_model} ({cpu_cores})",
    **get_ram_info(),
}
disk_info = get_disk_info()  # Fetch disk information

# Convert disk_info to a list of lists for tabulate
disk_table = []
for disk in disk_info:
    disk_table.append(
        [
            disk["Device"],
            disk["Total Space"],
            disk["Used Space"],
            disk["Free Space"],
            disk["Usage Percentage"],
        ]
    )

# Construct the table for system information
system_info_list = [[key, value] for key, value in system_info.items()]

# Construct the table for system information
system_info_table = tabulate(
    system_info_list,
    headers=["Attribute", "Value"],
    tablefmt="pretty",
    colalign=("left", "left"),
)

# Construct the table for disk information
disk_table_str = tabulate(
    disk_table,
    headers=[
        "Device",
        "Total",
        "Used",
        "Free",
        "Percentage",
    ],
    tablefmt="pretty",
)

# Print the combined system information and disk information tables
print("System Information:")
print(system_info_table)
print("\nDisk Information:")
print(disk_table_str)

# Print the list of installed software
software_list = get_installed_software()

software_table = []
for software in software_list:
    software_table.append(
        [
            software["Package"],
            software["Version"],
        ]
    )

software_table_str = tabulate(
    software_table,
    headers=[
        "Package",
        "Version",
    ],
    tablefmt="pretty",
)

print("\nInstalled Software:")
print(software_table_str)
