from __future__ import annotations

import argparse
from datetime import date, timedelta


WEEKDAYS_MON_FIRST = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
WEEKDAYS_SUN_FIRST = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]
MONTH_NAMES = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def is_leap(year: int) -> bool:
    """Return True if year is a leap year (Gregorian)."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def days_in_month(year: int, month: int) -> int:
    """Return the number of days in the given month of the year."""
    if month < 1 or month > 12:
        raise ValueError("month must be in 1..12")
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    if month in (4, 6, 9, 11):
        return 30
    return 29 if is_leap(year) else 28  # February


def month_matrix(year: int, month: int, sunday_first: bool = False) -> list[list[int]]:
    """
    Build a 6x7 matrix of the month where 0 indicates padding days.

    - Rows are weeks.
    - Columns are weekdays (Mon..Sun by default, or Sun..Sat if sunday_first).
    """
    first = date(year, month, 1)
    # Python's weekday(): Monday=0..Sunday=6
    first_wd = first.weekday()  # 0..6 (Mon..Sun)
    if sunday_first:
        # Convert to Sunday=0..Saturday=6
        first_wd = (first_wd + 1) % 7

    dim = days_in_month(year, month)

    weeks: list[list[int]] = []
    day_counter = 1

    # First week padding
    week = [0] * 7
    for i in range(first_wd, 7):
        week[i] = day_counter
        day_counter += 1
    weeks.append(week)

    # Remaining weeks
    while day_counter <= dim:
        week = [0] * 7
        for i in range(7):
            if day_counter <= dim:
                week[i] = day_counter
                day_counter += 1
        weeks.append(week)

    # Ensure 6 weeks for consistent rendering
    while len(weeks) < 6:
        weeks.append([0] * 7)

    return weeks


def format_month(year: int, month: int, sunday_first: bool = False, width: int = 20) -> str:
    """Return a formatted monthly calendar as a string (similar to `cal`)."""
    title = f"{MONTH_NAMES[month - 1]} {year}"
    header = title.center(width).rstrip()
    weekdays = WEEKDAYS_SUN_FIRST if sunday_first else WEEKDAYS_MON_FIRST
    days_header = " ".join(weekdays)

    lines = [header, days_header]
    for week in month_matrix(year, month, sunday_first):
        line_parts = ["  " if d == 0 else f"{d:2d}" for d in week]
        lines.append(" ".join(line_parts))
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Print a simple monthly calendar.")
    parser.add_argument("--year", type=int, help="Year (e.g., 2025)")
    parser.add_argument("--month", type=int, help="Month 1-12")
    parser.add_argument(
        "--sunday-first",
        action="store_true",
        help="Start weeks on Sunday instead of Monday",
    )
    return parser.parse_args()


def main() -> None:
    """Main function to demonstrate the calendar output."""
    args = parse_args()
    today = date.today()
    year = args.year or today.year
    month = args.month or today.month

    print(format_month(year, month, sunday_first=args.sunday_first))


if __name__ == "__main__":
    main()

