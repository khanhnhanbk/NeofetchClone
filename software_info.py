import os
import winreg
import csv

# Define an array of Registry keys to query
keys = [
    r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
    r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall",
    r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
]

# Set the output file path as a CSV file
output_file = "./output.csv"

# Create or clear the output CSV file
with open(output_file, "w", newline="") as file:
    csv_writer = csv.writer(file)

    # Write the header row to the CSV file
    csv_writer.writerow(
        ["DisplayName", "DisplayVersion", "Publisher", "InstallDate", "License"]
    )

    # Function to retrieve the value of a specific Registry entry if it exists
    def get_reg_value(key, value_name):
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key) as reg_key:
                value, _ = winreg.QueryValueEx(reg_key, value_name)
                return value
        except FileNotFoundError:
            return None

    # Loop through the Registry keys and append results to the CSV file
    for key in keys:
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key) as main_key:
                subkey_index = 0
                while True:
                    try:
                        subkey_name = winreg.EnumKey(main_key, subkey_index)
                        subkey_path = os.path.join(key, subkey_name)

                        display_name = get_reg_value(subkey_path, "DisplayName")
                        display_version = get_reg_value(subkey_path, "DisplayVersion")
                        publisher = get_reg_value(subkey_path, "Publisher")
                        install_date = get_reg_value(subkey_path, "InstallDate")
                        license = get_reg_value(subkey_path, "License")

                        # Check if the required values exist and write them to the CSV file
                        if display_name and display_version and publisher:
                            csv_writer.writerow(
                                [
                                    display_name,
                                    display_version,
                                    publisher,
                                    install_date,
                                    license,
                                ]
                            )

                        subkey_index += 1
                    except OSError:
                        break
        except FileNotFoundError:
            pass  # Ignore keys that don't exist

print(
    "Registry information has been extracted and saved to 'output.csv' with additional information."
)
