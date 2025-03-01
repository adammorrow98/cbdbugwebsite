import re

# Raw text - you can paste your whole 2019 block into this multiline string
raw_text = """
To BCC: <a href="20191205-CBD BUG sub - five new green bridges final.pdf">Submission to Green Bridges for Brisbane (BCC)</a> (5 December 2019) <br>
To BCC: <a href="20191205 - CBD BUG - Submission Cityreach Boardwalk.pdf">Submission to City Reach Waterfront Master Plan</a> (5 December 2019) <br>
To BCC LM: <a href="20191130-CBD BUG LM ltr re NBB.pdf">North Brisbane Bikeway</a> (30 November 2019) <br>
# (Paste the rest of your 2019 entries here)
"""

# Regex to extract details (to/from, date, file, subject)
pattern = re.compile(
    r'(?P<tofrom>(To|From)\s[^:]+):\s*<a href="(?P<file>[^"]+)">(?P<subject>[^<]+)</a>\s*\((?P<date>[\dA-Za-z\s]+)\)'
)

# Start of the markdown table
markdown_table = """| Date | To/From | Subject | Letter |
| --- | --- | --- | --- |
"""

# Process each line and extract data
for match in pattern.finditer(raw_text):
    tofrom = match.group('tofrom')
    file = match.group('file')
    subject = match.group('subject')
    date = match.group('date')

    # Format the button link with correct folder prefix
    button_link = f"old-letters/2019/{file}"
    button = f'{{{{< button label="View Letter" link="{button_link}" style="solid" >}}}}'

    # Add row to the markdown table
    markdown_table += f"| {date} | {tofrom} | {subject} | {button} |\n"

# Save to file
with open("old_letters_2019.md", "w", encoding="utf-8") as f:
    f.write(markdown_table)

print("Markdown file 'old_letters_2019.md' generated successfully!")
