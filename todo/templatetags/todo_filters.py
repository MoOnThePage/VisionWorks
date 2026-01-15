from django import template
from todo.models import Todo

register = template.Library()

@register.filter
def filtercompleted(queryset, completed):
    """Filter a queryset by completion status"""
    if hasattr(queryset, 'filter'):
        return queryset.filter(completed=completed)
    # If it's not a queryset (like a list), filter manually
    return [item for item in queryset if item.completed == completed]

# Alternative simpler filter that just counts completed
@register.filter
def completed_count(queryset):
    """Count completed todos in a queryset"""
    if hasattr(queryset, 'filter'):
        return queryset.filter(completed=True).count()
    return sum(1 for item in queryset if item.completed)