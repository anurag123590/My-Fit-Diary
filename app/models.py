from sqlalchemy import Column, Integer, String, Date, Enum,Table, ForeignKey, Text, DateTime, BigInteger
from .database import Base
from sqlalchemy.orm import relationship
from .schemas import BodyGoal
from datetime import datetime, timezone


group_members = Table('group_members', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('group_id', Integer, ForeignKey('groups.id'))
)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    phone_number = Column(BigInteger, unique=True, index=True, nullable=False)
    profile_picture = Column(String, nullable=True)
    working_out_from = Column(Date, nullable=False)
    body_goal = Column(Enum(BodyGoal), nullable=False)

class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    members = relationship("User", secondary=group_members, back_populates="groups")

User.groups = relationship("Group", secondary=group_members, back_populates="members")

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)  # For text content
    image_url = Column(String, nullable=True)  # For image URL
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id'), nullable=False)
    user = relationship("User", back_populates="posts")
    group = relationship("Group", back_populates="posts")

User.posts = relationship("Post", back_populates="user")
Group.posts = relationship("Post", back_populates="group")


class DailyQuestion(Base):
    __tablename__ = 'daily_questions'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime(timezone=True), default=datetime.now(timezone.utc))
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    workout_plan = Column(Text, nullable=False)
    guilty_action = Column(Text, nullable=False)
    user = relationship("User", back_populates="daily_questions")

User.daily_questions = relationship("DailyQuestion", back_populates="user")