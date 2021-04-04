import re
import csv

files = [
    "Path_to_input_file",
    "Path_to_input_file_2"
]

for file_path in files:
    # Open txt file for parsing
    with open(file_path, "r") as file:
        # Split file number from path and append .csv to get output name
        csv_name = file_path.split(' ')[0].replace("/", "_") + ".csv"
        csv_header = ["Filename", "ID#", "Name", "R.Time", "Area", "Height", "Conc.", "Curve", "3rd", "2nd", "1st", "Constant",
                      "Area Ratio", "Height Ratio", "Conc. %", "Norm Conc."]

        # Open csv out file
        with open(csv_name, "w", newline='',) as csv_file:
            # Setup csv writer
            csv_writer = csv.writer(csv_file)
            # Write CSV header to file
            csv_writer.writerow(csv_header)

            # Read file as one big string blob
            file_content = file.readlines()

            is_data_line = False
            data_file_name = ""

            for line in file_content:
                # Strip trailing/leading whitespaces and newlines from line
                line = line.strip()
                # Skip empty lines before [Header]
                if len(line) == 0:
                    # Save cpu cycles :)
                    continue
                # Set current data file name
                if "Data File Name" in line:
                    # Replace "Data File Name" with empty string
                    data_file_name = line.replace("Data File Name", "")
                    # Save cpu cycles :)
                    continue

                # Set is_data_line to treat following lines as data
                if "ID#" in line:
                    is_data_line = True
                    # Save cpu cycles :)
                    continue

                # Stop treating lines as data
                if "[Header]" in line:
                    is_data_line = False
                    # Save cpu cycles :)
                    continue

                # Write data to file
                if is_data_line:
                    # Split data on tabs (and remove trailing newlines)
                    splits = re.split('\t', line)
                    # Add data_file_name before other values
                    splits.insert(0, data_file_name)
                    # Write to file
                    csv_writer.writerow(splits)
