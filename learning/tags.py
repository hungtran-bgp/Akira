from django import template

register = template.Library()

@register.simple_tag
def update_variable(value, variable_name, context):
  context[variable_name] = value
  return value
