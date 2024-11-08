#Script to read docx file into a data frame
#read a heirarchal file with it preserved
#read tables into data frame
import pandas as pd
from docx import Document

# Function to read and parse a hierarchical docx file
def parse_docx(file_path):
    # Load the document
    doc = Document(file_path)
    
    sections = []
    current_section = None
    for para in doc.paragraphs:
        if para.style.name == "Heading 1":  # Level 1 headings (main sections)
            if current_section:  # If we have a previous section, add it
                sections.append(current_section)
            current_section = {'level': 1, 'title': para.text, 'content': []}
        elif para.style.name == "Heading 2":  # Level 2 headings (subsections)
            if current_section:  # If we are inside a section, add the subsection
                current_section['content'].append({'level': 2, 'title': para.text, 'content': []})
        elif para.style.name == "Heading 3":  # Level 3 headings (subsubsections)
            if current_section and current_section['content']:
                current_section['content'][-1]['content'].append({'level': 3, 'title': para.text, 'content': []})
        elif para.style.name == "Normal":  # Normal text
            if current_section:  # Add text to the most recent section or subsection
                if 'content' in current_section:
                    if current_section['content']:
                        current_section['content'][-1].setdefault('content', []).append(para.text)
                    else:
                        current_section['content'].append({'level': 1, 'title': para.text, 'content': []})

    # Append the last section if it exists
    if current_section:
        sections.append(current_section)
    
    return sections

# Function to flatten the hierarchical structure into a list of dicts
def flatten_sections(sections):
    flat_data = []
    
    def flatten(section, parent_title=''):
        section_title = parent_title + ' ' + section['title'] if parent_title else section['title']
        flat_data.append({'Level': section['level'], 'Title': section_title, 'Content': '\n'.join(section['content'])})
        for subsection in section['content']:
            flatten(subsection, section_title)

    for section in sections:
        flatten(section)
    
    return flat_data

# Main code
file_path = "/Users/gadappa/Downloads/Test-hierarchy-doc_v1.docx"  
# Path to your DOCX file

# Parse the document
sections = parse_docx(file_path)
print(sections)

# Flatten the hierarchical structure into a list of dictionaries
flat_data = flatten_sections(sections)

# Convert the flattened data into a pandas DataFrame
df = pd.DataFrame(flat_data)

# Display the DataFrame
print(df)

