# universal-translator
Provide the ultimate Star Trek feel with an AI-powered simultaneous translator, which takes your voice and provides the translated audio stream in target language.
Built on IBM Watson.


# Environment
## Beeware
sudo apt update
sudo apt install build-essential git pkg-config python3-dev python3-venv libgirepository1.0-dev libcairo2-dev gir1.2-webkit2-4.0 libcanberra-gtk3-module


# References
- IBM Watson cloud services
  - Speech to Text
    - API: https://cloud.ibm.com/apidocs/speech-to-text?code=python
    - Doc: https://cloud.ibm.com/docs/speech-to-text
  - Language translator
    - API: https://cloud.ibm.com/apidocs/language-translator?code=python
    - Doc: https://cloud.ibm.com/docs/language-translator
  - Text to Speech
    - API: https://cloud.ibm.com/apidocs/text-to-speech?code=python 
    - Doc: https://cloud.ibm.com/docs/text-to-speech
- https://github.com/ibm-developer-skills-network/translator-with-voice-and-watsonx

# Known issues

- pyaudio does not install on Ubuntu
run `sudo apt install portaudio19-dev` to resolve missing `portaudio.h` file
