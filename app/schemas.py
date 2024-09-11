from pydantic import BaseModel, Field, conint, HttpUrl
from datetime import date, datetime, timezone
from enum import Enum
from typing import Optional, List


class BodyGoal(str, Enum):
    bulk = "bulk"
    cut = "cut"
    athletic = "athletic"

class UserRegister(BaseModel):
    name: str = Field(..., example="John Doe")  # Required field
    phone_number: int = Field(..., gt=0, example=1234567890)  # Required numeric field
    profile_picture: Optional[str] = Field(None, example="http://example.com/image.jpg")
    working_out_from: date = Field(..., example="2023-01-01")  # Required field
    body_goal: BodyGoal  # Required field

class GroupMember(BaseModel):
    phone_number: int = Field(..., gt=0, example=1234567890)  # Required numeric field

class GroupCreate(BaseModel):
    name: str = Field(..., example="Fitness Enthusiasts")  # Group name
    description: Optional[str] = Field(None, example="A group for those serious about fitness.")  # Optional description
    members: List[GroupMember] = Field(..., example=[{"phone_number": 1234567890}, {"phone_number": 9876543210}])  # List of members by phone number

class GroupResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    members: List[int]  # Assuming you'll return a list of phone numbers or user IDs

    class Config:
        orm_mode = True


class PostCreate(BaseModel):
    content: str = Field(..., example="Today I did a 5km run.")
    image_url: Optional[str] = None  # URL for the image (optional)
    group_id: int
    user_id: int  # ID of the group where the post belongs

class PostResponse(BaseModel):
    id: int
    content: str
    image_url: Optional[HttpUrl] = None
    user_id: int
    group_id: int

    class Config:
        orm_mode = True

class DailyQuestionCreate(BaseModel):
    workout_plan: str = Field(..., example="I plan to run 5km tomorrow.")
    guilty_action: str = Field(..., example="I skipped my workout today.")
    user_id: int
    date: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))