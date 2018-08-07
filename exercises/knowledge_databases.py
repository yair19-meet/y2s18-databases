from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(article, topic, rating):
	arc = Knowledge(
		article=article,
		topic=topic,
		rating=rating)
	session.add(arc)
	session.commit()

def query_all_articles():
	articles = session.query(Knowledge).all()
	return articles

def query_article_by_topic(topic):
	arc = session.query(Knowledge).filter_by(topic=topic).all()
	return arc

def delete_article_by_topic(topic):
	session.query(Knowledge).filter_by(topic=topic).delete()
	session.commit()

def delete_all_articles():
	session.query(Knowledge).delete()
	session.commit()

def edit_article_rating():
	pass

def query_article_by_rating(rate):
	arcs = query_all_articles()
	high_rating = []
	for i in range(len(arcs)):
		if arcs[i].rating >= rate:
			high_rating.append(arcs[i])
	return high_rating

def query_article_by_primary_key(key):
	arc = session.query(Knowledge).filter_by(id=key).first()
	return arc

# add_article(1, "rain", "clouds", 8)
# add_article(2, "career", "Michael Jordan", 9)
# add_article(3, "In culture and religion", "clouds", 10)
#add_article("awards", "Michael Jordan", 6)
# delete_article_by_topic("Michael Jordan")
delete_all_articles()
print(query_all_articles())
# print(query_article_by_primary_key(1))
