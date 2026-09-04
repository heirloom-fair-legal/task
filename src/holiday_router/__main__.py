from __future__ import annotations

import argparse
import sys

from holiday_router.engine import route
from holiday_router.models import HolidayRequest, Product
from holiday_router.notify import notify


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="holiday_router",
        description="Route a payment holiday request through the configured workflow.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    run = subparsers.add_parser("run", help="Evaluate one payment holiday request")
    run.add_argument("--amount", type=int, required=True, help="Current monthly payment in GBP")
    run.add_argument("--months", type=int, required=True, help="Requested holiday length (1–6)")
    run.add_argument(
        "--in-arrears",
        action="store_true",
        help="Borrower has already missed at least one payment",
    )
    run.add_argument(
        "--product",
        choices=[p.value for p in Product],
        required=True,
        help="Loan product",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    request = HolidayRequest(
        amount_gbp=args.amount,
        holiday_months=args.months,
        in_arrears=args.in_arrears,
        product=Product(args.product),
    )
    decision = route(request)
    print(f"outcome: {decision.outcome.value}")
    if decision.notification is not None:
        notify(decision.notification)
    return 0


if __name__ == "__main__":
    sys.exit(main())
