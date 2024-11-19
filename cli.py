import sys
from orchestrator import Orchestrator

def main():
    model_name = sys.argv[1] if len(sys.argv) > 1 else 'llama3.2:latest'
    orchestrator = Orchestrator(model_name=model_name)
    print(f"Personal Assistant is ready using model '{model_name}'. Type 'exit' to quit.")
    while True:
        user_query = input("You: ")
        if user_query.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        print("Processing...")
        answer = orchestrator.get_answer(user_query)
        print(f"Assistant: {answer}\n")

if __name__ == '__main__':
    main()