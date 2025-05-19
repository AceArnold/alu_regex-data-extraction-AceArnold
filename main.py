import re

with open("alu_regex-data-extraction-AceArnold/sample_data.txt") as file:

#depending on what directory level you are in you may need to change the path
#i used the absolute path to the file so you can access it at root level but if you are in the "alu_regex-data-extraction-AceArnold" directory you can use the relative path
#relative path: sample_data.txt
#absolute path: alu_regex-data-extraction-AceArnold/sample_data.txt

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
    print(f"{x}:\n\n{matches}\n\n")
