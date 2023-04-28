import os
import openai
import speech_recognition as sr


def record_speech():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Говорите...")
        audio_text = r.listen(source)
        print("Запись завершина, спасибо")

        try:
            return r.recognize_google(audio_text, language="ru-RU")
        except Exception:
            print("Простите, я не распознал ваш голос")


def main():
    openai.api_key = os.getenv("CHAT_GTP_API")
    prompt = record_speech()

    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    print(completion.choices[0].text)


if __name__ == "__main__":
    main()
