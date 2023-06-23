import os
import openai
import prompt
import settings


def get_answer(prompt):
    openai.api_key = settings.openai_api_key

    model = 'gpt-3.5-turbo'
    response = openai.ChatCompletion.create(
        model = model,
        messages = [{'content':prompt, 'role':'user'}]
    )
    #return response
    return response['choices'][0]['message']['content']


#print(get_answer(prompt.generate_prompt('Морти', "08.07.2021", 'Когда меня покормят')))
