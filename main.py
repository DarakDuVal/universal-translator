from os.path import join, dirname
import json
from pathlib import Path

from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

_APIKEY = 'uF9F4RtONm6mTUuAfgsFXRknOW1ARkR-ow1fNoInDG15'
_S2T_SERVICE_URL = 'https://api.eu-de.speech-to-text.watson.cloud.ibm.com/instances/cad9fc09-4d2d-49c1-ae63-cdd85c2fa4f0'

_AUDIO_FILE = Path('./examples/audio-file2.flac')

authenticator = IAMAuthenticator(_APIKEY)

speech_to_text = SpeechToTextV1(
    authenticator=authenticator
)
speech_to_text.set_service_url(_S2T_SERVICE_URL)

print(_AUDIO_FILE.resolve())
with open(_AUDIO_FILE.resolve(), 'rb') as audio_file:
    results = speech_to_text.recognize(
        audio=audio_file,
        content_type='audio/flac'
    ).get_result()
print(json.dumps(results, indent=2))
