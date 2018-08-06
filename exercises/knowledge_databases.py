from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(id, article, topic, rating):
	arc = Knowledge(
		id=id,
		article=article,
		topic=topic,
		rating=rating)
	session.add(arc)
	session.commit()

def query_all_articles():
	articles = session.query(Knowledge).all()
	return articles

def query_article_by_topic():
	pass

def delete_article_by_topic():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass

add_article(1, "rain", "clouds", 8)
print(query_all_articles())