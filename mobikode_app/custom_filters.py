# custom_filters.py

from django import template
import re

register = template.Library()

@register.filter
def separate_pascal_case(value):
    return re.sub(r'(?<=.)([A-Z])', r' \1', value).strip()



