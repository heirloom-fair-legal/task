from holiday_router.models import Decision, HolidayRequest


def route(request: HolidayRequest) -> Decision:
    raise NotImplementedError("Implement route() using the workflow in the README.")
