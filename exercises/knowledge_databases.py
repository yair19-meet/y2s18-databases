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

def edit_article_rating(updated_rating, arc_title):
	arcs = session.query(Knowledge).filter_by(article=arc_title).all()
	for i in range(len(arcs)):
		arcs[i].rating = updated_rating

def query_article_by_high_rating(rate):
	arcs = query_all_articles()
	high_rating = []
	for i in range(len(arcs)):
		if arcs[i].rating >= rate:
			high_rating.append(arcs[i])
	return high_rating

def query_article_by_low_rating(rate):
	arcs = query_all_articles()
	low_rating = []
	for i in range(len(arcs)):
		if arcs[i].rating < rate:
			low_rating.append(arcs[i])
	return low_rating

def delete_article_by_rating(r):
	low_rating_arcs = query_article_by_low_rating(r)
	for i in range(len(low_rating_arcs)):
		session.query(Knowledge).filter_by(id=low_rating_arcs[i].id).delete()
		session.commit()

def query_article_by_primary_key(key):
	arc = session.query(Knowledge).filter_by(id=key).first()
	return arc

add_article("rain", "clouds", 8)
add_article("career", "Michael Jordan", 9)
add_article("In culture and religion", "clouds", 10)
add_article("awards", "Michael Jordan", 6)
# delete_article_by_topic("Michael Jordan")
# delete_all_articles()
# print(query_all_articles())
# print(query_article_by_primary_key(1))
# edit_article_rating(4, "rain")
# print(query_article_by_primary_key(1))
delete_article_by_rating(8)
query_all_articles()
