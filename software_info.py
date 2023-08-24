import subprocess


def get_installed_software():
    try:
        dpkg_output = subprocess.check_output(["dpkg", "--list"], text=True)
        dpkg_lines = dpkg_output.strip().split("\n")
        software_list = []

        for line in dpkg_lines[5:]:  # Skip header lines
            columns = line.split()
            if len(columns) >= 3:
                package_info = {
                    "Package": columns[1],
                    "Version": columns[2],
                }
                software_list.append(package_info)

        return software_list
    except subprocess.CalledProcessError:
        return []


# software_list = get_installed_software()

# # Print the list of installed software
# for software in software_list:
#     print(f"Package: {software['Package']}")
#     print(f"Version: {software['Version']}")
#     print()
