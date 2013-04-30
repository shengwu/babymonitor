from django import template

register = template.Library()

@register.filter()
def time_of_day(dt):
    """Return the time of day as a float"""
    return dt.hour + dt.minute / 60. + dt.second / 2400.
