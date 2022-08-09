# -*- coding: utf-8 -*-

import typing as T
from datetime import datetime


def get_pkey_by_second(dt: datetime) -> str:
    return "/".join(
        [
            f"year={dt.year}",
            f"month={str(dt.month).zfill(2)}",
            f"day={str(dt.day).zfill(2)}",
            f"hour={str(dt.hour).zfill(2)}",
            f"minute={str(dt.minute).zfill(2)}",
            f"second={str(dt.second).zfill(2)}",
        ]
    )


def get_pkey_by_5_second(dt: datetime) -> str:
    return "/".join(
        [
            f"year={dt.year}",
            f"month={str(dt.month).zfill(2)}",
            f"day={str(dt.day).zfill(2)}",
            f"hour={str(dt.hour).zfill(2)}",
            f"minute={str(dt.minute).zfill(2)}",
            f"five_second={str(dt.second // 5).zfill(2)}",
        ]
    )


def get_pkey_by_15_second(dt: datetime) -> str:
    return "/".join(
        [
            f"year={str(dt.year).zfill(2)}",
            f"month={str(dt.month).zfill(2)}",
            f"day={str(dt.day).zfill(2)}",
            f"hour={str(dt.hour).zfill(2)}",
            f"minute={str(dt.minute).zfill(2)}",
            f"fifteen_second={str(dt.second // 15).zfill(2)}",
        ]
    )


def get_pkey_by_minute(dt: datetime) -> str:
    return "/".join(
        [
            f"year={dt.year}",
            f"month={str(dt.month).zfill(2)}",
            f"day={str(dt.day).zfill(2)}",
            f"hour={str(dt.hour).zfill(2)}",
            f"minute={str(dt.minute).zfill(2)}",
        ]
    )


def get_pkey_by_5_minute(dt: datetime) -> str:
    return "/".join(
        [
            f"year={dt.year}",
            f"month={str(dt.month).zfill(2)}",
            f"day={str(dt.day).zfill(2)}",
            f"hour={str(dt.hour).zfill(2)}",
            f"five_minute={str(dt.minute // 5).zfill(2)}",
        ]
    )


def get_pkey_by_10_minute(dt: datetime) -> str:
    return "/".join(
        [
            f"year={dt.year}",
            f"month={str(dt.month).zfill(2)}",
            f"day={str(dt.day).zfill(2)}",
            f"hour={str(dt.hour).zfill(2)}",
            f"ten_minute={str(dt.minute // 10)}",
        ]
    )


def get_pkey_by_15_minute(dt: datetime) -> str:
    return "/".join(
        [
            f"year={dt.year}",
            f"month={str(dt.month).zfill(2)}",
            f"day={str(dt.day).zfill(2)}",
            f"hour={str(dt.hour).zfill(2)}",
            f"quarter={dt.minute // 15}",
        ]
    )


def get_pkey_by_half_hour(dt: datetime) -> str:
    return "/".join(
        [
            f"year={dt.year}",
            f"month={str(dt.month).zfill(2)}",
            f"day={str(dt.day).zfill(2)}",
            f"hour={str(dt.hour).zfill(2)}",
            f"half_hour={dt.minute // 30}",
        ]
    )


def get_pkey_by_hour(dt: datetime) -> str:
    return "/".join(
        [
            f"year={dt.year}",
            f"month={str(dt.month).zfill(2)}",
            f"day={str(dt.day).zfill(2)}",
            f"hour={str(dt.hour).zfill(2)}",
        ]
    )


def get_pkey_by_2_hour(dt: datetime) -> str:
    return "/".join(
        [
            f"year={dt.year}",
            f"month={str(dt.month).zfill(2)}",
            f"day={str(dt.day).zfill(2)}",
            f"two_hour={str(dt.hour // 2).zfill(2)}",
        ]
    )


def get_pkey_by_4_hour(dt: datetime) -> str:
    return "/".join(
        [
            f"year={dt.year}",
            f"month={str(dt.month).zfill(2)}",
            f"day={str(dt.day).zfill(2)}",
            f"four_hour={dt.hour // 4}",
        ]
    )


def get_pkey_by_6_hour(dt: datetime) -> str:
    return "/".join(
        [
            f"year={dt.year}",
            f"month={str(dt.month).zfill(2)}",
            f"day={str(dt.day).zfill(2)}",
            f"six_hour={dt.hour // 6}",
        ]
    )


def get_pkey_by_half_day(dt: datetime) -> str:
    return "/".join(
        [
            f"year={dt.year}",
            f"month={str(dt.month).zfill(2)}",
            f"day={str(dt.day).zfill(2)}",
            f"half_day={dt.hour // 12}",
        ]
    )


def get_pkey_by_day(dt: datetime) -> str:
    return "/".join(
        [
            f"year={dt.year}",
            f"month={str(dt.month).zfill(2)}",
            f"day={str(dt.day).zfill(2)}",
        ]
    )
