"""LikeIt: retrieve movies and books from two independent public APIs."""
import os
import sys
import requests
from dotenv import load_dotenv

load_dotenv()
TMDB_URL = "https://api.themoviedb.org/3/search/movie"
BOOKS_URL = "https://openlibrary.org/search.json"


def fetch_movies(query: str, api_key: str) -> list[dict]:
    response = requests.get(
        TMDB_URL,
        params={"api_key": api_key, "query": query, "language": "en-US", "page": 1},
        timeout=15,
    )
    response.raise_for_status()
    return [
        {"title": item.get("title", "Unknown"),
         "year": (item.get("release_date") or "????")[:4],
         "rating": item.get("vote_average", "N/A")}
        for item in response.json().get("results", [])[:5]
    ]


def fetch_books(query: str) -> list[dict]:
    response = requests.get(
        BOOKS_URL,
        params={"q": query, "limit": 5, "fields": "title,author_name,first_publish_year"},
        timeout=15,
    )
    response.raise_for_status()
    return [
        {"title": item.get("title", "Unknown"),
         "author": ", ".join(item.get("author_name", [])[:2]) or "Unknown",
         "year": item.get("first_publish_year", "N/A")}
        for item in response.json().get("docs", [])[:5]
    ]


def main():
    key = os.getenv("TMDB_API_KEY", "").strip()
    if not key:
        print("Missing TMDB_API_KEY. Copy .env.example to .env and add your key.", file=sys.stderr)
        return 1
    query = " ".join(sys.argv[1:]).strip() or input("Enter a title or keyword: ").strip()
    if not query:
        print("Please enter a search term.", file=sys.stderr)
        return 1
    try:
        movies = fetch_movies(query, key)
        books = fetch_books(query)
    except requests.HTTPError as exc:
        code = exc.response.status_code if exc.response is not None else "unknown"
        print(f"API request failed (HTTP {code}). Check your TMDB key and try again.", file=sys.stderr)
        return 1
    except requests.RequestException as exc:
        print(f"Network error: {exc}", file=sys.stderr)
        return 1
    print(f"\nLikeIt results for: {query}")
    print("\nMOVIES (TMDB)")
    for movie in movies:
        print(f"- {movie['title']} ({movie['year']}) | rating: {movie['rating']}")
    if not movies:
        print("No movies found.")
    print("\nBOOKS (Open Library)")
    for book in books:
        print(f"- {book['title']} ({book['year']}) | {book['author']}")
    if not books:
        print("No books found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
