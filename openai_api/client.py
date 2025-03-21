import openai

from decouple import config


def get_car_ai_bio(model, brand, year):
    openai.api_key = config('OPENAI_API_KEY')
    messages = [
        {
            'role': 'system',
            'content': f'Me mostre uma descrição de venda para o carro {brand} {model} {year} em apenas 250 caracteres.'
        },
        {
            'role': 'user',
            'content': 'Seja específico e técnico sobre o modelo.'
        }
    ]

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages
    )

    return response['choices'][0]['message']['content']