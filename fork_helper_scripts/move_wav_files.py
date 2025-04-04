import os
import shutil

def move_wav_files(source_dir, dest_dir):
    # Check if source and destination directories exist
    if not os.path.exists(source_dir):
        print(f"Source directory {source_dir} does not exist.")
        return
    
    if not os.path.exists(dest_dir):
        print(f"Destination directory {dest_dir} does not exist. Creating it...")
        os.makedirs(dest_dir)
    
    # Get all the .wav files in the source directory
    wav_files = [f for f in os.listdir(source_dir) if f.lower().endswith('.wav')]
    
    # Move each .wav file to the destination directory
    for wav_file in wav_files:
        source_path = os.path.join(source_dir, wav_file)
        dest_path = os.path.join(dest_dir, wav_file)
        
        print(f"Moving {wav_file} from {source_dir} to {dest_dir}")
        shutil.move(source_path, dest_path)
    
    print("All .wav files have been moved.")

# Example usage
source_directory = r'LJSpeech'
destination_directory = r'LJSpeech\wavs'

move_wav_files(source_directory, destination_directory)