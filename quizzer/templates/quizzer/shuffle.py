import random
from django import template
register = template.Library()

@register.filter
def tag(arg):
    aux = list(arg)[:]
    random.shuffle(aux)
    return aux