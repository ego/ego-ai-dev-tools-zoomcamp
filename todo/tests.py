from django.test import TestCase
from django.urls import reverse
from .models import Todo


class TodoModelTest(TestCase):
    def test_create_todo(self):
        todo = Todo.objects.create(title="Test Todo")
        self.assertEqual(todo.title, "Test Todo")
        self.assertFalse(todo.completed)


class TodoViewTest(TestCase):
    def test_index_view_with_no_todos(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No todos yet.")

    def test_index_view_with_todos(self):
        Todo.objects.create(title="First Todo")
        Todo.objects.create(title="Second Todo")
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "First Todo")
        self.assertContains(response, "Second Todo")

    def test_add_todo(self):
        response = self.client.post(reverse('add_todo'), {'title': 'New Todo'})
        # Redirect after successful POST
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Todo.objects.filter(title='New Todo').exists())

    def test_delete_todo(self):
        todo = Todo.objects.create(title="Todo to delete")
        response = self.client.get(reverse('delete_todo', args=[todo.id]))
        # Redirect after successful GET
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Todo.objects.filter(title='Todo to delete').exists())

    def test_add_todo_empty_title(self):
        response = self.client.post(reverse('add_todo'), {'title': ''})
        # Redirect after POST (even with empty title)
        self.assertEqual(response.status_code, 302)
        # Empty title should still create a todo (no validation in this simple implementation)
        # But we can check that it doesn't crash
        self.assertTrue(Todo.objects.exists())
