# audio-reader
Эта программа преобразует музыку в различные математические представления, такие как волновая форма (waveform), спектрограмма, мел-спектрограмма и MFCC (Mel Frequency Cepstral Coefficients)

This program converts music into various mathematical representations such as waveform, spectrogram, chalk spectrogram and MFCC (Mel Frequency Cepstral Coefficients)

# Программа для создания математического представления музыки

## Описание
Эта программа преобразует аудиофайлы (форматы MP3, WAV) в математические представления, такие как волновая форма, спектрограмма, мел-спектрограмма и MFCC (Mel Frequency Cepstral Coefficients). Результаты сохраняются в виде изображений и CSV-файлов для дальнейшего анализа и интерпретации.

## Обоснование
Программа полезна для исследователей, музыкантов, звукорежиссеров и разработчиков ИИ, которым необходимо анализировать музыку на более глубоком уровне. С ее помощью можно визуализировать аудиосигнал, выявлять его структуру и особенности, а также создавать основу для задач машинного обучения, таких как распознавание жанров, идентификация инструментов или синтез звука.

## Установка и запуск
1. Установите необходимые библиотеки:
    ```bash
    pip install librosa numpy matplotlib scipy
    ```

2. ⚠ Создайте две папки **queue** и **processed** в той же директории, где находится скрипт. Папка **queue** предназначена для добавления файлов, которые будут обработаны. Если папка **queue** не существует, программа не сможет начать обработку! ⚠

3. Поместите аудиофайлы в папку **queue**.

4. Запустите скрипт:
    ```bash
    python converter.py
    ```

## Как работает программа
- Программа ищет все аудиофайлы в папке **queue** и обрабатывает их, создавая различные математические представления звука.
- После обработки файлы перемещаются в папку **processed**, чтобы избежать повторной обработки.

## Результаты
После завершения работы скрипта, результаты будут сохранены в папке **output_data**. Каждому аудиофайлу будет соответствовать отдельная папка с данными, включая волновую форму, спектрограмму, мел-спектрограмму и MFCC.

## Важно!
**Обязательно создайте папку queue и добавьте в неё файлы перед запуском программы!** Это критически важный шаг для корректной работы скрипта.



# Program for Creating Mathematical Representations of Music

## Description
This program converts audio files (MP3, WAV formats) into mathematical representations such as waveform, spectrogram, mel-spectrogram, and MFCC (Mel Frequency Cepstral Coefficients). The results are saved as images and CSV files for further analysis and interpretation.

## Justification
This program is useful for researchers, musicians, sound engineers, and AI developers who need to analyze music at a deeper level. It allows visualizing audio signals, identifying their structure and features, and creating a foundation for machine learning tasks such as genre recognition, instrument identification, or sound synthesis.

## Installation and Execution
1. Install the required libraries:
    ```bash
    pip install librosa numpy matplotlib scipy
    ```

2. ⚠ Create two folders **queue** and **processed** in the same directory as the script. The **queue** folder is intended for adding files to be processed. If the **queue** folder does not exist, the program cannot start processing! ⚠

3. Place audio files in the **queue** folder.

4. Run the script:
    ```bash
    python converter.py
    ```

## How the Program Works
- The program searches for all audio files in the **queue** folder and processes them, creating various mathematical representations of the sound.
- After processing, the files are moved to the **processed** folder to avoid re-processing.

## Results
After the script completes, the results will be saved in the **output_data** folder. Each audio file will have its own folder containing data, including waveform, spectrogram, mel-spectrogram, and MFCC.

## Important!
**Be sure to create the queue folder and add files to it before running the program!** This is a critical step for the correct operation of the script.
