from ninja import Router

from login.models import User
from zadania.models import Solution, Comment
from .schemas import UserProfileOut

from django.db.models import Avg

router = Router()

# Base for XP gain.

BASE_XP = 1000


"""
Slightly GPT-generated,beware.
"""
@router.get("/users/{user_id}/profile", response=UserProfileOut)
def user_profile(request, user_id: int):
    user = User.objects.get(pk=user_id)
    
    # data assembly
    xp = user.xp
    level = user.lvl
    xp_to_next_level = (level * BASE_XP) - xp
    completed = Solution.objects.filter(user=user, completed=True).count()
    comments = Comment.objects.filter(user=user).count()
    avg_rating = Comment.objects.filter(user=user).aggregate(avg=Avg("rating"))["avg"] or 0.0

    return {
        "username": user.username,
        "level": level,
        "totalXP": xp,
        "xpToNextLevel": xp_to_next_level,
        "completedExercises": completed,
        "commentsPosted": comments,
        "averageExerciseRating": round(avg_rating, 2),
    }

    
