import uuid

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Boolean, DateTime, Float
from datetime import datetime
from backend.app.core.database import Base
from uuid import uuid4


class CaloriesPredictModel(Base):
    __tablename__ = "calories_predict"

    id: Mapped[str] = mapped_column(String(36),primary_key=True, nullable=False, default=lambda: str(uuid4()))
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    gender: Mapped[str] = mapped_column(String(255), nullable=False)
    weight: Mapped[float] = mapped_column(Float, nullable=False)
    height: Mapped[float] = mapped_column(Float, nullable=False)
    bmi: Mapped[float] = mapped_column(Float, nullable=False)
    workout_req: Mapped[float] = mapped_column(Float, nullable=False)
    session_duration: Mapped[float] = mapped_column(Float, nullable=False)
    workout_type: Mapped[str] = mapped_column(String(255), nullable=False)
    daily_meals: Mapped[float] = mapped_column(Float, nullable=False)
    calories: Mapped[float] = mapped_column(Float, nullable=True)
    physical_exercise: Mapped[float] = mapped_column(Float, nullable=False)
    experience_level: Mapped[float] = mapped_column(Float, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)


# common_features = [
#     'Age',
#     'Gender',
#     'Weight (kg)',
#     'Height (m)',
#     'BMI',
#     'Workout_Frequency (days/week)',
#     'Session_Duration (hours)',
#     'Workout_Type',
#     'Daily meals frequency',
#     'diet_type',
#     'Calories',
#     'Physical exercise',
#     'Experience_Level',
# ]
