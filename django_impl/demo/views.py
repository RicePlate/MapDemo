from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_protect

from .models import Maps, Marks
from django.contrib.auth.decorators import login_required
from forms import UserForm

from django.views.decorators.debug import sensitive_post_parameters

@sensitive_post_parameters("password")
@csrf_protect
def signup(request):
  if request.method == "POST":
    form = UserForm(request.POST)  # form = UserForm(request.POST)
    if form.is_valid():
      try:
        new_user = User.objects.create_user(**form.cleaned_data)
        # login(new_user, redirect_authenticated_user=True, redirect_field_name="/")
        # redirect, or however you want to get to the main view
        return HttpResponseRedirect('/demo/login')
      except Exception as e:
        print e
        form=UserForm()
  else:
    form = UserForm()
  return render(request, 'demo/signup.html', {'form': form})


class AddMap(LoginRequiredMixin, generic.DetailView):
  template_name = ''

# todo: could setup caching to prevent recalculating the model everytime...
class IndexView(LoginRequiredMixin, generic.ListView):
  template_name = 'demo/index.html'
  context_object_name = 'model'

  def get_queryset(self):
    model = {
      'maps': Maps.objects.filter(uid_id=self.request.user.id).order_by('-pub_date'),  # user's maps
      'current_map': None,                                                   # most recent map
      'current_marks': None,                                                 # marks for most recent map
    }
    model["current_map"] = model["maps"][0] if len(model["maps"]) > 0 else None  # grab the most recent map as the one to be viewed
    model["current_marks"] = Marks.objects.filter(mapid_id=model["current_map"].id) if model["current_map"] else None
    return model



# class DetailView(LoginRequiredMixin, generic.DetailView):
#   model = Question
#   template_name = 'demo/details.html'
#
# class ResultsView(LoginRequiredMixin, generic.DetailView):
#   model = Question
#   template_name = 'demo/results.html'
#
# @login_required
# def vote(request, question_id):
#   question = get_object_or_404(Question, pk=question_id)
#   try:
#     selected_choice = question.choice_set.get(pk=request.POST['choice'])
#   except (KeyError, Choice.DoesNotExist):
#     # Redisplay the question voting form.
#     return render(request, 'demo/details.html', {
#       'question': question,
#       'error_message': "You didn't select a choice.",
#     })
#   else:
#     selected_choice.votes += 1
#     selected_choice.save()
#     # Always return an HttpResponseRedirect after successfully dealing
#     # with POST data. This prevents data from being posted twice if a
#     # user hits the Back button.
#     return HttpResponseRedirect(reverse('demo:results', args=(question.id,)))