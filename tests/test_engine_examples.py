import pytest

from holiday_router.engine import route
from holiday_router.models import Channel, HolidayRequest, Outcome, Product, Role


@pytest.mark.skip(reason="Implement route() and unskip")
def test_standard_short_holiday_not_in_arrears_auto_approves():
    request = HolidayRequest(
        amount_gbp=250,
        holiday_months=2,
        in_arrears=False,
        product=Product.STANDARD,
    )
    decision = route(request)
    assert decision.outcome is Outcome.AUTO_APPROVE
    assert decision.notification is None


@pytest.mark.skip(reason="Implement route() and unskip")
def test_standard_in_arrears_high_amount_emails_risk_analyst():
    request = HolidayRequest(
        amount_gbp=500,
        holiday_months=1,
        in_arrears=True,
        product=Product.STANDARD,
    )
    decision = route(request)
    assert decision.outcome is Outcome.REVIEW
    assert decision.notification is not None
    assert decision.notification.channel is Channel.EMAIL
    assert decision.notification.role is Role.RISK_ANALYST


@pytest.mark.skip(reason="Implement route() and unskip")
def test_vulnerable_product_slacks_vulnerable_support_lead():
    request = HolidayRequest(
        amount_gbp=200,
        holiday_months=1,
        in_arrears=False,
        product=Product.VULNERABLE,
    )
    decision = route(request)
    assert decision.outcome is Outcome.REVIEW
    assert decision.notification is not None
    assert decision.notification.channel is Channel.SLACK
    assert decision.notification.role is Role.VULNERABLE_SUPPORT_LEAD
