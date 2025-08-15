from . import jalali

def jalaliConvertor(time):
    jmonth = [
        "فروردین",
        "اردیبهشت",
        "خرداد",
        "تیر",
        "مرداد",
        "شهریور",
        "مهر",
        "آبان",
        "آذر",
        "دی",
        "بهمن",
        "اسفند",
    ]

    time_to_str = "{},{},{}".format(time.year, time.month, time.day)
    time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()
    time_to_list = list(time_to_tuple)

    for index,month in enumerate(jmonth):
        if time_to_list[1] == index+1:
            time_to_list[1] = month
            break

    output = "{} {} {}".format(
        time_to_list[2],
        time_to_list[1],
        time_to_list[0],)
    return output



####################################class Gregorian:
class Gregorian:
    def __init__(self, *date):
        import datetime

        # اگر فقط یک آرگومان داده شده
        if len(date) == 1:
            date = date[0]
            if isinstance(date, datetime.datetime) or isinstance(date, datetime.date):
                self.gregorian_year = date.year
                self.gregorian_month = date.month
                self.gregorian_day = date.day
            elif isinstance(date, str):
                y, m, d = map(int, date.split('-'))
                self.gregorian_year, self.gregorian_month, self.gregorian_day = y, m, d
            elif isinstance(date, tuple):
                self.gregorian_year, self.gregorian_month, self.gregorian_day = date
            else:
                raise Exception("Invalid Input Type")
        elif len(date) == 3:
            self.gregorian_year, self.gregorian_month, self.gregorian_day = date
        else:
            raise Exception("Invalid Input")

        # --- اینجا تبدیل به جلالی را انجام بده ---
        self.persian_year = self.gregorian_year - 621  # نمونه ساده
        self.persian_month = self.gregorian_month
        self.persian_day = self.gregorian_day

    def persian_tuple(self):
        return self.persian_year, self.persian_month, self.persian_day

def jalaliConvertor(datetime_obj):
    g = Gregorian(datetime_obj)
    jy, jm, jd = g.persian_tuple()
    return f"{jy:04d}/{jm:02d}/{jd:02d}"
