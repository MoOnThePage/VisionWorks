from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from . models import Todo

# Create your views here.
def index(request):
    """Main page - shows all todos"""
    todos = Todo.objects.all().order_by('-created_at')
    return render(request, 'todo/index.html', {'todos': todos})


@require_http_methods(["POST"])
def create_todo(request):
    """HTMX endpoint to create a new todo"""
    title = request.POST.get('title', '').strip()

    if title:
        todo = Todo.objects.create(title=title)
        # Return just the new todo item HTML
        return render(request, 'todo/partials/todo_item.html', {'todo': todo})

    # Return empty response if no title
    return HttpResponse()


@require_http_methods(["POST"])
def toggle_todo(request, todo_id):
    """HTMX endpoint to toggle todo completion"""
    todo = get_object_or_404(Todo, id=todo_id)
    todo.completed = not todo.completed
    todo.save()

    # Return updated todo item HTML
    return render(request, 'todo/partials/todo_item.html', {'todo': todo})


@require_http_methods(["DELETE"])
def delete_todo(request, todo_id):
    """HTMX endpoint to delete a todo"""
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()

    # Return empty response (removes the element)
    return HttpResponse()


# Optional: View to return updated list (for sync after changes)
def todo_list(request):
    """HTMX endpoint to get updated todo list"""
    todos = Todo.objects.all().order_by('-created_at')
    return render(request, 'todo/partials/todo_list.html', {'todos': todos})