from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__ = 'knowledge'
	id = Column(Integer, primary_key=True)
	article = Column(String)
	topic = Column(String)
	rating = Column(Integer)

	def __repr__(self):
		if self.rating < 7:
			return ("If you want to learn about {}, \n" 
	   				"you should look at the Wikipedia article called {}. \n"
               	"We gave this article a rating of {} out of 10! \n"
				"Unfortunately, this article does not have a better rating. Maybe, this is an article that should be replaced soon!").format(
                    self.topic, self.article, self.rating)
		else:
			return ("If you want to learn about {}, \n" 
	   				"you should look at the Wikipedia article called {}. \n"
               	"We gave this article a rating of {} out of 10!").format(
                    self.topic, self.article, self.rating)

# new_arc = Knowledge(id=1, article="rainbow", topic="weather", rating= 8)
# print(new_arc)


	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.

	