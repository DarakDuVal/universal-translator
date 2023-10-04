import os
import json
from pathlib import Path

from ibm_watson import SpeechToTextV1, LanguageTranslatorV3, TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


def get_env(filename) -> dict:
    with open(filename, mode='r') as f:
        return json.loads(f.read())


secrets = get_env(Path('./secrets.json'))
settings = get_env(Path('./settings.json'))

_AUDIO_FILE = Path('./examples/audio-file2.flac')


speech_to_text = SpeechToTextV1(
    authenticator=IAMAuthenticator(secrets['API_KEYS']['SPEECH_TO_TEXT']),
)
speech_to_text.set_service_url(settings['SERVICE_URLS']['SPEECH_TO_TEXT'])

#print(_AUDIO_FILE.resolve())
with open(_AUDIO_FILE.resolve(), 'rb') as audio_file:
    result = speech_to_text.recognize(
        audio=audio_file,
        content_type='audio/flac'
    ).get_result()
# print(json.dumps(result, indent=2))
transcript = result['results'][0]['alternatives'][0]['transcript']
print(transcript)

language_translator = LanguageTranslatorV3(
    authenticator=IAMAuthenticator(secrets['API_KEYS']['LANGUAGE_TRANSLATOR']),
    version='2018-05-01'
)
language_translator.set_service_url(settings['SERVICE_URLS']['LANGUAGE_TRANSLATOR'])

result = language_translator.identify(transcript).get_result()
# print(json.dumps(result, indent=2))
language = result['languages'][0]['language']
print(language)

result = language_translator.translate(
    text=transcript,
    model_id='en-es'  # if source language is identified, otherwise use target only
).get_result()
# print(json.dumps(result, indent=2))
translation = result['translations'][0]['translation']
print(translation)

text_to_speech = TextToSpeechV1(
    authenticator=IAMAuthenticator(secrets['API_KEYS']['TEXT_TO_SPEECH'])
)
text_to_speech.set_service_url(settings['SERVICE_URLS']['TEXT_TO_SPEECH'])

with open('examples/audio-file-translated.flac', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            translation,
            voice='es-ES_LauraV3Voice',
            accept='audio/flac'
        ).get_result().content
    )
