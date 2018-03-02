import re

from django import forms 

from .models import Post, BlockedPost

from generic.models import BadWordList

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ("title", "post")

	def clean_title(self):
		title = self.cleaned_data.get("title", "")
		if title:
			blocked_words = BadWordList.objects.filter(
										active=True
								).values_list("word", flat=True)
			# words_in_title = title.split(" ")
			found = False
			found_list = ""
			for item in blocked_words:
				# if title.find(item) != -1:
				if re.search(
						item, 
						title, 
						re.IGNORECASE
					):

					found = True
					found_list += "%s " %(item)
			if found:
				self.add_error(
						"title", 
						"Blocked words (%s) found in your title" %(found_list)
					)
		return title

	def clean_post(self):
		post = self.cleaned_data.get("post", "")
		if post:
			blocked_words = BadWordList.objects.filter(
										active=True
								).values_list("word", flat=True)
	
			found = False
			found_list = ""
			for item in blocked_words:
				# if title.find(item) != -1:
				if re.search(
						item, 
						post, 
						re.IGNORECASE
					):
				
					found = True
					found_list += "%s " %(item)
			if found:
				self.add_error(
						"post", 
						"Blocked words (%s) found in your post" %(found_list)
					)
		return post


class BlockForm(forms.Form):

	post_id = forms.IntegerField()
	words = forms.CharField(required=False)



