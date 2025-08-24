# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

🔽 ChatGPT ReadME 🔽

# 📚 BookBot

BookBot is a simple Python command-line tool that analyzes the text of a book.  
It counts the total words and provides a character frequency report (A–Z).

---

## 🚀 Features

- Reads a text file (book) from a given file path.  
- Counts the **total number of words** in the text.  
- Counts **character frequencies** (alphabetic characters only).  
- Displays a neat, formatted report in the terminal.

---

## 📂 Project Structure

```bash
├── main.py        # Entry point for the program
├── stats.py       # Contains helper functions (e.g., word/char counting, sorting)
└── README.md      # Documentation
```
---

## ⚙️ Usage

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

### 2. Run The Program

```bash
python3 main.py <path_to_book>
```

Example
```bash
python3 main.py books/frankenstein.txt
```

## 📝 Example Output

```bash
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count -----------
Found 78345 total words
--------- Character Count ---------
a: 5421
b: 1293
c: 3212
...
============= END ===============
```

## 🛠️ Requirements
- Python 3.7+
- A valid text file (.txt) to analyze.

No external dependencies are required.

---

## 📖 How It Works
1. get_book_text(filepath)
   - Reads the entire text from the file.
2. Word Count
   - get_num_words(book_text) counts how many words are in the book.
3. Character Frequency
   - get_num_chars(book_text) counts the occurrences of each character.
   - get_sorted_list(num_chars_dict) sorts them (likely in descending order).
4. Report Generation
   - Word count summary.
   - Alphabet-only character frequency report.
   - Nicely formatted output with borders.

---

### ✨ Example Use Case

BookBot is great for:
	•	Analyzing public domain eBooks (like those from Project Gutenberg).
	•	Quick text statistics for reports, analysis, or fun insights.

---

### 📌 Notes
- Only alphabetic characters (A–Z) are included in the character report.
- Punctuation, spaces, and numbers are ignored.

