#!/usr/bin/python3
import sys
import os

def parse_markdown_line(line):
    """
    Parse a line of Markdown and convert it to HTML if it matches heading syntax.

    Args:
        line (str): A single line of markdown text.
    
    Returns:
        str: HTML representation of the line.
    """
    # Check if line starts with heading indicators (#)
    if line.startswith("#"):
        heading_level = len(line.split()[0])  # Count the number of leading #
        if 1 <= heading_level <= 6:
            content = line[heading_level:].strip()  # Extract the content after the #
            return f"<h{heading_level}>{content}</h{heading_level}>"
    # If not a heading, just wrap in <p> tags (basic implementation)
    return f"<p>{line.strip()}</p>"

def markdown_to_html(input_file, output_file):
    """
    Convert a markdown file to HTML and write to output file.

    Args:
        input_file (str): The name of the input markdown file.
        output_file (str): The name of the output HTML file.
    """
    try:
        with open(input_file, "r") as md_file:
            content = md_file.readlines()
    except FileNotFoundError:
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # Convert each line to HTML
    html_content = ""
    for line in content:
        html_content += parse_markdown_line(line) + "\n"

    # Write HTML to output file
    with open(output_file, "w") as html_file:
        html_file.write(html_content)

if __name__ == "__main__":
    # Check if the number of arguments is correct
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    # File names from command-line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Convert markdown to HTML
    markdown_to_html(input_file, output_file)
    
    sys.exit(0)
