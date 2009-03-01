from django import template
from quotes.models import Quote

register = template.Library()

@register.inclusion_tag('quotes/random_quote.html')
def show_random_quote():
    """
    For generating a single random quote
    """
    try:
         random_quote = Quote.objects.order_by('?')[0]
    except ValueError:
        print "There are no quotes"