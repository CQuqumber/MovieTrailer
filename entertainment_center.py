'''The file includes a list of movie objects from fresh_tomatoes.py '''
import media
import fresh_tomatoes

"""
Four arguments each:
	1st. title (title of movie)
	2nd. storyline (summary of moive)
	3rd. imsge_url (url of poster image)
	4th. trailer_url (url from youtube )
"""


toy_story = media.Movie("Toy Story",
						"A story of a boy and his toys that come to life",
					    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
					    "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
					 "A marine on an alien planet",
					 "http://upload.wikimedia.org/wikipedia/"
					 "id/b/b0/Avatar-Teaser-Poster.jpg",
					 "http://www.youtube.com/watch?v=-9ceBgWV8io")

mammamia = media.Movie("Mamma Mia",
					  "A bride-to-be trying to find her "
					  "real father told using hit songs by the popular "
					  "'70s group ABBA",
					  "https://upload.wikimedia.org/wikipedia/"
					  "en/a/a6/MammaMiaTeaserPoster.JPG",
					  "https://www.youtube.com/watch?v=DGUmXBgPvrg")

hunger_games = media.Movie("Hunger Games",
						   "A televised competition "
						   "in which two teenagers from each of the "
						   "twelve Districts of ",
						   "http://upload.wikimedia.org/wikipedia/"
						   "en/4/42/HungerGamesPoster.jpg",
						   "https://www.youtube.com/watch?v=PbA63a7H0bo")

midnight_in_paris = media.Movie("Midnight in Paris",
								"While on a trip to Paris with his fiancee's "
								"family, a nostalgic screenwriter finds himself "
								"mysteriously.",
								"https://upload.wikimedia.org/wikipedia/"
								"en/9/9f/Midnight_in_Paris_Poster.jpg",
								"https://www.youtube.com/watch?v=FAfR8omt-CY")

threeidiots = media.Movie("3 Idiots",
						  "Two friends are searching for their long lost companion, "
						  "who inspired them to think differently",
						  "https://upload.wikimedia.org/wikipedia/"
						  "en/d/df/3_idiots_poster.jpg",
						  "https://www.youtube.com/watch?v=xvszmNXdM4w")

devilwearsprada = media.Movie("The Devil Wears Prada",
						  "A smart but sensible new graduate lands a "
						  "job as an assistant to Miranda Priestly, "
						  "the demanding editor-in-chief of a high fashion magazine.",
						  "https://upload.wikimedia.org/wikipedia/en/e/e7/"
						  "The_Devil_Wears_Prada_main_onesheet.jpg",
						  "hhttps://www.youtube.com/watch?v=XTDSwAxlNhc")

fantabeasts = media.Movie("Fantastic Beasts and Where to Find Them",
						  "The adventures of writer Newt Scamander in New York's "
						  "secret community of witches and wizards seventy years "
						  "before Harry Potter reads his book in school.",
						  "https://upload.wikimedia.org/wikipedia/en/5/5e/"
						  "Fantastic_Beasts_and_Where_to_Find_Them_poster.png",
						  "https://www.youtube.com/watch?v=Vso5o11LuGU")

# assign movies into the array
movies = [toy_story, avatar, mammamia, hunger_games, midnight_in_paris,
 			threeidiots, devilwearsprada, fantabeasts]

# call open_movies_page function to show the info on the page
fresh_tomatoes.open_movies_page(movies)

















