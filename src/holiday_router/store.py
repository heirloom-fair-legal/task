# In-memory list of requests. Document the schema in the README —
# no real database layer is required.

from holiday_router.models import HolidayRequest

_requests: list[HolidayRequest] = []


def save(request: HolidayRequest) -> None:
    _requests.append(request)


def all_requests() -> list[HolidayRequest]:
    return list(_requests)
