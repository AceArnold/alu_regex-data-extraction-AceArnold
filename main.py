import re

with open("sample_data.txt") as file:
    test_input = file.read()

patterns = {
    "Email Addresses": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
    "URLs": r"https?:\/\/(?:www\.)?[a-zA-Z0-9\-\.]+\.[a-z]{2,}(?:\/\S*)?",
    "Phone Numbers": r"\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}",
    "HTML Tags": r"<[^>]+>", 
    "currency": r"\$\d+(?:\.\d{2})?",

}

print("\nExtracted Data:\n")
for x, y in patterns.items():
    #x is the name of the pattern
    #y is the regex pattern
    matches = re.findall(y, test_input)
    print(f"{x}:\n{matches}\n")
