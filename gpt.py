import os 
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import threading
import re
from audio import record_audio, speech_to_text, text_to_speech, play_audio
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

with open(os.path.join(os.path.dirname(__file__), "system_prompt.txt"), "r") as file:
    system_prompt = file.read()
    messages = [{"role": "system", "content": system_prompt}]

while True:
    # content = input("User: ") keyboard input

    chime_1 = threading.Thread(target=lambda: os.system('afplay ./audio_files/init.wav'))
    chime_1.start()

    content = speech_to_text(record_audio()) # speech input

    chime_2 = threading.Thread(target=lambda: os.system('afplay ./audio_files/conf.wav'))
    chime_2.start()

    messages.append ({"role": "user", "content": content})
    completion = openai.chat.completions.create(
        # model="gpt-3.5-turbo", 
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=200, 
        temperature=0.2
    )
    chat_response = completion.choices[0].message.content
    match = re.search(r'\{(\d+)\}', chat_response)
    if match:
        control_number = int(match.group(1))
        print(control_number) # send this number to control system
        chat_response = re.sub(r'\{\d+\}', '', chat_response)

    print(f'Dustin: {chat_response}')
    messages.append ({"role": "assistant", "content": chat_response})

    # with open(os.path.join(os.path.dirname(__file__), "temp.txt"), "r") as file: info_update = file.read()
    # messages.append ({"role": "assistant", "content": info_update})

    text_to_speech(chat_response)
    # elevenlabs_tts(chat_response
    play_audio("./audio_files/output.wav")





