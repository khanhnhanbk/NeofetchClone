import subprocess
import psutil


def get_all_disk_info():
    disk_info = []
    try:
        df_output = subprocess.check_output(
            ["df", "--output=source,size,used,avail,pcent,fstype", "--block-size=G"],
            text=True,
        )
        df_lines = df_output.strip().split("\n")
        for line in df_lines[1:]:  # Skip the header line
            columns = line.split()
            if len(columns) == 6:
                disk = {
                    "Device": columns[0],
                    "Size": columns[1],
                    "Used Space": columns[2],
                    "Free Space": columns[3],
                    "Usage Percentage": columns[4],
                    "File System": columns[5],
                }
                disk_info.append(disk)
    except subprocess.CalledProcessError:
        pass  # Handle the error or logging here
    return disk_info


def get_disk_info():
    partitions = psutil.disk_partitions()
    disk_info = []

    for partition in partitions:
        partition_info = {
            "Device": partition.device,
            "Mount Point": partition.mountpoint,
        }
        usage = psutil.disk_usage(partition.mountpoint)
        partition_info["Total Space"] = f"{usage.total / (1024 ** 3):.2f} GB"
        partition_info["Used Space"] = f"{usage.used / (1024 ** 3):.2f} GB"
        partition_info["Free Space"] = f"{usage.free / (1024 ** 3):.2f} GB"
        partition_info["Usage Percentage"] = f"{usage.percent:.2f}%"
        disk_info.append(partition_info)

    return disk_info
