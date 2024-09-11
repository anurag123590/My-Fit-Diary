from . import models, schemas
from .models import User
from sqlalchemy.orm import Session
from .schemas import UserRegister
from datetime import datetime, timezone

def create_user(db: Session, user: UserRegister):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
 
def get_user_by_phone(db: Session, phone_number: int):
    return db.query(models.User).filter(models.User.phone_number == phone_number).first()

def create_group(db: Session, group: schemas.GroupCreate):
    db_group = models.Group(name=group.name, description=group.description)
    for member in group.members:
        user = get_user_by_phone(db, phone_number=member.phone_number)
        if user:
            db_group.members.append(user)
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    print (db_group)
    return db_group

def create_post(db: Session, post: schemas.PostCreate):
    db_post = models.Post(
        content=post.content,
        image_url=post.image_url,
        user_id=post.user_id,
        group_id=post.group_id
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def create_daily_question(db: Session, question: schemas.DailyQuestionCreate):
    db_question = models.DailyQuestion(
        date= datetime.now(timezone.utc),
        workout_plan=question.workout_plan,
        guilty_action=question.guilty_action,
        user_id=question.user_id
    )
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

