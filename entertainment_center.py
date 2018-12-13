import fresh_tomatoes
import media

# this is a list of the movies that will be shown at the webpage; the instances were created at the media.py file.
anomalisa = media.Movie("Anomalisa",
                        """
                        A guy perceives everyone as identical 
                        until he meets a unique woman in a Cincinnati hotel.
                        """,
                        "https://upload.wikimedia.org/wikipedia/en/0/0f/Anomalisa_poster.jpg",  #noqa
                        "https://www.youtube.com/watch?v=WQkHA3fHk_0")

black_hawk_down = media.Movie("Black Hawk Down",
                              """Follow United Nations' military operation in
                              Somalia during the early 90's civil war.""",
                              "https://upload.wikimedia.org/wikipedia/en/0/0c/Black_hawk_down_ver1.jpg",  #noqa
                              "https://www.youtube.com/watch?v=2GfBkC3qs78")

before_sunrise = media.Movie("Before Sunrise",
                             """Two strangers meet in a Euro Train
                              and a love story begins.""",
                             "https://upload.wikimedia.org/wikipedia/pt/d/da/Before_Sunrise_poster.jpg",  # noqa
                             "https://www.youtube.com/watch?v=25v7N34d5HE")

before_sunset = media.Movie("Before Sunset",
                            """The love story Continues, 09 years later,
                             but now in Paris.""",
                            "https://upload.wikimedia.org/wikipedia/pt/a/ae/Before_Sunset.jpg",  # noqa
                            "https://www.youtube.com/watch?v=HurI2rFB_mk")

before_midnight = media.Movie("Before Midnight",
                              """The drama of a married life 18 years
                               after meeting each other.""",
                              "https://upload.wikimedia.org/wikipedia/en/a/ad/Before_Midnight_poster.jpg",  # noqa
                              "https://www.youtube.com/watch?v=Kv6JWoVKlGY")

ff_advent = media.Movie("Final Fantasy - Advent Children",
                        """Follow the story of Cloud after the
                         events of Final Fantasy VII.""",
                        "https://upload.wikimedia.org/wikipedia/pt/1/18/Final_Fantasy_VII_Advent_Children_poster.jpg",  # noqa
                        "https://www.youtube.com/watch?v=q7Kup3jp-Ss")

movies = [
          anomalisa,
          black_hawk_down,
          before_sunrise,
          before_sunset,
          before_midnight,
          ff_advent
          ]

fresh_tomatoes.open_movies_page(movies)  # calls the file fresh_tomatoes.py
