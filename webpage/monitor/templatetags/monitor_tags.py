from django import template

register = template.Library()

@register.filter()
def time_of_day(dt):
    """Return the time of day as a float"""
    return dt.hour + dt.minute / 60. + dt.second / 2400.

@register.filter()
def is_active(path, name):
    """Return an active tag for the menu item if we're on that page"""
    condition = name in path and name != '' or (name == '' and path == '/')
    return 'class="active"' if condition else ''
