from dataclasses import dataclass
from enum import Enum


class Product(str, Enum):
    STANDARD = "standard"
    VULNERABLE = "vulnerable"


class Channel(str, Enum):
    EMAIL = "email"
    SLACK = "slack"


class Role(str, Enum):
    RISK_ANALYST = "Risk Analyst"
    COLLECTIONS_OFFICER = "Collections Officer"
    UNDERWRITER = "Underwriter"
    VULNERABLE_SUPPORT_LEAD = "Vulnerable Support Lead"


class Outcome(str, Enum):
    AUTO_APPROVE = "auto-approve"
    REVIEW = "review"


@dataclass(frozen=True)
class HolidayRequest:
    amount_gbp: int
    holiday_months: int
    in_arrears: bool
    product: Product


@dataclass(frozen=True)
class Notification:
    channel: Channel
    role: Role


@dataclass(frozen=True)
class Decision:
    outcome: Outcome
    notification: Notification | None = None
