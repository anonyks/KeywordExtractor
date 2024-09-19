import os

def get_keywords():
    """Load keywords from a file to a set."""
    keywords_file_path = "words.txt"
    with open(keywords_file_path, "r") as f:
        return set(line.strip() for line in f)

def process_file(input_file_path, output_file_path, keywords, mode):
    """Process the file to extract or remove lines based on keywords."""
    with open(input_file_path, "r", encoding="utf-8", errors='ignore') as in_file, \
         open(output_file_path, "a", encoding="utf-8") as out_file:

        for line in in_file:
            if (mode == 'remove' and not any(keyword in line for keyword in keywords)) or \
               (mode == 'extract' and any(keyword in line for keyword in keywords)):
                out_file.write(line)

        out_file.flush()
        os.fsync(out_file.fileno())

def main():
    print("""
    ##########################################
    #                                        #
    #       KeywordExtractor Utility        #
    #                                        #
    ##########################################

    Script developed by: @AnonyKs_xD
    Telegram: @AnonyKs_xD
    """)
    
    input_file_path = input("Enter the path to the input file: ")
    output_file_path = "output.txt"
    keywords = get_keywords()
    mode = input("Enter the mode ('extract' or 'remove'): ")

    if mode not in ['extract', 'remove']:
        print("Invalid mode! Please enter either 'extract' or 'remove'.")
        return

    process_file(input_file_path, output_file_path, keywords, mode)
    print("Done! Results saved to", output_file_path)

if __name__ == "__main__":
    main()
