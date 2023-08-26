import platform

# only import win32com.client if on Windows
if platform.system() == "Windows":
    import win32com.client
elif platform.system() == "Linux":
    from pyudev import Context

def get_connected_mouse_devices_linux():
    devices = []
    context = Context()

    list_devices = context.list_devices(subsystem="input")
    # print(list_devices) to see what you can filter on
    for device in list_devices:
        device_name = device.get("NAME")
        if device_name:
            mouse_info = {
                "name": device.get("NAME"),
                "phys": device.get("PHYS"),
                "id": device.get("ID"),
                "properties": device.get("PROPERTIES"),
                # Add more properties you're interested in...
            }
            print(mouse_info)

    return devices


def get_connected_mouse_devices_window():
    mouse_devices = []
    wmi = win32com.client.GetObject("winmgmts:")
    list_devices = wmi.InstancesOf("Win32_PnPEntity")

    for device in list_devices:
        if device.Description and (
            "Mouse" in device.Description or "Pointing Device" in device.Description
        ):
            mouse_info = {
                "Caption": device.Caption,
                "Description": device.Description,
                "Manufacturer": device.Manufacturer,
                "Status": device.Status,
                "DeviceID": device.DeviceID,
                # Add more properties you're interested in...
            }
            mouse_devices.append(mouse_info)

    return mouse_devices


def get_connected_mouse_devices():
    if platform.system() == "Linux":
        return get_connected_mouse_devices_linux()
    elif platform.system() == "Windows":
        return get_connected_mouse_devices_window()
    else:
        return []
