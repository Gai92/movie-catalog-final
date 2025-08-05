class MovieCatalog:

    # Define valid genres
    VALID_GENRES = ["drama", "comedy", "sci-fi", "action", "horror"]

    def __init__(self):
        self.movies = []

    # Return all movies
    def get_all_movies(self):
        if not self.movies:
            print("The catalog is currently empty.")
        return self.movies

    # Add a movie to the catalog
    def add_movie(self, title, genre):
        if not title or not genre:
            raise ValueError("Title and genre cannot be empty.")

        title = title.strip().title()
        genre = genre.strip().lower()

        if genre not in self.VALID_GENRES:
            raise ValueError(
                f"Invalid genre. Allowed genres: {', '.join(self.VALID_GENRES)}"
            )

        for movie in self.movies:
            if movie["title"].lower() == title.lower():
                raise ValueError("This movie is already in the catalog.")

        movie = {"title": title, "genre": genre}
        self.movies.append(movie)
        return movie


    # Return all movies
    def get_all_movies(self):
        if not self.movies:
            print("The catalog is currently empty.")
        return self.movies
    
    # Filter by genre
    def get_movies_by_genre(self, genre):
        genre = genre.strip().lower()
        return [movie for movie in self.movies if movie["genre"] == genre]
    

def main():
    catalog = MovieCatalog()

    print("Welcome to the Movie Catalog!")
    print("Available genres:", ", ".join(MovieCatalog.VALID_GENRES))

    while True:
        print("\nEnter a new movie (or type 'q' to quit).")

        title = input("Title: ").strip()
        if title.lower() == "q":
            break

        genre = input("Genre: ").strip()
        if genre.lower() == "q":
            break

        try:
            movie = catalog.add_movie(title, genre)
            print(f" '{movie['title']}' added successfully.")
        except ValueError as e:
            print(f" Error: {e}")

    #Print all movies
    print("\nAll Movies in Catalog:")
    movies = catalog.get_all_movies()
    for movie in movies:
        print(f" {movie['title']} ({movie['genre']})")

     # Show available genres before asking
    print("Available genres:", ", ".join(MovieCatalog.VALID_GENRES))

    genre = input("Enter a genre to filter by: ").strip()
    filtered = catalog.get_movies_by_genre(genre)

    if not filtered:
        print(f"No movies found for genre '{genre}'.")
    else:
        print(f"\n Movies in genre '{genre}':")
        for movie in filtered:
            print(f"{movie['title']} ({movie['genre']})")

if __name__ == "__main__":
    main()