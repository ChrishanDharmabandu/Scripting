import os
import subprocess
import shutil
import sys

# Check if the script was run with an argument
if len(sys.argv) < 2:
    print("Usage: autopy.py [input_file]")
    exit(1)

# Get the input file from the command-line argument
input_file = sys.argv[1]

# Check if the specified file exists
if not os.path.isfile(input_file):
    print(f"{input_file} does not exist in the current directory.")
    exit(1)

# Run pyinstaller to create a one-file .exe
subprocess.run(['pyinstaller', '--onefile', input_file])

# Check if the .exe file was created
exe_file = input_file.replace(".py", ".exe")
if os.path.isfile(exe_file):
    print(f"{exe_file} successfully created.")
else:
    print("Failed to create the .exe file.")

# Move all files from the 'dist' folder to the working directory
dist_folder = "dist"
if os.path.exists(dist_folder) and os.path.isdir(dist_folder):
    for item in os.listdir(dist_folder):
        item_path = os.path.join(dist_folder, item)
        if os.path.isfile(item_path):
            os.rename(item_path, item)
    os.rmdir(dist_folder)

# Delete the .spec file
spec_file = input_file.replace(".py", ".spec")
if os.path.exists(spec_file):
    os.remove(spec_file)

# Clean up the 'build' directory and its contents
build_folder = "build"
if os.path.exists(build_folder) and os is not os.path.isdir(build_folder):
    shutil.rmtree(build_folder)

print("Workflow completed. Cleaned up build artifacts.")
