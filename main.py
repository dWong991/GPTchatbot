#requires paid plan for api calls
#pip install openai
import openai
#add api secret key here 
openai.api_key = ""

def chat_bot(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]                                    
        )
    
    return response.choices[0].messages.content.strip()
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_bot(user_input)
        print("Chatbot: ", response)
