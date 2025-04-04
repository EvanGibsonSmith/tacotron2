
from tacotron2.data_utils import TextMelLoader
from types import SimpleNamespace
import matplotlib.pyplot as plt
import librosa

hparams = SimpleNamespace(
    text_cleaners=['english_cleaners'],
    max_wav_value=32768,
    sampling_rate=22050,
    load_mel_from_disk=False,
    filter_length=1024,
    hop_length=256,
    win_length=1024,
    n_mel_channels=80,
    mel_fmin=0.0,
    mel_fmax=8000.0,
    seed=1234  # Example seed
)

validation_files = r"tacotron2\get_dataset\ljs_audio_text_val_filelist.txt"
trainset = TextMelLoader(validation_files, hparams)

# Get the mel spectrogram and text corresponding to that index
text, mel = trainset[5]

# If `mel` is a PyTorch tensor, you need to move it to CPU and convert to numpy for plotting
mel = mel.squeeze(0).cpu().numpy()  # Remove batch dimension and move to CPU

# Plot the mel spectrogram using librosa.display
plt.figure(figsize=(10, 6))
librosa.display.specshow(mel, x_axis='time', y_axis='mel', cmap='viridis')
plt.colorbar(format='%+2.0f dB')
plt.title(f"Mel Spectrogram - {text}")
plt.show()

# TODO build dataset including mel spec