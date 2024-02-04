#!/bin/bash

# Define the target directory with an absolute path under the user's home directory
target_dir="$HOME/Documents/Linux-Kernel-Logs"

# Create the target directory if it doesn't exist
sudo mkdir -p "$target_dir"
sudo chown $USER:$USER "$target_dir"  # Ensure the target directory is owned by your user

# Get the current date and time in the desired format
timestamp=$(date "+%y%m%d_%H%M%S")

# Get the kernel version
kernel_version=$(uname -r)

# Create a subdirectory with the specified naming convention under the target directory
subdir_name="${timestamp}_Kernel${kernel_version}"
subdir_path="$target_dir/$subdir_name"
sudo mkdir -p "$subdir_path"
sudo chown $USER:$USER "$subdir_path"  # Ensure the subdirectory is owned by your user

# Function to dump messages based on log level
dump_messages() {
    log_level=$1
    log_file="$subdir_path/dmesg_${log_level}.log"

    # Run the dmesg command with sudo and save the output to a file
    sudo dmesg -t -l "$log_level" > "$log_file"

    echo "Messages with $log_level log level saved to: $log_file"
}

# Execute operations for each log level
dump_messages emerg
dump_messages crit
dump_messages alert
dump_messages err
dump_messages warn
# 'k' is not a valid log level, removing it
# dump_messages k
dump_messages

echo "Operation completed successfully."

# Prompt the user to change into the created directory
echo -e "\nYou can change into the created directory by running the following command:"
echo "cd $subdir_path"

# Wait for user input before exiting
read -p "Press Enter to continue..."

