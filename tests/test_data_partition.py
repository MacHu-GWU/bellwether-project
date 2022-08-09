# -*- coding: utf-8 -*-

import os
import pytest

from datetime import datetime
from bellwether.data_partition import (
    get_pkey_by_second,
    get_pkey_by_5_second,
    get_pkey_by_15_second,
    get_pkey_by_minute,
    get_pkey_by_5_minute,
    get_pkey_by_10_minute,
    get_pkey_by_15_minute,
    get_pkey_by_half_hour,
    get_pkey_by_hour,
    get_pkey_by_2_hour,
    get_pkey_by_4_hour,
    get_pkey_by_6_hour,
    get_pkey_by_half_day,
    get_pkey_by_day,
)


def test_get_pkey_by_second():
    assert (
        get_pkey_by_second(datetime(2000, 1, 1, 8, 13, 47))
        == "year=2000/month=01/day=01/hour=08/minute=13/second=47"
    )


def test_get_pkey_by_5_second():
    assert (
        get_pkey_by_5_second(datetime(2000, 1, 1, 8, 13, 47))
        == "year=2000/month=01/day=01/hour=08/minute=13/five_second=09"
    )


def test_get_pkey_by_15_second():
    assert (
        get_pkey_by_15_second(datetime(2000, 1, 1, 8, 13, 47))
        == "year=2000/month=01/day=01/hour=08/minute=13/fifteen_second=03"
    )


def test_get_pkey_by_minute():
    assert (
        get_pkey_by_minute(datetime(2000, 1, 1, 8, 13, 47))
        == "year=2000/month=01/day=01/hour=08/minute=13"
    )


def test_get_pkey_by_5_minute():
    assert (
        get_pkey_by_5_minute(datetime(2000, 1, 1, 8, 13, 47))
        == "year=2000/month=01/day=01/hour=08/five_minute=02"
    )


def test_get_pkey_by_10_minute():
    assert (
        get_pkey_by_10_minute(datetime(2000, 1, 1, 8, 13, 47))
        == "year=2000/month=01/day=01/hour=08/ten_minute=1"
    )


def test_get_pkey_by_15_minute():
    assert (
        get_pkey_by_15_minute(datetime(2000, 1, 1, 8, 13, 47))
        == "year=2000/month=01/day=01/hour=08/quarter=0"
    )


def test_get_pkey_by_half_hour():
    assert (
        get_pkey_by_half_hour(datetime(2000, 1, 1, 8, 13, 47))
        == "year=2000/month=01/day=01/hour=08/half_hour=0"
    )


def test_get_pkey_by_hour():
    assert get_pkey_by_hour(datetime(2000, 1, 1)) == "year=2000/month=01/day=01/hour=00"


def test_get_pkey_by_2_hour():
    assert (
        get_pkey_by_2_hour(datetime(2000, 1, 1, 8, 13, 47))
        == "year=2000/month=01/day=01/two_hour=04"
    )


def test_get_pkey_by_4_hour():
    assert (
        get_pkey_by_4_hour(datetime(2000, 1, 1, 8, 13, 47))
        == "year=2000/month=01/day=01/four_hour=2"
    )


def test_get_pkey_by_6_hour():
    assert (
        get_pkey_by_6_hour(datetime(2000, 1, 1, 8, 13, 47))
        == "year=2000/month=01/day=01/six_hour=1"
    )


def test_get_pkey_by_half_day():
    assert (
        get_pkey_by_half_day(datetime(2000, 1, 1, 8, 13, 47))
        == "year=2000/month=01/day=01/half_day=0"
    )


def test_get_pkey_by_day():
    assert get_pkey_by_day(datetime(2000, 1, 1)) == "year=2000/month=01/day=01"


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
        "-s",
        "--tb=native",
        f"--rootdir={dir_project_root}",
        "--cov=bellwether.data_partition",
        "--cov-report",
        "term-missing",
        "--cov-report",
        f"html:{dir_htmlcov}",
        abspath,
    ]
    subprocess.run(args)
