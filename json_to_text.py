"""
Takes input the json file downloaded from AWS Transcribe
Ouputs a txt file consisting of all the words and punctuations in the transcript along with their start and end times corresponding to the input audio file.
"""

import os
import sys
import json

json_obj = None

totalInputs = 176
# loops over all the files
for i in range(1, totalInputs):

    input_json_path = 'path to json file'

    # if 'json' not in input_json_path:
    #     print("Please provide valid json path")
    #     sys.exit(1)

    output_text_path = input_json_path[:-4]+'txt'

    with open(input_json_path, 'r') as f:
        json_obj = json.load(f)

    text = ""
    line = ""
    st, et = 0, 0
    for i in range(len(json_obj["results"]['items'])):
        word_dict = json_obj["results"]['items'][i]
        if word_dict["type"]=="punctuation":
            sent = word_dict['alternatives'][0]['content']
            line = "{}\t{}\t{}\n".format(sent, et,et)
        elif word_dict["type"]=="pronunciation":
            words = []
            for w in word_dict['alternatives']:
                words.append(w['content'])
            sent=" ".join(words)
            st = float(word_dict['start_time'])
            et = float(word_dict['end_time'])
            line = "{}\t{}\t{}\n".format(sent, st,et)
        text += line

    print("output path:",output_text_path)
    with open(output_text_path, 'w') as f:
        f.write(text)
