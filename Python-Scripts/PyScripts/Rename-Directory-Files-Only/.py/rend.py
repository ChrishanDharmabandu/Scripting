import os
import sys
from datetime import date

# Define a function to rename files in the specified directory
def rename_files_in_directory(directory):
    # Loop through the files in the directory
    for filename in os.listdir(directory):
        # Create the full path to the file
        file_path = os.path.join(directory, filename)
        
        # Check if the file_path corresponds to a file (not a directory)
        if os.path.isfile(file_path):
            # Generate a new filename by replacing spaces with hyphens and adding a date prefix
            new_filename = date.today().strftime("%y%m%d_") + filename.replace(" ", "-")
            
            # Create the full path to the new filename
            new_file_path = os.path.join(directory, new_filename)
            
            # Rename the file with the new name
            os.rename(file_path, new_file_path)

if __name__ == "__main__":
    # Check if the script is being run as the main program
    if len(sys.argv) > 1:
        # Get the directory path from the command-line argument
        directory = sys.argv[1]
        
        # Call the function to rename files in the specified directory
        rename_files_in_directory(directory)
    else:
        # Print a message if no command-line argument is provided
        print("Please provide a directory path as a command-line argument.")

