from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from .crud import create_daily_question
from .database import SessionLocal
from . import models
from . import schemas

def send_daily_questions():
    # Open a new database session
    db = SessionLocal()
    
    # Get all users
    users = db.query(models.User).all()
    
    # For each user, create a daily question entry
    for user in users:
        workout_plan = "What is your workout plan for tomorrow?"
        guilty_action = "Something you did today that makes you feel guilty"
        
        # You can adjust the prompt messages as needed
        daily_question = schemas.DailyQuestionCreate(
            workout_plan=workout_plan,
            guilty_action=guilty_action,
            user_id=user.id
        )
        create_daily_question(db=db, question=daily_question)
    
    # Commit and close the database session
    db.commit()
    db.close()

scheduler = BackgroundScheduler()
scheduler.add_job(send_daily_questions, 'cron', hour=23, minute=59)  # Adjust as needed
scheduler.start()
