'''The file stores the classes to build the website, 
   The class TvShow is for future project'''

import webbrowser


class Video():
	"""The Clss provides one movie's information"""
	def __init__(self, movie_title, movie_storyline):
		self.title = movie_title
		self.storyline = movie_storyline



class Movie(Video):
	"""The Clss 'Movie' provides one movie's information and 
		inherite from calss Video"""
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		Video.__init__(self, movie_title,movie_storyline)
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		webbrowser.open("self.trailer_youtube_url")



class TvShow(Video):
	"""It's for further TvShow function"""
	def __init__(self, movie_season, movie_episodes, tv_station):
		Video.__init__(self, movie_title, movie_storyline)
		self.episodes = movie_episodes
		self.season = movie_season
		self.tv_station_url = tv_station


