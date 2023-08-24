import win32com.client
import platform


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


def get_connected_mouse_devices_linux():
    pass


def get_connected_mouse_devices():
    if platform.system() == "Linux":
        return get_connected_mouse_devices_linux()
    elif platform.system() == "Windows":
        return get_connected_mouse_devices_window()
    else:
        return []
