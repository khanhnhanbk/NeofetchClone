import win32com.client
import json


def get_connected_mouse_devices():
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


connected_mouse_devices = get_connected_mouse_devices()

# Print list_devices as JSON
print(json.dumps(connected_mouse_devices, indent=4))
