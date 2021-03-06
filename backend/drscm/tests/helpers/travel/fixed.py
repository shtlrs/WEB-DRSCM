from drscm.models import FixedTravel, Project
from utils.date import purify_timestamp
from faker import Faker

faker = Faker()


def create_random_fixed_travel(
    timestamp=None,
    project: Project = None,
    rate: float = 2.5,
    occurrences: int = 1,
    save=False,
) -> FixedTravel:

    timestamp = timestamp or faker.future_datetime().timestamp()
    timestamp = purify_timestamp(timestamp)
    fixed_travel = FixedTravel(timestamp=timestamp, occurrences=occurrences, rate=rate)

    if project:
        fixed_travel.project = project
        fixed_travel.owner = project.owner

    if save:
        fixed_travel.save()

    return fixed_travel
