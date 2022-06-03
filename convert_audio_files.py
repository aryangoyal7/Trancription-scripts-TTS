import os
import wave
#Also need ffmpeg installed

can_scan = False
folder_name = ''  #folder containing all the wav files to be checked/preprossed
folder_path = f'{folder_name}/'

if os.path.isdir(folder_path):
  print(f'Folder name set to {folder_name}.')
  can_scan = True
else:
  print('Invalid folder path.')


if can_scan == True:
  resample_list = []
  for file_name in os.listdir(folder_path):
    if(file_name[-4:] != '.wav'): continue
    with wave.open(folder_path + file_name, "rb") as wave_file:
        frame_rate = wave_file.getframerate()
        channels = wave_file.getnchannels()
        if frame_rate == 22050 and channels == 1:
          print(f'{file_name} does not require resampling.')
        else:
          print(f'{file_name} requires resampling.')
          resample_list.append(file_name)
else:
  print('Please provide a valid folder path!!')

if len(resample_list) > 0:
  need_to_resample = True
  print(f'\nScan completed. Please continue to resample {len(resample_list)} file(s).')
else:
  print('\nThere are no files to resample.')
  need_to_resample = False

if need_to_resample == False:
  print('There is nothing to resample.')
  exit()

new_rate = 22050
new_folder = 'temp/' #folder to store all the resampled files

for item in resample_list:
  os.system(f'ffmpeg -y -i {folder_path}{item} -ar {new_rate} -ac 1 {folder_path}{new_folder}{item}') # Converts to Mono also
  print(f'Resampled file {item}.')