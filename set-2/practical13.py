def count_words_in_file(filepath):
    """Reads a file and returns the total word count."""
    try:
        # 'with' ensures the file is automatically closed
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            return len(words)
            
    except FileNotFoundError:
        return "Error: The file was not found."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Usage
filename = "hi.txt"
total_words = count_words_in_file(filename)

print(f"Total word count: {total_words}")