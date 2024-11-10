#!/usr/bin/python3
import sys
import os

def markdown_to_html(input_file, output_file):
    """
    Convert a basic markdown file to HTML and write to output file.

    Args:
        input_file (str): The name of the input markdown file.
        output_file (str): The name of the output HTML file.
    """
    try:
        with open(input_file, "r") as md_file:
            content = md_file.read()
    except FileNotFoundError:
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # Basic conversion: this example just wraps the content in <p> tags.
    # For a complete implementation, you'd need to parse markdown elements.
    html_content = f"<p>{content}</p>"

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
