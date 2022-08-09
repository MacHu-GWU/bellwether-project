# -*- coding: utf-8 -*-

import os
import pytest
from datetime import datetime, date, timezone
from bellwether.time_utils import (
    utc_now,
    ensure_utc_timezone,
    round_to_begin_of_the_day,
    round_to_end_of_the_day,
    round_to_begin_of_the_next_day,
    round_to_end_of_the_previous_day,
    date_to_datetime,
    from_utc_timestamp,
    to_timestamp_in_seconds,
    to_timestamp_in_milliseconds,
    to_timestamp_in_microseconds,
)


def test_utc_now():
    now = utc_now()
    assert now.tzinfo == timezone.utc

    # test delta_seconds parameter
    now1 = utc_now()
    now2 = utc_now(delta_seconds=-10)
    now3 = utc_now(delta_seconds=10)
    assert (now1 - now2).total_seconds() == pytest.approx(10, 0.1)
    assert (now3 - now1).total_seconds() == pytest.approx(10, 0.1)


def test_ensure_utc_timezone():
    with pytest.raises(ValueError):
        ensure_utc_timezone(datetime.now())

    ensure_utc_timezone(utc_now())


def test_round_to_begin_of_the_day():
    assert round_to_begin_of_the_day(datetime(2000, 1, 5, 8)) == datetime(2000, 1, 5)


def test_round_to_end_of_the_day():
    assert round_to_end_of_the_day(datetime(2000, 1, 5, 8)) == datetime(
        2000, 1, 5, 23, 59, 59, 999999
    )


def test_round_to_begin_of_the_next_day():
    assert round_to_begin_of_the_next_day(datetime(2000, 1, 5, 8)) == datetime(
        2000, 1, 6
    )


def test_round_to_end_of_the_previous_day():
    assert round_to_end_of_the_previous_day(datetime(2000, 1, 5, 8)) == datetime(
        2000, 1, 4, 23, 59, 59, 999999
    )


def test_date_to_datetime():
    assert date_to_datetime(date(2000, 1, 1)) == datetime(2000, 1, 1, tzinfo=timezone.utc)


def test_from_utc_timestamp():
    dt = from_utc_timestamp(1654041600)
    assert str(dt) == "2022-06-01 00:00:00+00:00"

    dt = from_utc_timestamp(0)
    assert str(dt) == "1970-01-01 00:00:00+00:00"

    dt = from_utc_timestamp(1654041600123)
    assert str(dt) == "2022-06-01 00:00:00.123000+00:00"

    dt = from_utc_timestamp(1654041600123456)
    assert str(dt) == "2022-06-01 00:00:00.123456+00:00"

    with pytest.raises(ValueError):
        from_utc_timestamp(-1)

    with pytest.raises(ValueError):
        from_utc_timestamp(999999999999999999)


def test_to_timestamp_in_seconds():
    dt = datetime(1970, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
    assert to_timestamp_in_seconds(dt) == 0

    dt = datetime(1970, 1, 1, 0, 0, 0, 123000, tzinfo=timezone.utc)
    assert to_timestamp_in_seconds(dt) == 0

    dt = datetime(1970, 1, 1, 0, 0, 0, 999999, tzinfo=timezone.utc)
    assert to_timestamp_in_seconds(dt) == 0


def test_to_timestamp_in_milliseconds():
    dt = datetime(1970, 1, 1, 0, 0, 1, tzinfo=timezone.utc)
    assert to_timestamp_in_milliseconds(dt) == 1000

    dt = datetime(1970, 1, 1, 0, 0, 1, 123000, tzinfo=timezone.utc)
    assert to_timestamp_in_milliseconds(dt) == 1123

    dt = datetime(1970, 1, 1, 0, 0, 1, 123456, tzinfo=timezone.utc)
    assert to_timestamp_in_milliseconds(dt) == 1123

    dt = datetime(1970, 1, 1, 0, 0, 1, 123999, tzinfo=timezone.utc)
    assert to_timestamp_in_milliseconds(dt) == 1123


def test_to_timestamp_in_microseconds():
    dt = datetime(1970, 1, 1, 0, 0, 1, 0, tzinfo=timezone.utc)
    assert to_timestamp_in_microseconds(dt) == 1000000

    dt = datetime(1970, 1, 1, 0, 0, 1, 123, tzinfo=timezone.utc)
    assert to_timestamp_in_microseconds(dt) == 1000123

    dt = datetime(1970, 1, 1, 0, 0, 1, 999999, tzinfo=timezone.utc)
    assert to_timestamp_in_microseconds(dt) == 1999999

    dt = datetime(2022, 6, 1, 0, 0, 0, 0, tzinfo=timezone.utc)
    assert to_timestamp_in_microseconds(dt) == 1654041600000000


if __name__ == "__main__":
    import sys
    import subprocess

    abspath = os.path.abspath(__file__)
    dir_project_root = os.path.dirname(abspath)
    for _ in range(10):
        if os.path.exists(os.path.join(dir_project_root, ".git")):
            break
        else:
            dir_project_root = os.path.dirname(dir_project_root)
    else:
        raise FileNotFoundError("cannot find project root dir!")
    dir_htmlcov = os.path.join(dir_project_root, "htmlcov")
    bin_pytest = os.path.join(os.path.dirname(sys.executable), "pytest")

    args = [
        bin_pytest,
        "-s", "--tb=native",
        f"--rootdir={dir_project_root}",
        "--cov=bellwether.time_utils",
        "--cov-report", "term-missing",
        "--cov-report", f"html:{dir_htmlcov}",
        abspath,
    ]
    subprocess.run(args)
