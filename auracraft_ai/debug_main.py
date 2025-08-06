print("Starting script...")
import os
print("Imported os")
from dotenv import load_dotenv
print("Imported dotenv")
load_dotenv()
print("Loaded dotenv")

def main():
    print("In main function!")
    return "done"

print("Defined main function")
if __name__ == "__main__":
    print("Running main...")
    result = main()
    print(f"Main returned: {result}")
