import os
import pyttsx3

def speak_text(text: str) -> None:
    """Speak and print a line of text."""
    engine = pyttsx3.init()
    engine.say(text)
    print(text)
    engine.runAndWait()
    engine.stop()

def list_available_forms(forms_dir: str) -> list[str]:
    """Return a sorted list of .txt form filenames in the forms directory."""
    return sorted(f for f in os.listdir(forms_dir) if f.endswith(".txt"))

def choose_form(forms: list[str]) -> str:
    """Prompt the user to choose a form from the available list."""
    print("\nAvailable Forms:")
    for idx, filename in enumerate(forms, start=1):
        form_name = os.path.splitext(filename)[0]  # removes '.txt'
        print(f"{idx}. {form_name}")

    while True:
        choice = input("\nEnter the number of the form you want to practice: ")
        if choice.isdigit() and 1 <= int(choice) <= len(forms):
            return forms[int(choice) - 1]
        print("Invalid choice. Please enter a valid number.")

def read_form(filepath: str) -> None:
    """Read the selected form and speak each line."""
    with open(filepath, "r") as file:
        for count, line in enumerate(file, start=1):
            cleaned = line.strip()
            speak_text(cleaned)
            print(f"Line {count}: {cleaned}")

def main():
    forms_dir = "forms"

    if not os.path.exists(forms_dir):
        print("Error: 'forms' directory not found.")
        return

    forms = list_available_forms(forms_dir)

    if not forms:
        print("No form files found in the 'forms' directory.")
        return

    selected_form = choose_form(forms)
    form_path = os.path.join(forms_dir, selected_form)

    print(f"\nStarting form: {os.path.splitext(selected_form)[0]}\n")
    read_form(form_path)

if __name__ == "__main__":
    main()
