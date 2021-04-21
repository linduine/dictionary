from django import template
register = template.Library()

@register.simple_tag
def define_clause_div_id(val=None):
  return f"#{val}"