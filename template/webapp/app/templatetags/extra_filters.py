from django.template.defaulttags import register


@register.filter
def get_item(d, k):
    # provides dictionary-like functionality
    return d.get(k)
