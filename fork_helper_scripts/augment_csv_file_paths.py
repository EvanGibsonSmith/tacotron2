import csv

def add_prefix_to_file_paths(csv_file, output_file):
    # Open the CSV file for reading
    with open(csv_file, 'r') as infile:
        reader = csv.reader(infile, delimiter='|')
        
        # Open the output file to write the modified lines
        with open(output_file, 'w', newline='') as outfile:
            writer = csv.writer(outfile, delimiter='|')
            
            # Loop through each row in the input CSV
            for row in reader:
                if len(row) == 2:  # Ensure the row has exactly 2 columns (file path and description)
                    wav_file = row[0].strip()  # Get the wav file name
                    description = row[1].strip()  # Get the text description
                    
                    # Add the prefix to the wav file name
                    modified_path = f"LJSpeech/wavs/{wav_file}"
                    
                    # Write the modified path and description to the output CSV
                    writer.writerow([modified_path, description])
                else:
                    print(f"Skipping invalid row: {row}")

    print(f"Modified CSV saved to {output_file}")

# Example usage
input_csv = 'LJSpeech\metadata_old_file_paths.csv'  # Path to the original CSV
output_csv = 'LJSpeech\metadata.csv'  # Path to save the modified CSV
add_prefix_to_file_paths(input_csv, output_csv)
