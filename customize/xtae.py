from exchange_calendars.exchange_calendar_xtae import (
    XTAEExchangeCalendar as XTAEExchangeCalendarUpstream,
)
from exchange_calendars.exchange_calendar import SUNDAY, HolidayCalendar
from pandas.tseries.holiday import Holiday


class XTAEExchangeCalendar(XTAEExchangeCalendarUpstream):
    @property
    def special_closes(self):
        def convert_rule(rule: Holiday):
            return Holiday(
                rule.name,
                month=rule.month,
                day=rule.day,
                offset=rule.offset,
                days_of_week=tuple(x for x in rule.days_of_week if x != SUNDAY),
            )

        # Get upstream calendar, but remove any periodic entries for Sunday.
        return [
            (x[0], HolidayCalendar([convert_rule(y) for y in x[1].rules]))
            for x in super(XTAEExchangeCalendar, self).special_closes
            if not isinstance(x[1], int) or x[1] != SUNDAY
        ]

    @property
    def weekmask(self):
        # Exclude Sunday.
        return "1111000"
