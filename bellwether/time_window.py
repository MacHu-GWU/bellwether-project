# -*- coding: utf-8 -*-

import dataclasses
from functools import cached_property
from datetime import datetime, timedelta

from .time_utils import (
    MICRO_SEC,
    MILLI_SEC,
    SEC,
    ONE_SEC,
    FIVE_SEC,
    FIFTEEN_SEC,
    ONE_MINUTE,
    FIVE_MINUTE,
    TEN_MINUTE,
    ONE_QUARTER,
    HALF_HOUR,
    ONE_HOUR,
    TWO_HOUR,
    FOUR_HOUR,
    SIX_HOUR,
    HALF_DAY,
    ONE_DAY,
    EPOCH,
    to_timestamp_in_seconds,
    to_timestamp_in_milliseconds,
    to_timestamp_in_microseconds,
)
from . import data_partition

_VALID_INTERVAL = {
    ONE_SEC,
    FIVE_SEC,
    FIFTEEN_SEC,
    ONE_MINUTE,
    FIVE_MINUTE,
    TEN_MINUTE,
    ONE_QUARTER,
    HALF_HOUR,
    ONE_HOUR,
    TWO_HOUR,
    FOUR_HOUR,
    SIX_HOUR,
    HALF_DAY,
    ONE_DAY,
}

_VALID_RESOLUTION = {
    SEC,
    MILLI_SEC,
    MICRO_SEC,
}

_slots = (
    "interval", "resolution", "seq",
    "start_time", "end_time",
    "start_ts", "end_ts",
)

GET_PKEY_FUNC_MAPPER = {
    ONE_SEC: data_partition.get_pkey_by_second,
    FIVE_SEC: data_partition.get_pkey_by_5_second,
    FIFTEEN_SEC: data_partition.get_pkey_by_15_second,
    ONE_MINUTE: data_partition.get_pkey_by_minute,
    FIVE_MINUTE: data_partition.get_pkey_by_5_minute,
    TEN_MINUTE: data_partition.get_pkey_by_10_minute,
    ONE_QUARTER: data_partition.get_pkey_by_15_minute,
    HALF_HOUR: data_partition.get_pkey_by_half_hour,
    ONE_HOUR: data_partition.get_pkey_by_hour,
    TWO_HOUR: data_partition.get_pkey_by_2_hour,
    FOUR_HOUR: data_partition.get_pkey_by_4_hour,
    SIX_HOUR: data_partition.get_pkey_by_6_hour,
    HALF_DAY: data_partition.get_pkey_by_half_day,
    ONE_DAY: data_partition.get_pkey_by_day,
}
"""
Find the corresponding get partition key function based on time window interval
"""


@dataclasses.dataclass
class TimeWindow:
    """
    A timeseries task in specific time window.

    :param interval: the length of the time window. 15 minutes window means
        ``interval = 15 * 60 * 1000 * 1000``.
    :param resolution: the time precision. 1 second = 1,000,000; 1 millisecond
        = 1,000; 1 microsecond = 1.
    :param seq: the nth sequence from EPOCH ("1970-01-01 00:00:00.000000")

    .. note::
        All integer is in microseconds, i.e. 1 = 0.000001 seconds.
    """
    seq: int = dataclasses.field()
    interval: int = dataclasses.field()
    resolution: int = dataclasses.field()

    def _check_interval(self):
        if self.interval not in _VALID_INTERVAL:
            raise ValueError("Not a valid interval!")

    def _check_resolution(self):
        if self.resolution not in _VALID_RESOLUTION:
            raise ValueError("Not a valid resolution!")

    def __post_init__(self):
        self._check_interval()
        self._check_resolution()

    @cached_property
    def start_time(self) -> datetime:
        """
        Example:
        With 15 minutes interval, 1 milliseconds resolution, the 1th task is
        ("1970-01-01 00:15:00.000Z", "1970-01-01 00:29:59.999Z")
        """
        return EPOCH + timedelta(microseconds=self.seq * self.interval)

    @cached_property
    def end_time(self) -> datetime:
        """
        Example:
        With 15 minutes interval, 1 milliseconds resolution, the 1th task is
        ("1970-01-01 00:15:00.000Z", "1970-01-01 00:29:59.999Z")
        """
        return self.start_time + timedelta(microseconds=self.interval - self.resolution)

    @cached_property
    def start_ts(self) -> int:
        """
        Timestamp of the :meth:`TimeWindow.start_time`
        """
        return self.seq * self.interval

    @cached_property
    def end_ts(self) -> int:
        """
        Timestamp of the :meth:`TimeWindow.end_time`
        """
        return (self.seq + 1) * self.interval - self.resolution

    @classmethod
    def find_by_dt(
        cls,
        dt: datetime,
        interval: int,
        resolution: int,
    ) -> 'TimeWindow':
        """
        Find the corresponding TimeWindow object.
        """
        seq = to_timestamp_in_microseconds(dt) // interval
        return cls(
            seq=seq,
            interval=interval,
            resolution=resolution,
        )
