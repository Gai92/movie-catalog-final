# movie-catalog

This is a simple movie catalog application developed in Python.

### Features:
1. Add movie to catalog
2. Get all movies in catalog
3. Get movies by genre
4. Unit testing with both passing and failing test cases (to simulate CI/CD build failure)

### Project Structure:

- `movie_catalog.py` — main application logic
- `test_movie_catalog.py` — unit tests (PyTest)
- `build.sh` — build script
- `requirements.txt` — dependency list

### Unit Testing
Project has 5 unit-tests, three of them are passed, two are failed.
As a result the build will not be successful, due to the failed tests.

Dependencies listed in `requirements.txt`. To install them, run:
```bash
pip install -r requirements.txt
```

### How to run the build

Make sure you have Python 3 and pip installed.

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2.  Make the build script executable (if needed):

```bash
chmod +x build.sh
```

3. Run the build script:

```bash
./build.sh
```

The script will install dependencies and run all unit tests using pytest.
If tests fail, the build will exit with status 1.

### GitHub Webhook:

The GitHub webhook is configured to trigger Jenkins upon push:
```arduino
https://<your-ngrok-address>.ngrok-free.app/github-webhook/
```

Please ensure your local Jenkins server is accessible via NGROK.

### Jenkins Job (Freestyle)

The project is integrated with Jenkins via a Freestyle job, which executes the build.sh script and monitors the test results.

   If all tests pass — build succeeds

   If any test fails — build fails


