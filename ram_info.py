import psutil


# Gather RAM information using psutil library
def get_ram_info():
    ram = psutil.virtual_memory()
    ram_info = {
        "RAM Total": f"{ram.total / (1024 ** 3):.2f} GB",
        "RAM % Used": f"{ram.percent:.2f}%",
    }
    return ram_info
