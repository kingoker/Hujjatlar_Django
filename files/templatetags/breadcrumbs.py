from django import template
from django.urls import reverse
from django.utils.safestring import mark_safe


register = template.Library()


@register.simple_tag(takes_context=True)
def breadcrumbs(context):
    if 'directory' in context:
        directory = context['directory']
    elif 'topic' in context:
        directory = context['topic'].section
    else:
        directory = None

    index_url = reverse('files:files-list')
    sections = []
    while directory != None:
        sections.append(
            f'/ <a class="bread " href="{directory.get_absolute_url()}">{directory.title}</a> '
        )
        directory = directory.directories
    sections.append(f'<a class="bread " href="{index_url}">Главная</a> ')
    sections.reverse()
    return mark_safe("".join(sections))
