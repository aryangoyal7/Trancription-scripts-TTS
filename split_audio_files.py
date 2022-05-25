"""
Input .txt file containing labels to create smaller audio chunks
"""
from pydub import AudioSegment

for i in range(1, 176):

    file_path = 'path to the labels file' ## provide path to the labels file
    print(f"Getting labels from file {file_path}")

    audio_path = 'path to load the audio files ' ## provide audio path
    print(f"Loading file {audio_path}")
    audio = AudioSegment.from_wav(audio_path)

    for labels in f:
        labels = labels.strip('\n')
        l = labels.split('\t')
        tmin = float(l[0]) * 1000
        tmax = float(l[1]) * 1000
        file_name = 'wavs/' + l[2] + '.wav'
        newAudio = audio[tmin: tmax]
        newAudio.export(file_name, format='wav')
        print(f"Exported file {file_name} successfully")

