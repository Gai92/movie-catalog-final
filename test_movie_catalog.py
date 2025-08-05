import unittest
from movie_catalog import MovieCatalog

class TestMovieCatalog(unittest.TestCase):
    #setUp
    def setUp(self):
        self.catalog = MovieCatalog()
        self.catalog.add_movie("Matrix", "sci-fi")
        self.catalog.add_movie("Titanic", "drama")

    #add movie testing
    def test_add_valid_movie(self):
        movie = self.catalog.add_movie("She", "drama")
        self.assertEqual(movie["title"], "She")
        self.assertEqual(movie["genre"], "drama")

    #get all movies
    def test_get_all_movies(self):
        movies = self.catalog.get_all_movies()
        self.assertEqual(len(movies), 2)

    #filter by genre
    def test_get_movies_by_genre(self):
        sci_fi_movies = self.catalog.get_movies_by_genre("sci-fi")
        self.assertEqual(len(sci_fi_movies), 1)
        self.assertEqual(sci_fi_movies[0]["title"], "Matrix")

    #invalid genre
    def test_add_movie_with_invalid_genre(self):
        with self.assertRaises(ValueError) as context:
            self.catalog.add_movie("Lord of the Rings", "fantasy")  # 'fantasy' is not a valid genre
        self.assertIn("Invalid genre", str(context.exception))

    #duplicate movie
    def test_add_duplicate_movie_should_fail(self):
        with self.assertRaises(ValueError) as context:
            self.catalog.add_movie("Matrix", "sci-fi")  # Already added in setUp
        self.assertIn("already in the catalog", str(context.exception))

if __name__ == "__main__":
    unittest.main()