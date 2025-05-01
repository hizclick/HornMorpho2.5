from contextlib import redirect_stdout
from l3 import load_lang, anal_word

# Input and output file paths
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"

def main():
    # Load language data
    load_lang("am")

    with open(INPUT_FILE, "r", encoding="utf-8") as infile, \
         open(OUTPUT_FILE, "w", encoding="utf-8") as outfile, \
         redirect_stdout(outfile):

       

        for line in infile:
            word = line.strip()
            if not word:
                continue
            anal_word("am", word)
            print("-" * 40)

if __name__ == "__main__":
    main()
