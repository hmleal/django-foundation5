from django import template
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter
def render_form(form):
    s = force_unicode(form.non_field_errors())
    for field in form.hidden_fields():
        s += force_unicode(field)

    for field in form.visible_fields():
        s += render_field(field)
    return mark_safe(s)


@register.filter
def render_field(field):
    slug = field.field.widget.__class__.__name__.lower()
    templates = [
        'foundation/{0}.html'.format(slug),
        'foundation/field.html'
    ]
    return template.loader.render_to_string(
        templates, {'field': field, 'slug': slug})
