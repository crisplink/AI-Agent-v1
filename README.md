# AI-Agent-v1
💫Talk to 3 AI brains at once , a simple multi-agent chatbot to test, learn, and build on.

🧩 Multi-Agent AI Assistant — Python Project
This project is a simple Python-based multi-agent AI assistant.  
It lets you choose between Gemini, Hugging Face, or OpenAI to generate responses for your input.

## 📥 Clone the project
  git clone https://github.com/yourusername/AI-Agent-v1.git
  cd AI-Agent-v1

     
## 🚀 How it works
    The project has three agents:
   Gemini (gemini-2.5-pro),
   Hugging Face (zephyr-7b-alpha),
   OpenAI GPT (gpt-3.5-turbo).  
  You run the script → pick an agent → type your prompt → get a reply → the conversation is logged.

## 📂 Project structure
>>agent_v1/  
   ├─ __pycache__/  
   ├─ log/               # Logs of your conversations (ignored by Git)  
   ├─ agent_modules.py   # Main agent classes  
   ├─ .env               # Your secret API keys (DO NOT SHARE!)  
   ├─ run_agent.py       # Entry point to run your agents  
   ├─ .gitignore  

## 🔑 How to add your API keys
  This project uses a .env file to keep your API keys safe.  
  Create a file named .env in your project root (same level as agent_modules.py).  
  >>Example .env:  
     GEMINI_API_KEY=your_gemini_api_key_here  
     HUGGING_API_KEY=your_huggingface_api_key_here  
     OPENAI_API_KEY=your_openai_api_key_here  

✅ Full Setup — Requirements-
  Before you run the project, make sure you have Python installed (Python 3.10+ is best).
  >>Then install these libraries in your project’s virtual environment:  
     # Activate virtual environment  
     # On Windows:  
     venv\Scripts\activate  
     # On macOS/Linux:  
     source venv/bin/activate  
     # Install required packages for all 3 agents  
     pip install google-generativeai  
     pip install huggingface_hub   
     pip install openai  
     pip install python-dotenv  

✅ How to run-
  Install requirements (pip install....)-add your dependencies if needed.
  Make sure your .env file is set up.  
 Run:  
   python run_agent.py  
  Pick an agent by number → enter your prompt → see your AI reply!  

## 📌 Notes
  Logs: All conversations are saved inside the log/ folder. This folder is ignored by .gitignore so your logs stay local.  
  API keys: Each user must use their own keys for Gemini, Hugging Face, and OpenAI.  
  OpenAI billing: If your key is expired or quota is exhausted, the agent will show an error — handled with try/except.  
  Gemini pro recomended (use student offer available now as of (20th june 2025). 

## 🫧 Why I built this?
  This is my first step towards building a *AI agent agency*.  
  I made this to learn how to:
    Handle multiple LLM providers in one project,
    Securely manage API keys,
    Log user-agent interactions,
    Build a reusable structure for future agents.  

## ⚡️ Contributing
  Feel free to fork, improve, and share feedback!
  Create an issue or pull request if you find bugs or have ideas.

📃 Licensed as MIT.   
📌 Tip: Never commit your .env file or API keys to GitHub — keep them in .gitignore.

