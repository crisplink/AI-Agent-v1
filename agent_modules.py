from huggingface_hub import InferenceClient
from openai import OpenAI 
import google.generativeai as genai
from dotenv import load_dotenv
from datetime import datetime
import os
import re

# Load .env
load_dotenv()
# Get the API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
HUGGING_API_KEY = os.getenv("HUGGING_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class hugg_v1:
 
 def __init__(self):
    #connect with hugging face
    self.client = InferenceClient(token=HUGGING_API_KEY)
 
 #Reusable agent function
 def chat_with_agent(self,user_prompt):
    try:
      response = self.client.chat_completion(
      model="HuggingFaceH4/zephyr-7b-alpha",
      messages=[

           {"role": "system", "content": ("You are a helpful assistant. "
           "Keep your answers clear and direct. "
           "Do not include any role tags."
           "When listing, stop EXACTLY at the number requested by the user."
           "Never go beyond that number, even if you have more ideas.")
           },
           {"role": "user", "content":user_prompt}
      ],
      temperature=0.7
       )
      ans=response.choices[0].message.content
      ans = ans.replace("*", " ").strip()
      ans = re.sub(r'\n{2,}','\n',ans)
      #save the file(log)
      timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      with open(r"C:\Users\Hp\Desktop\agent_v1\log\agent_log_hugg_v1.txt","a",encoding="utf-8")as file:
          file.write(f"[{timestamp}]\n User: {user_prompt}\nAgent:\n{ans}\n")    
          return ans
    except Exception as err:
       return f"An error occurred: {err}"

class open_v1:
  # Initialize your OpenAI client
  def __init__(self):
   self.client = OpenAI(api_key=OPENAI_API_KEY)

  def chat_with_agent(self,user_prompt):
    try:
       # Create a completion
       response = self.client.chat.completions.create(      
          model="gpt-3.5-turbo",
          messages=[
          {"role": "system", "content": ("You are a helpful AI assistant."
          "Keep your answers clear and direct. ")},
          {"role": "user", "content": user_prompt}
          ]
        )

       # Print the result
       ans=response.choices[0].message.content
       ans = ans.replace("*", " ").strip()
       ans = re.sub(r'\n{2,}','\n',ans)
       #log
       timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       with open(r"C:\Users\Hp\Desktop\agent_v1\log\agent_log_openai_v1.txt","a",encoding="utf-8")as file:
           file.write(f"[{timestamp}]\n User: {user_prompt}\nAgent:\n{ans}\n")
           return ans    
    except Exception as err:
       return f"An error ocurred: {err}"
    
class gemini_v1:
   #connect with gemini
   def __init__(self):
      genai.configure(api_key=GEMINI_API_KEY)  
      self.model=genai.GenerativeModel('models/gemini-2.5-pro')

   def chat_with_agent(self,user_prompt):
     try:   
       response=self.model.generate_content(user_prompt)
       ans=response.text
       #clean response
       ans = ans.replace("*", " ").strip()
       ans = re.sub(r'\n{2,}','\n',ans)

      # timestamp with log
       timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       with open(r"C:\Users\Hp\Desktop\agent_v1\log\agent_log_gemini_v1.txt","a",encoding="utf-8")as file:
          file.write(f"[{timestamp}]\n User: {user_prompt}\nAgent:\n{ans}\n")
       return ans
     except Exception as err:
       return f"An error occured: {err}"   
