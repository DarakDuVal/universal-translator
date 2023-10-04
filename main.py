import json
from pathlib import Path

from ibm_watson import SpeechToTextV1, LanguageTranslatorV3, TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

_S2T_APIKEY = 'uF9F4RtONm6mTUuAfgsFXRknOW1ARkR-ow1fNoInDG15'
_S2T_SERVICE_URL = 'https://api.eu-de.speech-to-text.watson.cloud.ibm.com/instances/cad9fc09-4d2d-49c1-ae63-cdd85c2fa4f0'

_L2L_APIKEY = 'HRslcYr0HqXeC-8smRzaK6YIQo2sfUM-70FV9X64Sl_s'
_L2L_SERVICE_URL = 'https://api.eu-de.language-translator.watson.cloud.ibm.com/instances/8c68b0b5-5ce9-47cb-9e9c-6e1c2a1da190'

_T2S_APIKEY = 'rt5SEFrq11DA5nZl4KySMTOaVLYYkDJL3vJzP3Ym99Dg'
_T2S_SERVICE_URL = 'https://api.eu-de.text-to-speech.watson.cloud.ibm.com/instances/77d6e5a8-81c5-4c50-b744-549e1e5cefae'

_AUDIO_FILE = Path('./examples/audio-file2.flac')


s2t_auth = IAMAuthenticator(_S2T_APIKEY)
l2l_auth = IAMAuthenticator(_L2L_APIKEY)
t2s_auth = IAMAuthenticator(_T2S_APIKEY)


speech_to_text = SpeechToTextV1(
    authenticator=s2t_auth,
)
speech_to_text.set_service_url(_S2T_SERVICE_URL)

print(_AUDIO_FILE.resolve())
with open(_AUDIO_FILE.resolve(), 'rb') as audio_file:
    result = speech_to_text.recognize(
        audio=audio_file,
        content_type='audio/flac'
    ).get_result()
#print(json.dumps(result, indent=2))
transcript = result['results'][0]['alternatives'][0]['transcript']
print(transcript)


language_translator = LanguageTranslatorV3(
    authenticator=l2l_auth,
    version='2018-05-01'
)
language_translator.set_service_url(_L2L_SERVICE_URL)

result = language_translator.identify(transcript).get_result()
#print(json.dumps(result, indent=2))
language = result['languages'][0]['language']
print(language)


result = language_translator.translate(
    text=transcript,
    model_id='en-es'  # if source language is identified, otherwise use target only
).get_result()
#print(json.dumps(result, indent=2))
translation = result['translations'][0]['translation']


text_to_speech = TextToSpeechV1(
    authenticator=t2s_auth
)
text_to_speech.set_service_url(_T2S_SERVICE_URL)

with open('examples/audio-file-translated.flac', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            translation,
            voice='es-ES_LauraV3Voice',
            accept='audio/flac'
        ).get_result().content
    )
