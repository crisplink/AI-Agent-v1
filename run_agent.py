from agent_modules import hugg_v1 , gemini_v1 , open_v1
agent_1=gemini_v1()
agent_2=hugg_v1()
agent_3=open_v1()
agents=["1.Gemini-2.5-pro","2.Hugg_zephyr-7b-alpha","3.OpenAI-3.5-turbo"]

def run_agent(agent, agent_name):
   print(f"\n{agent_name}✅")
   respo=input("What's on your mind, tell the Agent to do:\n>")
   result=agent.chat_with_agent(respo)
   print("\nAgent:\n",result)
   should_exit=input("\nDo you what to ask something more:\n").strip().lower()
   if should_exit not in ["yea","ya","ye","yes","s","yeah","sure","y"]:
     print("Goodbye👋...")
     exit()

while True:
  print("\n---Agents available---")
  for items in agents:
    print(items)  
  try:
    opp=int(input("Select a index of agent:\n").strip())
  except ValueError:
    print("Please enter a valid number.")
    continue
  if opp==1:
   print
   run_agent(agent_1,"Gemini-2.5-pro")
  elif opp==2:
    run_agent(agent_2,"Hugg_zephyr-7b-alpha")
  elif opp==3:
    run_agent(agent_3,"OpenAI-3.5-turbo")    
  else:
    print("Invalid oppition")   
