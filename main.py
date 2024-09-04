from app.gpt_interaction import interact_with_gpt

def main():
    print("Welcome to the GPT Application!")
    
    while True:
        user_input = input("\nEnter your message (or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
        response = interact_with_gpt(user_input)
        print("\nGPT Response: ", response)

if __name__ == '__main__':
    main()
