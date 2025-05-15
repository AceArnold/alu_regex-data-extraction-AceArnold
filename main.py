import re

with open("sample_data.txt") as file:
    test_input = file.read()

patterns = {
    "Email Addresses": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
    "URLs": r"https?:\/\/(?:www\.)?[a-zA-Z0-9\-\.]+\.[a-z]{2,}(?:\/\S*)?",
    "Phone Numbers": r"\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}",
    "HTML Tags": r"<[^>]+>",
    # "Hashtags": r"#\w+",
    # "Currency Amounts": r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?",
    # "Credit Card Numbers": r"(\d{4}[-\s]?){3}\d{4}",
    # "Time (24-hour & 12-hour)": r"\b(?:[01]?\d|2[0-3]):[0-5]\d(?: ?[APap][Mm])?\b",
}

print("\nExtracted Data:\n")
for label, pattern in patterns.items():
    matches = re.findall(pattern, test_input)
    print(f"{label}:\n{matches}\n")
