import selenium.webdriver.common.by
from selenium import webdriver
import keyboard
import speech_recognition as sr
from selenium.webdriver import Keys


def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        res = r.recognize_whisper(audio, language="chinese")
        print("Whisper thinks you said: " + res)
        return res
    except sr.UnknownValueError:
        print("Whisper could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Whisper; {e}")
        return ""


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com")
    while True:
        if keyboard.is_pressed("a"):
            print("'a' was pressed")
            element = driver.find_element(selenium.webdriver.common.by.By.NAME, 'search_query')
            song = recognize_speech()
            if song:
                element.clear()
                element.send_keys(song + ' karaoke')
                element.send_keys(Keys.ENTER)



