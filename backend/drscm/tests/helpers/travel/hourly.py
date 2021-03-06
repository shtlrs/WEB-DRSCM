from drscm.models import HourlyTravel, Project
from faker import Faker

from utils.date import purify_timestamp

faker = Faker()


def create_random_hourly_travel(
    timestamp=None, project: Project = None, rate: float = 2.5, hours: int = 1, save=False
) -> HourlyTravel:

    timestamp = timestamp or faker.future_datetime().timestamp()
    timestamp = purify_timestamp(timestamp)

    hourly_travel = HourlyTravel(timestamp=timestamp, hours=hours, rate=rate)

    if project:
        hourly_travel.project = project
        hourly_travel.owner = project.owner

    if save:
        hourly_travel.save()

    return hourly_travel
