# KeywordExtractor

The KeywordExtractor toolkit comprises a Python script and two Batch scripts designed for versatile keyword-based text processing tasks. It allows for efficient extraction or removal of lines from text files based on user-specified keywords. This utility is ideal for handling large volumes of text in automated or semi-automated environments.

---

## Files in this Repository

### 1. **KeywordExtractor.py**

**Description**:  
A Python script that processes text files to either extract or remove lines containing specified keywords.

**Usage**:
1. Ensure a `words.txt` file exists in the same directory with keywords listed one per line.
2. Run the script and follow the prompts to input the file path and choose the mode ('extract' or 'remove'):
   ```bash
   python KeywordExtractor.py
   ```
3. Outputs are saved in `output.txt`.

---

### 2. **ext[Bulk].bat**

**Description**:  
A Batch script that searches for and extracts lines containing a user-specified keyword across all `.txt` files in a directory and its subdirectories, outputting the results into a text file named after the keyword.

**Usage**:
1. Place the script in the directory containing the `.txt` files.
2. Execute the script and enter keyword (less than 500 with space & not begining with /) when prompted:
   ```bash
   ext[Bulk].bat
   ```
3. Find extracted lines in a file named `list.txt`.

---

### 3. **ext[KeyWord].bat**

**Description**:  
A Batch script that filters `.txt` files in the current directory to find and compile lines containing a specified keyword into a file named `list.txt`.

**Usage**:
1. Run the script in the directory with the `.txt` files:
   ```bash
   ext[KeyWord].bat
   ```
2. Input single keyword (not begining with /) when prompted.
3. Access the compiled results in `<keyword>.txt`.

---

## Requirements

- Python 3.x for running `KeywordExtractor.py`.
- Windows environment for executing Batch files (`ext[Bulk].bat` and `ext[KeyWord].bat`).

---

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/anonyks/KeywordExtractor.git
   ```
2. Navigate into the repository directory:
   ```bash
   cd KeywordExtractor
   ```
3. Follow the usage instructions above for each script based on your needs.

---


**Contact**:  
For support or inquiries, reach out via [Telegram](https://t.me/AnonyKs_xD).
