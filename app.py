from google import genai

client = genai.Client(api_key="AIzaSyDlirZJiQuJDSIpgxT2IWbUvaa7U3t2-sM")

system_prompt = "You are a Python coding assistant. Reply with Python code only."

def ask_agent(message):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=message, 
        config={
            "system_instruction": system_prompt
        }
    )
    return response.text

print("Agent Ready! Type your question below (type 'exit' to quit):\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Thank you! Exiting...")
        break

    answer = ask_agent(user_input)
    print("\nAI Response:\n", answer, "\n")
