# -*- coding: utf-8 -*-

import os
import pytest
from datetime import datetime, timezone, timedelta

from bellwether.time_window import (
    ONE_QUARTER,
    MILLI_SEC,
    TimeWindow,
)


class TestTimeWindow:
    def test_datetime_compare_precision(self):
        """
        Verify that the Python datetime object compare operator precision is
        microsecond.
        """
        dt = datetime(1970, 1, 1, 0, 0, 0, 0, tzinfo=timezone.utc)
        assert dt == dt.replace(microsecond=0)
        assert dt == dt.replace(microsecond=1000) - timedelta(milliseconds=1)
        assert dt != dt.replace(microsecond=1)

    def test_validator(self):
        with pytest.raises(ValueError):
            TimeWindow(
                interval=100,  # invalid
                resolution=1,  # 1 microsecond
                seq=0,
            )

        with pytest.raises(ValueError):
            TimeWindow(
                interval=60000000,  # 1 min
                resolution=60,  # invalid
                seq=0,
            )

    def test_cached_property(self):
        tw1 = TimeWindow(seq=0, interval=ONE_QUARTER, resolution=MILLI_SEC)
        tw2 = TimeWindow(seq=1, interval=ONE_QUARTER, resolution=MILLI_SEC)
        assert (tw2.start_time - tw1.start_time).total_seconds() == 900

        assert (tw1.end_ts - tw1.start_ts + MILLI_SEC) == ONE_QUARTER
        assert tw2.start_ts - tw1.end_ts == MILLI_SEC

    def test_find_by_dt(self):
        dt = datetime(2022, 6, 1, 8, 24, 0, 0, tzinfo=timezone.utc)
        tw = TimeWindow.find_by_dt(dt, ONE_QUARTER, MILLI_SEC)
        assert str(tw.start_time) == "2022-06-01 08:15:00+00:00"
        assert str(tw.end_time) == "2022-06-01 08:29:59.999000+00:00"


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
        "--cov=bellwether.time_window",
        "--cov-report", "term-missing",
        "--cov-report", f"html:{dir_htmlcov}",
        abspath,
    ]
    subprocess.run(args)
