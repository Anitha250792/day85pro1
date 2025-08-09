from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Note

class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes/note_list.html'
    context_object_name = 'notes'
    paginate_by = 10

    def get_queryset(self):
        # Superuser sees all notes; regular users see only their own
        user = self.request.user
        if user.is_superuser:
            return Note.objects.all().order_by('-updated_at')
        return Note.objects.filter(owner=user).order_by('-updated_at')

class NoteDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Note
    template_name = 'notes/note_detail.html'
    context_object_name = 'note'
    raise_exception = True

    def test_func(self):
        note = self.get_object()
        return self.request.user.is_superuser or note.owner == self.request.user

class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    template_name = 'notes/note_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class NoteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Note
    template_name = 'notes/note_form.html'
    fields = ['title', 'content']
    raise_exception = True

    def test_func(self):
        note = self.get_object()
        return self.request.user.is_superuser or note.owner == self.request.user

class NoteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Note
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('notes:list')
    raise_exception = True

    def test_func(self):
        note = self.get_object()
        return self.request.user.is_superuser or note.owner == self.request.user
