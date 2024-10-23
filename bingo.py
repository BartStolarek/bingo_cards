from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
import textwrap
import json
import random

def load_config(config_file):
    """Load configuration and sentences from JSON file."""
    with open(config_file, 'r') as f:
        config = json.load(f)
    
    # Replace placeholder with actual name in sentences
    processed_sentences = [
        s.replace("{NAME}", config["buck_name"]) 
        for s in config["sentences"]
    ]
    
    return config["buck_name"], config["pages"], processed_sentences

def create_grid(c, x, y, cell_size, grid_size):
    for i in range(grid_size + 1):
        c.line(x, y + i * cell_size, x + grid_size * cell_size, y + i * cell_size)
        c.line(x + i * cell_size, y, x + i * cell_size, y + grid_size * cell_size)

def add_title(c, x, y, title):
    c.setFont("Helvetica", 12)
    text_width = pdfmetrics.stringWidth(title, "Helvetica", 12)
    text_x = x + (5 * inch - text_width) / 2
    c.drawString(text_x, y + 5.25 * inch, title)

def add_bottom_text(c, x, y, text):
    c.setFont("Helvetica", 10)
    lines = text.split('\n')
    for i, line in enumerate(lines):
        c.drawString(x, y - (0.25 + i * 0.2) * inch, line)

def add_text_to_cell(c, text, x, y, width, height):
    font_size = 12
    c.setFont("Helvetica", font_size)
    padding = 5
    
    while True:
        char_width = font_size * 0.6
        chars_per_line = int((width - 2*padding) / char_width)
        
        wrapped_text = textwrap.wrap(text, width=chars_per_line)
        total_height = len(wrapped_text) * font_size * 1.2
        
        if total_height <= height - 2*padding and font_size >= 6:
            break
        font_size -= 0.5
        c.setFont("Helvetica", font_size)
    
    y_offset = y + height - padding - font_size
    
    for line in wrapped_text:
        text_width = pdfmetrics.stringWidth(line, "Helvetica", font_size)
        x_centered = x + (width - text_width) / 2
        c.drawString(x_centered, y_offset, line)
        y_offset -= font_size * 1.2

def create_pdf_with_grids(filename, num_pages, buck_name, sentences):
    # Separate sentences into name and non-name lists
    non_name_sentences = [s for s in sentences if buck_name not in s]
    all_sentences = sentences
    
    pagesize = A4[::-1]  # Landscape orientation
    c = canvas.Canvas(filename, pagesize=pagesize)
    width, height = pagesize
    
    cell_size = 1 * inch
    grid_size = 5
    grid_width = grid_size * cell_size
    
    left_x = (width / 4) - (grid_width / 2)
    right_x = (3 * width / 4) - (grid_width / 2)
    y = (height / 2) - (grid_width / 2)
    card_id = 0

    for page in range(num_pages):
        create_grid(c, left_x, y, cell_size, grid_size)
        create_grid(c, right_x, y, cell_size, grid_size)
        
        add_title(c, left_x, y, f"{buck_name}'s Buck Weekend Bingo - ID {card_id + 1}")
        add_title(c, right_x, y, f"{buck_name}'s Buck Weekend Bingo - ID {card_id + 2}")
        
        if card_id == 0:
            left_sentences = random.sample(non_name_sentences, min(24, len(non_name_sentences)))
        else:
            left_sentences = random.sample(all_sentences, 24)
        right_sentences = random.sample(all_sentences, 24)
        
        for i in range(grid_size):
            for j in range(grid_size):
                cell_x = left_x + j * cell_size
                cell_y = y + (grid_size - i - 1) * cell_size
                
                if i == 2 and j == 2:
                    add_text_to_cell(c, "FREE SPACE", cell_x, cell_y, cell_size, cell_size)
                else:
                    index = i * grid_size + j
                    if index > 12:
                        index -= 1
                    add_text_to_cell(c, left_sentences[index], cell_x, cell_y, cell_size, cell_size)
                
                cell_x = right_x + j * cell_size
                if i == 2 and j == 2:
                    add_text_to_cell(c, "FREE SPACE", cell_x, cell_y, cell_size, cell_size)
                else:
                    index = i * grid_size + j
                    if index > 12:
                        index -= 1
                    add_text_to_cell(c, right_sentences[index], cell_x, cell_y, cell_size, cell_size)
        
        bottom_text = (
            "1. It's Bingo!\n"
            "2. Winner gets a mystery prize!\n"
            "3. If there is no winner by 11:59pm Saturday night, the prize is burnt!\n"
            "4. Witnesses required.\n"
            "5. Loopholes and cheating are encouraged"
        )
        
        add_bottom_text(c, left_x, y, bottom_text)
        add_bottom_text(c, right_x, y, bottom_text)
        
        c.showPage()
        card_id += 2
    
    c.save()

def main():
    # Load configuration and sentences
    try:
        buck_name, pages, sentences = load_config('bingo_config.json')
    except Exception as e:
        print(f"You need a 'bingo_config.json' file in the current directory which has a dictionary with 'buck_name' and 'sentences' keys, where sentences is a list of strings. {e}")
        raise Exception(e)
    
    if len(sentences) < 24:
        raise ValueError("There must be at least 24 sentences in the configuration file.")
    
    count = 0
    
    for sentence in sentences:
        if "NAME" not in sentence:
            count += 1
            
    if count < 24:
        raise ValueError("There must be at least 24 sentences without the name placeholder.")
    
    # Create the PDF
    create_pdf_with_grids("buck_bingo.pdf", pages, buck_name, sentences)
    print("PDF created successfully!")

if __name__ == "__main__":
    main()