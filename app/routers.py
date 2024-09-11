from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .schemas import UserRegister
from .crud import create_user,create_group
from . import schemas, crud, models
from .database import get_db

router = APIRouter()

@router.post("/register/", response_model=UserRegister)
def register_user(user: UserRegister, db: Session = Depends(get_db)):
    db_user = create_user(db=db, user=user)
    return db_user

@router.post("/create_group/", response_model=schemas.GroupResponse)
def create_group_endpoint(group: schemas.GroupCreate, db: Session = Depends(get_db)):
    db_group = create_group(db=db, group=group)
    
    # Extract the user IDs (or phone numbers) from the members
    group_response = schemas.GroupResponse(
        id=db_group.id,
        name=db_group.name,
        description=db_group.description,
        members=[member.phone_number for member in db_group.members] 
    )
    return group_response

@router.post("/posts/", response_model=schemas.PostResponse)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    db_post = crud.create_post(db=db, post=post)
    return db_post


@router.post("/daily_questions/", response_model=schemas.DailyQuestionCreate)
def create_daily_question(question: schemas.DailyQuestionCreate, db: Session = Depends(get_db)):
    db_question = crud.create_daily_question(db=db, question=question)
    return db_question
