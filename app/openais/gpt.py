import openai
import json
import  time
from .response_parser import parse_response

api_key = "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"

client = openai.Client(api_key=api_key)
assistant_id="asst_0Js3FxXqKkhUlMpjikhe09el"

def select_option(option, thread_id):

    message_run = client.beta.threads.runs.create(
    thread_id=thread_id,
    assistant_id=assistant_id,
    additional_messages=[
        {
        "role": "user",
        "content": [
            {"type": "text", "text": option},
        ],
        }]
    )

    run = message_run
    while run.status != "completed":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run.id)
    
    messages = client.beta.threads.messages.list(
        thread_id=thread_id
    )

    response_message_id = messages.first_id

    message = client.beta.threads.messages.retrieve(
        thread_id=thread_id,
        message_id=response_message_id
    )

    data={}
    parsed_reaponse = parse_response(message.content.pop().text.value)
    data['response']=parsed_reaponse
    if 'lose_game' not in parsed_reaponse.keys() and 'win_game' not in parsed_reaponse.keys():
        data['successful_option']=True
    return data


def start_game():
    run = client.beta.threads.create_and_run(
    assistant_id=assistant_id,
    thread={
        "messages": [
        {"role": "user", "content": "Lets start a game"}
        ]
    }
    )

    run_check = run
    while run_check.status != "completed":
        time.sleep(1)
        run_check = client.beta.threads.runs.retrieve(
            thread_id=run.thread_id,
            run_id=run.id)
    
    messages = client.beta.threads.messages.list(thread_id=run.thread_id)
    assitant_response_id=messages.first_id
    message = client.beta.threads.messages.retrieve(
        thread_id=run.thread_id,
        message_id=assitant_response_id
    )

    data={}
    parsed_reaponse = parse_response(message.content.pop().text.value)
    data['thread_id']=run.thread_id
    data['response']=parsed_reaponse
    return data

