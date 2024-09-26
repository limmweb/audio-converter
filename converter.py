import librosa
import numpy as np
import matplotlib.pyplot as plt
import os
import csv
import shutil

# Функция для сохранения волновой формы аудиофайла
def save_waveform(audio_data, sr, output_folder):
    waveform_file = os.path.join(output_folder, 'waveform.csv')
    with open(waveform_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Time', 'Amplitude'])
        for i, sample in enumerate(audio_data):
            writer.writerow([i / sr, sample])
    print(f'Waveform saved to {waveform_file}')

# Функция для сохранения спектрограммы аудиофайла
def save_spectrogram(audio_data, sr, output_folder):
    spectrogram = np.abs(librosa.stft(audio_data))
    spectrogram_db = librosa.amplitude_to_db(spectrogram, ref=np.max)
    
    plt.figure(figsize=(10, 6))
    librosa.display.specshow(spectrogram_db, sr=sr, x_axis='time', y_axis='log')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Spectrogram')
    spectrogram_img = os.path.join(output_folder, 'spectrogram.png')
    plt.savefig(spectrogram_img)
    plt.close()
    print(f'Spectrogram saved to {spectrogram_img}')

# Функция для сохранения мел-спектрограммы аудиофайла
def save_mel_spectrogram(audio_data, sr, output_folder):
    mel_spectrogram = librosa.feature.melspectrogram(y=audio_data, sr=sr)
    mel_spectrogram_db = librosa.power_to_db(mel_spectrogram, ref=np.max)
    
    plt.figure(figsize=(10, 6))
    librosa.display.specshow(mel_spectrogram_db, sr=sr, x_axis='time', y_axis='mel')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Mel Spectrogram')
    mel_spectrogram_img = os.path.join(output_folder, 'mel_spectrogram.png')
    plt.savefig(mel_spectrogram_img)
    plt.close()
    print(f'Mel Spectrogram saved to {mel_spectrogram_img}')

# Функция для сохранения MFCC аудиофайла
def save_mfcc(audio_data, sr, output_folder):
    mfccs = librosa.feature.mfcc(y=audio_data, sr=sr, n_mfcc=13)
    
    mfcc_file = os.path.join(output_folder, 'mfcc.csv')
    with open(mfcc_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['MFCC_' + str(i) for i in range(mfccs.shape[0])])
        for frame in mfccs.T:
            writer.writerow(frame)
    print(f'MFCC saved to {mfcc_file}')

# Основная функция для обработки аудиофайла
def process_audio_file(file_path, output_folder):
    # Загружаем аудиофайл
    audio_data, sr = librosa.load(file_path, sr=None)
    
    # Создаем выходную папку для файла
    output_folder = os.path.join(output_folder, os.path.basename(file_path).split('.')[0])
    os.makedirs(output_folder, exist_ok=True)
    
    # Сохраняем различные представления аудиофайла
    save_waveform(audio_data, sr, output_folder)
    save_spectrogram(audio_data, sr, output_folder)
    save_mel_spectrogram(audio_data, sr, output_folder)
    save_mfcc(audio_data, sr, output_folder)

# Функция для обработки всех аудиофайлов в папке queue
def process_all_files():
    queue_folder = 'queue'
    processed_folder = 'processed'
    
    # Создаем папки, если их нет
    os.makedirs(queue_folder, exist_ok=True)
    os.makedirs(processed_folder, exist_ok=True)
    
    # Получаем список всех MP3 и WAV файлов в папке queue
    audio_files = [f for f in os.listdir(queue_folder) if f.lower().endswith(('.mp3', '.wav'))]
    
    if not audio_files:
        print("No audio files found in the queue folder.")
        return
    
    # Обрабатываем каждый файл
    for file_name in audio_files:
        file_path = os.path.join(queue_folder, file_name)
        print(f"Processing {file_name}...")
        
        # Обрабатываем файл и сохраняем результаты
        process_audio_file(file_path, 'output_data')
        
        # Перемещаем обработанный файл в папку processed
        shutil.move(file_path, os.path.join(processed_folder, file_name))
        print(f"Moved {file_name} to processed folder.")

if __name__ == "__main__":
    process_all_files()
