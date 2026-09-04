import pytest

from holiday_router.engine import route
from holiday_router.models import Channel, HolidayRequest, Notification, Product, Role
from holiday_router.notify import notify, send_email, send_slack


def test_send_slack_prints_expected_line(capsys):
    send_slack(Role.VULNERABLE_SUPPORT_LEAD)
    captured = capsys.readouterr()
    assert captured.out.strip() == (
        "sending approval request via Slack to Vulnerable Support Lead"
    )


def test_send_email_prints_expected_line(capsys):
    send_email(Role.RISK_ANALYST)
    captured = capsys.readouterr()
    assert captured.out.strip() == "sending approval request via Email to Risk Analyst"


def test_notify_dispatches_to_channel(capsys):
    notify(Notification(channel=Channel.SLACK, role=Role.COLLECTIONS_OFFICER))
    captured = capsys.readouterr()
    assert captured.out.strip() == (
        "sending approval request via Slack to Collections Officer"
    )


@pytest.mark.skip(reason="Implement route() so the engine calls notify, then unskip")
def test_risk_analyst_example_uses_email_mock(capsys):
    request = HolidayRequest(
        amount_gbp=500,
        holiday_months=1,
        in_arrears=True,
        product=Product.STANDARD,
    )
    decision = route(request)
    assert decision.notification is not None
    notify(decision.notification)
    captured = capsys.readouterr()
    assert "Email" in captured.out
    assert "Risk Analyst" in captured.out
