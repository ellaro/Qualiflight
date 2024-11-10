from datetime import datetime


class Solution(object):
    info = dict()

    def get_weather(self, string):
        split_list = string.split()
        airport = split_list[1]
        self.info[airport] = {}

        self.extract_written_time(split_list, airport)

        self.extract_dates(split_list, airport)

        self.extract_wind_info(split_list, airport)

        return self.info

    def extract_written_time(self, split_list, airport):
        time = split_list[2]
        self.info[airport]['written'] = time

    def extract_wind_info(self, split_list, airport):
        wind = split_list[4]
        wind_direction = wind[:3]
        wind_power = wind[3:5]
        self.info[airport]['wind direction'] = wind_direction
        self.info[airport]['wind power'] = int(wind_power)

    def extract_dates(self, split_list, airport):
        start_end = split_list[3].split("/")
        start = start_end[0]
        end = start_end[1]
        time_stamp_start = self.convert_to_timestamp(start)
        time_stamp_end = self.convert_to_timestamp(end)
        self.info[airport]['start date'] = time_stamp_start
        self.info[airport]['end date'] = time_stamp_end

    @staticmethod
    def convert_to_timestamp(time):
        current_month = datetime.now().month
        current_year = datetime.now().year
        day = time[:2]
        hour = int(time[2:4])
        date = day + "-" + str(current_month) + "-" + str(current_year) + " " + str(hour)
        dt_object = datetime.strptime(date, "%d-%m-%Y %H")
        time_stamp = dt_object.timestamp()
        return time_stamp




if __name__ == '__main__':
    Ella = Solution()
    s = "TAF LLHZ 030503Z\n0306/0406 VRB03KT\n9999 SCT030\nTEMPO 0306/0307\n17010KT 5000 TSRA"
    print(Ella.get_weather(s))
