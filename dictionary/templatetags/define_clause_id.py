from django import template
register = template.Library()

@register.simple_tag
def define_clause_id(val=None):
  return f"lemma_{val}"