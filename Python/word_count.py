def analyze_text(text):
    """
    Analyzes a given string and returns the count of lines, words, and characters.
    """
    lines = text.splitlines()
    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)
    num_characters = len(text)
    return num_lines, num_words, num_characters

def main():
    # Part 1: Analyze a text file
    file_path = input("Enter the path to the text file: ")
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            lines, words, characters = analyze_text(file_content)
            print("\n--- File Analysis ---")
            print(f"Number of lines: {lines}")
            print(f"Number of words: {words}")
            print(f"Number of characters: {characters}")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

    # Part 2: Analyze user-entered text
    print("\n--- Enter new lines of text (type 'DONE' on a new line to finish) ---")
    user_input_lines = []
    while True:
        line = input()
        if line.upper() == 'DONE':
            break
        user_input_lines.append(line)

    user_text = "\n".join(user_input_lines)
    if user_text:
        lines, words, characters = analyze_text(user_text)
        print("\n--- User Input Analysis ---")
        print(f"Number of lines: {lines}")
        print(f"Number of words: {words}")
        print(f"Number of characters: {characters}")
    else:
        print("No text was entered by the user.")

if __name__ == "__main__":
    main()