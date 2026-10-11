## LikeIt – Movie and Book Finder (Python)

This small Python project is inspired by my existing **LikeIt** media recommendation application. It searches 2 external API sources using the same keyword

## APIs

1. **TMDB (The Movie Database)** – `https://api.themoviedb.org/3/search/movie` – returns movies, release years and user ratings. Requires your own **TMDB API key**.
2. **Open Library** – `https://openlibrary.org/search.json` – returns books, authors and publication years. No API key needed.

This is still data retrieval prototype, not yet a personalized recommendation, perhaps in the future I can make it bigger

## Requirements

- Python 3.10 or newer
- Internet access
- Your own TMDB API key (v3 API key)

## Run it

1. Download or clone this repository and open a terminal in the project folder.
2. Create a virtual environment (recommended):

   ```bash
   python -m venv .venv
   ```

3. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```
4. Register or sign in at <https://www.themoviedb.org/> and request an API key in your account's API settings. Use the **API Key (v3 auth)** value.
5. Copy `.env.example` to `.env`. Replace the placeholder with your real key,
6. Run the project:

   ```bash
   python main.py "harry potter"
   ```

The program prints matches from each API separately. If the key is missing or invalid, or the service is unavailable, it displays an error message.


## Future semester-project ideas

- Save retrieved records in SQLite
- Combine API results in an interface
- Add genre filters and personalized media recommendations

## Notes

TMDB and Open Library are independent services. Availability depend on those providers. This is just an educational prototype.
