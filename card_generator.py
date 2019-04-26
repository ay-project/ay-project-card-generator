#!/usr/bin/python3
import json
import subtext_generator

def read_input(input_file):
    with open(input_file) as json_file:
        data = json.load(json_file)
        print(data['input'][0]['name'])
        for input_card in data['input']:
            if 'abilities' in input_card['specs']:
                print("Found abilities for {}".format(input_card['id']))
                subtext = subtext_generator.generate(input_card['specs']['abilities'])
                print(subtext)