# Book Alchemy

Book Alchemy is a Flask-based web application that lets you manage a personal library of authors and books. Users can add authors, add books (linked to an author), search books by title, sort them, and delete entries. If an author has no books left, the author is automatically removed from the database.

## 🛠 Features

- Add new authors with name and life dates
- Add books with ISBN, title, publication year, and author assignment
- Search books by title (case-insensitive)
- Sort books by title or author name
- Delete books (and auto-delete authors if no books remain)
- Error handling for 404 and 500 pages
- Basic form validation for inputs
- Placeholder image if book cover is not available from API

## 🧱 Project Structure

```
book_alchemy/
├── app.py
├── data_models.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
├── data/
│   └── library.sqlite
├── static/
│   └── placeholder.jpg
├── templates/
│   ├── 404.html
│   ├── 500.html
│   ├── add_author.html
│   ├── add_book.html
│   ├── base.html
│   └── home.html
```

## 🚀 How to Run

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/book_alchemy.git
   cd book_alchemy
   ```

2. **Create and activate virtual environment (optional but recommended)**  
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variable**  
   Create a `.env` file and add:  
   ```bash
   KEY_FLASH=your_secret_key_here
   ```

5. **Run the app**  
   ```bash
   python3 app.py
   ```

6. **Open in Browser**  
   Visit: `http://localhost:5006`

## 🧪 Testing

- Test search, sort and add/delete features manually.
- Run in Codio on port `5002` as required by assignment guidelines.

## 📝 Notes

- Make sure `library.sqlite` stays in the `data/` directory.
- API-based image fallback works using ISBN; invalid or missing ISBNs may show a placeholder.

---

📅 Last updated: 2025-10-04
