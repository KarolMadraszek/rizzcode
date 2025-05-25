from pydantic import BaseModel


class UserProfileOut(BaseModel):
    username: str
    level: int
    totalXP: int
    xpToNextLevel: int
    completedExercises: int
    commentsPosted: int
    averageExerciseRating: float

    class Config:
        orm_mode = True
