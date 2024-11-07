from datetime import datetime

class Solution(object):
    info = dict()

    def get_weather(self, s):
        split_list = s.split()
        airport = split_list[1]
        self.info[airport] = {}

        time = split_list[2]
        self.info[airport]['written'] = time

        start_end = split_list[3].split("/")
        start = start_end[0]
        end = start_end[1]
        current_month = datetime.now().month
        current_year = datetime.now().year
        start_day = start[:2]
        start_hour = int(start[2:4])
        start_date = start_day + "-" + str(current_month) + "-" + str(current_year) + " " + str(start_hour)
        end_day = end[:2]
        end_hour = int(end[2:4])
        end_date = end_day + "-" + str(current_month) + "-" + str(current_year) + " " + str(end_hour)
        dt_object_start = datetime.strptime(start_date, "%d-%m-%Y %H")
        time_stamp_start = dt_object_start.timestamp()
        dt_object_end = datetime.strptime(end_date, "%d-%m-%Y %H")
        time_stamp_end = dt_object_end.timestamp()
        self.info[airport]['start date'] = time_stamp_start
        self.info[airport]['end date'] = time_stamp_end


        wind = split_list[4]
        wind_direction = wind[:3]
        wind_power = wind[3:5]
        self.info[airport]['wind direction'] = wind_direction
        self.info[airport]['wind power'] = int(wind_power)

        return self.info


if __name__ == '__main__':
    Ella = Solution()
    s = "TAF LLHZ 030503Z\n0306/0406 VRB03KT\n9999 SCT030\nTEMPO 0306/0307\n17010KT 5000 TSRA"
    print(Ella.get_weather(s))
    stamp = datetime.fromtimestamp(1730692800.0)
    print(stamp)
