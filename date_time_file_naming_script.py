import os
import datetime
import time

directory_path = r"C:\Users\Heron\Desktop\Shoes"  # Replace with your directory

for entry_name in os.listdir(directory_path):
    file_path = os.path.join(directory_path, entry_name) # Specify the path to your file

    try:
        # Get the file creation timestamp (in seconds since the epoch)
        # On Windows, os.path.getctime() returns the creation time.
        # On Unix-like systems (like macOS, Linux), it returns the last metadata change time.
        creation_timestamp = os.path.getctime(file_path)

        # Convert the timestamp to a datetime object for better readability
        creation_datetime = datetime.datetime.fromtimestamp(creation_timestamp)

        # Print the creation date and time
        print(f"File '{file_path}' was created on: {creation_datetime}")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    os.rename(file_path, creation_datetime)

    if os.path.isfile(file_path):
        print(f"File: {entry_name}")
