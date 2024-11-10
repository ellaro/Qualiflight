from datetime import datetime
from consts import AIRPORT_LENGTH, WIND_SUFFIX, WRITTEN_SUFFIX, DATE_DURATION_LENGTH


class Solution(object):
    info = dict()

    def get_weather(self, string) -> dict:
        split_list = string.split()

        if split_list[0] != 'TAF':
            print('not a TAF document')
            return {}

        airport = split_list[1]
        if len(airport) != AIRPORT_LENGTH:
            print(f'airport is not in length of 4, but length of {len(airport)}')
            return {}

        self.info[airport] = {}
        self.extract_written_time(split_list[2], airport)
        self.extract_dates(split_list[3], airport)
        self.extract_wind_info(split_list[4], airport)

        return self.info

    def extract_written_time(self, word, airport):
        if word[-1] != WRITTEN_SUFFIX or not word[:-1].isdigit():
            print(f'word is not a written time: {word}')
            return

        self.info[airport]['written'] = self.convert_to_timestamp_by_day_hour_minute(word)

    def extract_wind_info(self, word, airport):
        if word[-2:] != WIND_SUFFIX:
            print(f'did not found wind format: {word}')
            return

        wind_direction = word[:3]
        wind_power = word[3:5]
        self.info[airport]['wind direction'] = int(wind_direction) if wind_direction.isdigit() else wind_direction
        self.info[airport]['wind power'] = int(wind_power)

    def extract_dates(self, word, airport):
        if '/' not in word:
            print(f'did not found backslash in word: {word}')
            return

        dates = word.split("/")
        if len(dates) != 2 or len(dates[0]) != DATE_DURATION_LENGTH or len(dates[1]) != DATE_DURATION_LENGTH:
            print(f'did not found dates: {word}')
            return

        start = dates[0]
        end = dates[1]
        time_stamp_start = self.convert_to_timestamp_by_day_hour(start)
        time_stamp_end = self.convert_to_timestamp_by_day_hour(end)
        self.info[airport]['start date'] = time_stamp_start
        self.info[airport]['end date'] = time_stamp_end

    @staticmethod
    def convert_to_timestamp_by_day_hour(time):
        day = str(int(time[:2]))
        hour = str(int(time[2:]))
        date = day + "-" + str(datetime.now().month) + "-" + str(datetime.now().year) + " " + hour
        dt_object = datetime.strptime(date, "%d-%m-%Y %H")
        return dt_object.timestamp()

    @staticmethod
    def convert_to_timestamp_by_day_hour_minute(time):
        day = str(int(time[:2]))
        hour = str(int(time[2:4]))
        minute = str(int(time[4:6]))
        date = day + "-" + str(datetime.now().month) + "-" + str(datetime.now().year) + " " + hour + "-" + minute
        dt_object = datetime.strptime(date, "%d-%m-%Y %H-%M")
        return dt_object.timestamp()


if __name__ == '__main__':
    Ella = Solution()
    s = "TAF LLHZ 030503Z\n0306/0406 VRB03KT\n9999 SCT030\nTEMPO 0306/0307\n17010KT 5000 TSRA"
    print(Ella.get_weather(s))
