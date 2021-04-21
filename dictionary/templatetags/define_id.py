from django import template
register = template.Library()

@register.simple_tag
def define_id(val=None):
  return val