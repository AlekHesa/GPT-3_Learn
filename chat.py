import openai as ai

def open_file(filepath):
    with open(filepath,'r',encoding='utf-8') as infile:
        return infile.read()


ai.api_key = open_file('key.txt')

def chatbot(prompt,engine ='text-davinci-003',temp = 0.7,tokens = 100,top_p = 1.0,freq_pen = 0.0,pres_pen = 0.0,stop=['JAX: ','USER: ']):
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
    convo = list()
    while True:
        user_input = input("USER: ")
        convo.append('USER: %s' % user_input)
        text_block = '\n'.join(convo)
        print(text_block)
        prompt = open_file('prompt.txt').replace('<<BLOCK>>',text_block)
        print(prompt)
        prompt = prompt + '\nJAX:'  
        response = chatbot(prompt)
        #print('JAX:', response)
        convo.append('JAX: %s' % response)




    