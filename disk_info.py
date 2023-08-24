import psutil


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
