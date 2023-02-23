import openai as ai
import os


def open_file(filepath):
    with open(filepath,'r',encoding='utf-8') as infile:
        return infile.read()


ai.api_key = open_file('key.text')





    