# -*- coding: utf-8 -*-

from datetime import date, datetime, timedelta, timezone

# ------------------------------------------------------------------------------
# Time integer constants in microseconds
# ------------------------------------------------------------------------------
MICRO_SEC = 1
MILLI_SEC = 1000 * MICRO_SEC
SEC = 1000 * MILLI_SEC

ONE_SEC = SEC
FIVE_SEC = 5 * ONE_SEC
FIFTEEN_SEC = 15 * ONE_SEC

ONE_MINUTE = 60 * ONE_SEC
FIVE_MINUTE = 5 * ONE_MINUTE
TEN_MINUTE = 10 * ONE_MINUTE
ONE_QUARTER = 15 * ONE_MINUTE
HALF_HOUR = 30 * ONE_MINUTE

ONE_HOUR = 60 * ONE_MINUTE
TWO_HOUR = 2 * ONE_HOUR
FOUR_HOUR = 4 * ONE_HOUR
SIX_HOUR = 6 * ONE_HOUR
HALF_DAY = 12 * ONE_HOUR

ONE_DAY = 24 * ONE_HOUR

EPOCH = datetime(1970, 1, 1, 0, 0, 0, 0, tzinfo=timezone.utc)


def utc_now(delta_seconds: int = 0) -> datetime:
    """
    Get the timezone aware UTC now datetime.

    :param delta_seconds: shift the time for x seconds. This parameter can be
        used to simulate a "historical" or "future" UTC now.
    """
    utcnow = datetime.utcnow().replace(tzinfo=timezone.utc)
    if delta_seconds == 0:
        return utcnow
    else:
        return utcnow + timedelta(seconds=delta_seconds)


def ensure_utc_timezone(dt: datetime):
    """
    Ensure the datetime object is timezone aware and in UTC timezone
    """
    if not dt.tzinfo == timezone.utc:
        raise ValueError(f"{dt} is not a timezone aware UTC time")


def round_to_begin_of_the_day(dt: datetime) -> datetime:
    """
    Round to 00:00:00 AM
    """
    return dt.replace(hour=0, minute=0, second=0, microsecond=0)


def round_to_end_of_the_day(dt: datetime) -> datetime:
    """
    Round to 23:59:59.999999 PM
    """
    return dt.replace(hour=23, minute=59, second=59, microsecond=999999)


def round_to_begin_of_the_next_day(dt: datetime) -> datetime:
    return round_to_begin_of_the_day(dt) + timedelta(days=1)


def round_to_end_of_the_previous_day(dt: datetime) -> datetime:
    return round_to_end_of_the_day(dt) - timedelta(days=1)


def date_to_datetime(the_date: date) -> datetime:
    """
    Convert date object to UTC aware datetime object.
    """
    return datetime(
        the_date.year,
        the_date.month,
        the_date.day,
        tzinfo=timezone.utc,
    )


def from_utc_timestamp(ts: int) -> datetime:
    """
    Assuming the timestamp is between 2000-01-01 to 2100-01-01
    Smartly convert an integer timestamp to timezone aware UTC time.
    Automatically detect the time precision, could be second, millisecond,
    microsecond.

    :param ts: UTC timestamp integer.

    .. note::

        - 2000-01-01 timestamp =   946,684,800
        - 2022-06-01 timestamp = 1,654,041,600
        - 2100-01-01 timestamp = 4,102,444,800
    """
    ts_2100_1_1 = 4102444800
    if ts < 0:
        raise ValueError
    elif ts <= ts_2100_1_1:
        return datetime.utcfromtimestamp(ts).replace(tzinfo=timezone.utc)
    elif ts <= ts_2100_1_1 * 1000:
        return datetime.utcfromtimestamp(ts / 1000).replace(tzinfo=timezone.utc)
    elif ts <= ts_2100_1_1 * 1000000:
        return datetime.utcfromtimestamp(ts / 1000000).replace(tzinfo=timezone.utc)
    else:
        raise ValueError


def to_timestamp_in_seconds(dt: datetime) -> int:
    """
    Convert datetime object to its timestamp in seconds,
    ignore the milliseconds and
    microseconds part.
    """
    return int(dt.timestamp())


def to_timestamp_in_milliseconds(dt: datetime) -> int:
    """
    Convert datetime object to its timestamp in milliseconds,
    ignore the microseconds part.
    """
    return int(dt.timestamp() * 1000)


def to_timestamp_in_microseconds(dt: datetime) -> int:
    """
    Convert datetime object to its timestamp in microseconds
    """
    return int(dt.timestamp() * 1000000)
