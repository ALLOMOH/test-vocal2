import speech_recognition as sr

recognizer = sr.Recognizer()

# On enregistre le son
with sr.Microphone() as source:
    print("Réglage du bruit ambiant... Patientez...")
    recognizer.adjust_for_ambient_noise(source)
    print("Vous pouvez parler")
    audio = recognizer.listen(source)

    # Sauvegarde de l'audio en format WAV
    with open('record.wav', 'wb') as f:
        f.write(audio.get_wav_data())

    # Reconnaissance de l'audio
    try:
        print("Reconnaissance du texte...")
        text = recognizer.recognize_google(audio, language="fr-FR")
        print(f"Vous avez dit : {text}")
    except sr.UnknownValueError:
        print("Impossible de comprendre l'audio")
    except sr.RequestError as e:
        print(f"Erreur lors de la requête au service de reconnaissance vocale ; {e}")