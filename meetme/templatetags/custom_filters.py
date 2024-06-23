from django import template

register = template.Library()

@register.filter
def weekday_filter(s, index):
    if isinstance(s, list) and 0 <= index < len(s):
        return s[index]
    return None