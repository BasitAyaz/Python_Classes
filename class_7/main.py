# date function

# date = "26-08-2023"
# print(type(date))

# we cant use date methods in string


# importing date module which is builtin


#    sourse          module
# from datetime import datetime

#    sourse          modules
from datetime import datetime, date, time, timedelta

# current_date = date.today()
# print(current_date)

# current_date_time = datetime.now()
# print(current_date_time)


# print(current_date_time.year)
# print(current_date_time.day)
# print(current_date_time.month)
# print(current_date_time.hour)
# print(current_date_time.minute)
# print(current_date_time.second)
# print(current_date_time.time())
# print(current_date_time.date())


# setting specific date

# my_date = 1
# my_month = 1
# my_year = 2023

# d = date(year=my_year, month=my_month, day=my_date)
# # or
# dt = date(1997, 5, 18)


# we can use also as datetime like
# dt = datetime(1997, 5, 18, 12, 30, 45, 500)

# this is datetime class see all perameter in this class we can also as keyword argument like
# dt = datetime(year=2000, month=6, day=26)

# class datetime(
#     year: SupportsIndex,
#     month: SupportsIndex,
#     day: SupportsIndex,
#     hour: SupportsIndex = ...,
#     minute: SupportsIndex = ...,
#     second: SupportsIndex = ...,
#     microsecond: SupportsIndex = ...,
#     tzinfo: _TzInfo | None = ...,
#     *,
#     fold: int = ...
# )


# print(dt)
# print(d.year)


# date_iso = "2023-08-26"  # ISO 8601
# dt = "26-08-2023"  # not ISO Formate
# dt = "08-26-2023"  # not ISO Formate

# # dt_obj = date.fromisoformat(dt)  # it will give error because it it not ISO Formate
# dt_obj = date.fromisoformat(date_iso)

# print(dt_obj.year)


# datetime_str = "2023-08-01 10:54:00"
# dt_time_obj = datetime.fromisoformat(datetime_str)

# print(dt_time_obj)


# ts = 169302 # timestamp represent the seconds from 1 january 1970

# ts_date = datetime.fromtimestamp(ts)
# print(ts_date)


# what if date string is not in isoformate use this

# dt = "26-08-2023"  # not ISO Formate
# dt = "08-26-2023"  # not ISO Formate

# dts = datetime.strptime(dt, "%m-%d-%Y")
# print(dts)

# %m for month (small m for months)
# %d for date
# %Y for year (it should be capital)
# %H for hours
# %M for minutes (capital M for minutes)
# %S for seconds


# we only have to know what is the formate of date once you know this apply function of strptime() in the first peramter pass date string and second perameter pass the formate (formate : get your not ISO formated dated string and replace the value with above charts)

# dt = datetime.now()  # it will give ISO Formated
# x = str(dt)


# print(x)


# we can change specific date by replace() function

# dt = datetime.now()

# x = dt.replace(year=2000, month=1)

# print(x)

# but it is not aware from daylight saving.


# this liberary have to installed before using

# from dateutil import parser
# x = "2023/02/01"
# dt_obj = parser.parse(x)
# print(dt_obj.month)


# date manipulation using timedelta


# x = datetime.fromisoformat("2020-01-05")
# print(x)

# change_dt = x - timedelta(days=5) # it will - 5 days in actual date
# change_dt = x + timedelta(days=5) # it will + 5 days in actual date

# timedelta changes date and time according to calendar like e.g : "2020-02-05" and by timedelta we - 10 days in this date so output will be like "2020-01-25" it is only possible in timedelta, in replace method is not possible.

# timedelta arguments

# days: float = ...,
# seconds: float = ...,
# microseconds: float = ...,
# milliseconds: float = ...,
# minutes: float = ...,
# hours: float = ...,
# weeks: float = ...

# print(change_dt)

# current_dt = datetime.now()
# custom_dt = datetime.now()
# custom_dt = custom_dt.replace(day=5)

# diff = current_dt - custom_dt  # it will give deltatime
# print(diff)
# print(diff.days)
# print(diff.total_seconds())
# print(diff.seconds)

# import calendar

# month_r = calendar.monthrange(2023, 6)
# print(list(month_r))


# install module by this command "pip install pytz"
import pytz

# all_timeZones = pytz.all_timezones

# print(len(all_timeZones))
# print(pytz.timezone("Asia/Karachi"))

# tz_detail = pytz.timezone("US/Pacific")
# dt_str = "2020-03-07 15:00:00"
# dt_obj = datetime.fromisoformat(dt_str)

# tz_aware_dt = tz_detail.localize(dt_obj)
# print(tz_aware_dt)

# tz_detail = pytz.timezone("US/Pacific")
# dt_str = "2020-03-08 15:00:00"
# dt_obj = datetime.fromisoformat(dt_str)

# tz_aware_dt = tz_detail.localize(dt_obj)
# print(tz_aware_dt)
