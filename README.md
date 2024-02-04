# Repository Contents

This repository contains the following components:

## Windows Context Menu Scripts
These Python scripts serve as productivity hacks for the Windows context menu. They are compiled into `.exe` files for users who prefer to run them without viewing the source code. However, if you have Python installed on your system, you can still examine the source files.

Once you run these scripts as a service (either via Python or the binary), your context menu in File Explorer will have the script readily available for execution.

## Linux Kernel `dmesg` Logs
In addition, this repository includes a script for managing Linux Kernel `dmesg` logs. The script allows you to filter and save messages based on different log levels.

## Usage

### Clone the Repository
To get started, clone this repository to your local machine:

```bash
git clone https://github.com/ChrishanDharmabandu/Scripting.git
```

### Make Scripts Executable

Navigate to the repository directory and make the Python scripts executable:
```bash
cd YourRepository
chmod +x script1.py script2.py
```

### Run the Scripts

Execute the desired script:
```bash
./script1.sh
```
## Note
### Windows Registry Integration
For improved usability, the scripts have been compiled into .exe files. Follow these steps to integrate them into the Windows Registry context menu and run them as services from the system tray:
- Install Registry Context Menu Item: Run install_registry_context_menu.reg to add the context menu items to the Windows Registry.
- Run the .exe as a Service: Execute the compiled .exe file corresponding to the script you want to use. The .exe will run in the system tray, providing a convenient way to access the script’s functionality.

