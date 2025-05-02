import io
import json
from contextlib import redirect_stdout
from l3 import load_lang, anal_word

INPUT_FILE = "input.txt"
OUTPUT_TEXT_FILE = "output.txt"
OUTPUT_JSON_FILE = "stems.json"

def extract_citations(output_text):
    citations = []
    for line in output_text.splitlines():
        line = line.strip()
        if "citation:" in line:
            parts = line.split("citation:")
            if len(parts) > 1:
                citation = parts[1].strip().split()[0]
                citations.append(citation)
    return citations

def main():
    load_lang("am")
    results = {}

    with open(INPUT_FILE, "r", encoding="utf-8") as infile, \
         open(OUTPUT_TEXT_FILE, "w", encoding="utf-8") as txt_outfile:

        for line in infile:
            word = line.strip()
            if not word:
                continue

            buffer = io.StringIO()
            with redirect_stdout(buffer):
                anal_word("am", word)
                print("-" * 40)

            output = buffer.getvalue()
            txt_outfile.write(output)

            citations = extract_citations(output)
            results[word] = citations

    with open(OUTPUT_JSON_FILE, "w", encoding="utf-8") as json_outfile:
        json.dump(results, json_outfile, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
