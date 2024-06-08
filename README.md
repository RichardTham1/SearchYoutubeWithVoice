# SearchYoutubeWithVoice

My mom wanted a way to search for Youtube songs for karaoke using her voice. Therefore I tried and did it.

## Tech

I used Selenium to communicate with Chrome, Python library SpeechRecognition, PyAudio to detect microphone input and Whisper to detect and recognize chinese language (mandarin).

## How it works

The script will launch a Chrome web and go to Youtube. Tt will then enter a while loop to wait for keyboard input. When the key 'a' is pressed, the script will look for the search bar in Youtube and listen to the microphone input. After a few seconds, it will search the song on Youtube.

## Conclusion

You can use the code written however you'd like, I was simply experimenting some stuff.

In the end, my mom didn't need it :(
