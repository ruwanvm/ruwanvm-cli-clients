from datetime import datetime
import pytz

default_timezone = 'UTC'
default_time_format = '%Y/%m/%d %H:%M:%S'


class Timestamp:
    """Client to get current unix timestamp"""

    @staticmethod
    def current_timestamp(timezone: str = default_timezone):
        """
        :param timezone: Timezone string (default is 'UTC')
        :return: Unix timestamp for the specified timezone
        """
        tz = pytz.timezone(timezone)
        current_datetime = datetime.now(tz)
        return int(current_datetime.timestamp())

    @staticmethod
    def datetime_to_timestamp(
            datetime_string: str,
            time_format: str = default_time_format,
            timezone=default_timezone
    ):
        """
        :param datetime_string: Date-time string in the format `time_format`
        :param time_format: Datetime format. (Default is '%Y/%m/%d %H:%M:%S')
        :param timezone: Timezone string (default is UTC)
        :return: Corresponding Unix timestamp
        """
        tz = pytz.timezone(timezone)
        datetime_row = datetime.strptime(datetime_string, time_format)
        datetime_localized = tz.localize(datetime_row)
        return int(datetime_localized.timestamp())

    @staticmethod
    def timestamp_to_datetime(
            timestamp: int,
            time_format: str = default_time_format,
            timezone=default_timezone
    ):
        """
        :param timestamp: Unix timestamp to convert
        :param time_format: Datetime format. (Default is '%Y/%m/%d %H:%M:%S')
        :param timezone: Timezone string (default is UTC)
        :return: Human-readable date-time string
        """
        tz = pytz.timezone(timezone)
        datetime_row = datetime.fromtimestamp(timestamp, tz)
        return datetime_row.strftime(time_format)
