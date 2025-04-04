# Define the desired path
desired_path = "tacotron2/LJSpeech/wavs/"  # Change this to your desired path

# Open the input file and output file
input_file_path = "tacotron2\get_dataset\ljs_audio_text_val_filelist_DUMMY.txt"  # Replace with your actual file path
output_file_path = "tacotron2\get_dataset\ljs_audio_text_val_filelist.txt"  # Replace with the desired output file path

with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
    # Iterate through each line in the input file
    for line in infile:
        # Replace 'DUMMY' with the desired path
        new_line = line.replace("DUMMY/", desired_path)
        # Write the modified line to the output file
        outfile.write(new_line)

print(f"Replacement complete. Check {output_file_path} for the updated file.")
