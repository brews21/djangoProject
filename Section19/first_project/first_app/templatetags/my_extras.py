from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of "arg from the string"
    """
    return value.replace(arg,'')

# this can be done either like this or with the @register.... style
#register.filter('cut',cut)
