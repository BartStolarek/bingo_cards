# Buck Weekend Bingo Generator
A Python script that generates printable bingo cards for a buck's weekend/bachelor party. The script creates a PDF with multiple pages, where each page contains two bingo cards - one with general activities and one that includes activities specific to the buck.

## Setup

1. Make sure you have Python 3.x installed on your system.
2. Create a virtual environment and activate it:
```
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. Install the required packages:
bashCopypip install reportlab


## Configuration

Create a file named bingo_config.json with your bingo card content:
```
{
    "buck_name": "Tom",
    "pages": 30,
    "sentences": [
        "{NAME} falls asleep in a weird place",
        "{NAME} loses their phone",
        "{NAME} does karaoke",
        "Take a silly photo with {NAME}",
        "{NAME} has to wear a funny hat for an hour",
        "Swap shirts with {NAME}",
        "Get {NAME} to give a dramatic apology",
        "{NAME} has to do 20 push-ups",
        "Call {NAME} by the wrong name all night",
        "{NAME} has to speak in an accent for 10 minutes",
        "Make a heartfelt toast to {NAME}",
        "{NAME} tells a dad joke",
        "{NAME} does their best dance move",
        "Wake {NAME} with a loud song",
        "Get {NAME} to do the chicken dance",
        "Beat {NAME} in rock paper scissors",
        "Beat {NAME} in an arm wrestle",
        "Get a stranger to wish {NAME} good luck",
        "Secretly put a party hat on {NAME}",
        "Give {NAME} a face paint makeover",
        "{NAME} has to drink water from a baby bottle",
        "Get a stranger to join in a group photo",
        "Do the macarena in public",
        "Tell 3 embarrassing stories about {NAME}",
        "Win 2 games of pool in a row",
        "Win a dance-off",
        "Get everyone to do the conga line",
        "Try 5 different mocktails",
        "Get a birdie or better in mini golf",
        "Be the first to spot someone sleeping",
        "Eat a weird food combination",
        "Buy a round of soft drinks",
        "Get a free appetizer",
        "Get a business card from someone",
        "Get the DJ to play your favorite song",
        "Make an impossible paper airplane shot",
        "Hit a bulls eye in darts",
        "Drink water from a new shoe",
        "Order food in a silly accent",
        "Get a stranger to draw your portrait",
        "Pour water over {NAME}'s head",
        "Get 5 high-fives from strangers",
        "Do the saltine cracker challenge",
        "Create a mystery drink for {NAME} (non-alcoholic)",
        "Successfully start a flash mob",
        "Balance a spoon on your nose for 1 minute"
    ]
}
```

Important notes about the configuration:

- Replace "Tom" with the buck's name
- Use {NAME} as a placeholder in sentences where you want the buck's name to appear
- pages: Number of bingo cards to generate (each page has two grids/cards)
- You must have at least 24 sentences in total
- You must have at least 24 sentences that don't include the {NAME} placeholder (this is for bingo card ID 1 and is the buck's card)
- Each sentence will be automatically wrapped to fit in the bingo card cells, but still don't make them too long. 



## Running the Script

1. Make sure your virtual environment is activated
2. Run the script:
```
python bingo.py
```
3. The script will generate a file named buck_bingo.pdf in the same directory

## Output

- The script generates the specified number of pages of bingo cards
- Each page contains two 5x5 bingo grids
- The first grid (ID 1) only contains activities without the buck's name, give this to the buck
- All other grids (ID 2 and onwards) contain random activities that may include the buck's name
- Each grid has a unique ID number
- Each grid has a FREE SPACE in the center
- Bottom text includes rules and instructions

## File Structure
your-project-directory/<br>
├── bingo_generator.py<br>
├── bingo_config.json<br>
├── .gitignore<br>
├── venv/<br>
└── buck_bingo.pdf (generated)<br>

## Error Handling
The script will show helpful error messages if:

The configuration file is missing or incorrectly formatted
There aren't enough total sentences (minimum 24 required)
There aren't enough sentences without the buck's name (minimum 24 required)
The pages parameter is missing or invalid

## Notes

- The generated PDF is in landscape orientation
- The script uses reportlab to generate the PDF
- Font size will automatically adjust to fit text in cells
- The configuration file is excluded from git tracking for privacy