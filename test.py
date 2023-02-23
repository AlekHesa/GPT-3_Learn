import openai as ai
import os


def open_file(filepath):
    with open(filepath,'r',encoding='utf-8') as infile:
        return infile.read()


ai.api_key = open_file('key.txt')

def gpt3_completion(prompt,engine ='text-davinci-003',temp = 0.7,tokens = 100,top_p = 1.0,freq_pen = 0.0,pres_pen = 0.0,stop=["'<<END>>"]):
    prompt = prompt.encode(encoding='ASCII',errors='ignore').decode()
    response = ai.Completion.create(
        engine = engine,
        prompt = prompt,
        temperature = temp,
        max_tokens = tokens,
        top_p = top_p,
        frequency_penalty = freq_pen,
        presence_penalty = pres_pen,
        stop= stop
    )
    text = response['choices'][0]['text'].strip()
    return text

if __name__ == '__main__':
    promptt = 'write me a list of famous American actors: '
    response = gpt3_completion(promptt)
    print(response)



    