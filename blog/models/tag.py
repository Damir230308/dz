from sqlalchemy import Column, Integer, String
from blog.models.database import db
from sqlalchemy.orm import relationship
from blog.models.article_tag import article_tag_association_table


class Tag(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False, default="", server_default="")
    articles = relationship(
        "Articles",
        secondary=article_tag_association_table,
        back_populates="tags",
    )

