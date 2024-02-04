import sys  # Import the sys module to access command-line arguments
import os  # Import the os module for file and directory operations
from datetime import date  # Import the date class from the datetime module

# Define a function to rename a file
def rename_file(file_path):
    # Extract the directory and filename from the provided file path
    directory = os.path.dirname(file_path)
    filename = os.path.basename(file_path)

    # Replace spaces in the filename with hyphens
    new_filename = filename.replace(" ", "-")

    # Generate the current date in the format "yymmdd_" and append it to the new filename
    new_filename = date.today().strftime("%y%m%d_") + new_filename

    # Construct the new file path by combining the directory and the modified filename
    new_file_path = os.path.join(directory, new_filename)

    # Rename the file to the new file path
    os.rename(file_path, new_file_path)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Check if command-line arguments are provided
        file_path = sys.argv[1]  # Get the file path from the first command-line argument
        rename_file(file_path)  # Call the rename_file function to rename the file
    else:
        # Print a message if no command-line argument is provided
        print("Please provide a file path as a command-line argument.")
