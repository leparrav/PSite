from blog.models import Comment
from django import forms
import bleach
import datetime


class  CommentForm(forms.ModelForm):
	author = forms.CharField(help_text="Username", max_length=36)
	text = forms.CharField(widget=forms.Textarea, help_text="Comment", max_length=512)
	date = forms.DateField(widget=forms.HiddenInput(), initial= datetime.datetime.now())
	class Meta:
		model = Comment
		fields = ('author','text','date')

	# I'm not sure if django escapes evil scripts to avoid xss (bleach would be better)
	def clean(self):
		cleaned_data = self.cleaned_data
		text = bleach.clean(cleaned_data.get('text'))
		cleaned_data['text'] = text
		return cleaned_data