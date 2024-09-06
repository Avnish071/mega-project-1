import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
from openai import OpenAI



# Initialize the recognizer
recognizer = sr.Recognizer()
engine =pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
     engine.setProperty('voice',voice.id)
newsapi = '062b3fd0b21c43fe8d0db70e619b001c'

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiprocess(command):
     client = OpenAI(
     api_key="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")

    


     completion = client.chat.completions.create(
     model="gpt-4o-mini",
     messages=[
        {"role": "system", "content": "You are a helpful  VIRTUAL assistant named JARVIS like alexa and google_cloud."},
        { "role": "user","content": "command"}
      ]
      )
      
        
         
         


     return completion.choices[0].message.content

     

def processcommand(c):
   if  "open google" in c.lower():
          webbrowser.open("https://google.com")
          speak("opening google")
   elif  "open facebook" in c.lower():
          speak("bekar h bhai")
          webbrowser.open("https://facebook.com")
   elif  "open youtube" in c.lower():
         speak("opening youtube..")
         webbrowser.open("https://youtube.com")
   elif  "open flipkart" in c.lower():
         speak("shopping kiya jaye..")
         webbrowser.open("https://flipkart.com")
   elif  "open spotify" in c.lower():
         speak("gana sunne k liye tayar..")
         webbrowser.open("https://spotify.com")
   elif "news" in c.lower():
         r = requests.get("https://newsapi.org/v2/top-headlines?q=startup&apiKey=062b3fd0b21c43fe8d0db70e619b001c")
         if r.status_code == 200:
              data = r.json()
              articles = data.get('articles', [])

              for article in articles:
                    speak(article['title'])
         
   else:
        #let open ai handle the request
           
            
             
             output = aiprocess(c)
             speak(output)
            
                       
      
if __name__== "__main__":
      speak("hello , how may i help you:")

# Open the microphone and start listening
      while True:
           
              
              
            print("Recognizing...")  
            r = sr.Recognizer()

            
               
            try:
        # Recognize the speech using Google's Web Speech API
             
              with sr.Microphone() as source:
    
                print("Listening...")
                audio = r.listen(source )  # Listen for the first phrase
                text = r.recognize_google(audio)
              


              if (text.lower()=="jarvis"):
                    speak("yesssssss sirrrrrrrr")


                    with sr.Microphone() as source:
                 
                          print(" jarvis Listening...")
                          audio = r.listen(source ) 
                          command  = r.recognize_google(audio)
                          print(command)

                          processcommand(command)

          
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
              print("Could not request results from Google Speech Recognition service; {0}".format(e))
