import re

from django import forms 

from .models import Post, BlockedPost

from generic.models import BadWordList

import nltk
sno = nltk.stem.SnowballStemmer('english')
lemma = nltk.wordnet.WordNetLemmatizer()
from flashtext import KeywordProcessor
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')
# import hunspell
# hobj = hunspell.HunSpell('/usr/share/myspell/en_US.dic', '/usr/share/myspell/en_US.aff')

# hobj.stem('linked')
# lemma.lemmatize('leaves')


class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ("title", "post")

	def clean_title(self):
		title = self.cleaned_data.get("title", "")
		the_title = title
		keyword_processor = KeywordProcessor()
		if title:
			blocked_words = BadWordList.objects.filter(
										active=True
								)
			bad_word_list = []
			stemmed_words = []
			for word in blocked_words:
				if not word.word in bad_word_list:
					bad_word_list.append(word.word)
			tokenized_words = tokenizer.tokenize(title)

			for word in tokenized_words:
				word = word.lower()
				if word not in stemmed_words:
					word = sno.stem(word)
					stemmed_words.append(word)
			count=0
			while count < len(tokenized_words):
				word = tokenized_words[count]
				word = word.lower()
				word = lemma.lemmatize(word)
				count += 1

				if word not in stemmed_words:
					stemmed_words.append(word)

			
			tokenized_list = list(set(tokenized_words))

			word_list = tokenized_list + stemmed_words
			word_list = list(set(word_list))

			title = " ".join(word_list)


			for word in bad_word_list:
				keyword_processor.add_keyword(word)

			keywords_found = keyword_processor.extract_keywords(title)

			found = False
			found_list = ""
			re_found_list = []

			for item in bad_word_list:
				if re.search(
						item, 
						title, 
						re.IGNORECASE
					):

					found_word = item.lower() 
					re_found_list.append(found_word)
					found = True
					found_list += "%s " %(item)

			if found or len(keywords_found) > 0:
				bad_word_found_list = []
				word_found_list = re_found_list + keywords_found
				for word in word_found_list:
					if not word in bad_word_found_list:
						bad_word_found_list.append(word)


				found_list = ",".join(bad_word_found_list)
				self.add_error(
						"title", 
						"Blocked words (%s) found in your title" %(found_list)
					)
		return the_title

	def clean_post(self):
		title = self.cleaned_data.get("post", "")
		the_title = title
		keyword_processor = KeywordProcessor()
		if title:
			blocked_words = BadWordList.objects.filter(
										active=True
								)
			bad_word_list = []
			stemmed_words = []
			for word in blocked_words:
				if not word.word in bad_word_list:
					bad_word_list.append(word.word)
			tokenized_words = nltk.word_tokenize(title)

			for word in tokenized_words:
				word = word.lower()
				if word not in stemmed_words:
					word = sno.stem(word)
					stemmed_words.append(word)
			count=0
			while count < len(tokenized_words):
				word = tokenized_words[count]
				word = word.lower()
				word = lemma.lemmatize(word)
				count += 1

				if word not in stemmed_words:
					stemmed_words.append(word)

			
			tokenized_list = list(set(tokenized_words))

			word_list = tokenized_list + stemmed_words
			word_list = list(set(word_list))

			title = " ".join(word_list)


			for word in bad_word_list:
				keyword_processor.add_keyword(word)

			keywords_found = keyword_processor.extract_keywords(title)

			found = False
			found_list = ""
			re_found_list = []

			for item in bad_word_list:
				if re.search(
						item, 
						title, 
						re.IGNORECASE
					):

					found_word = item.lower() 
					re_found_list.append(found_word)
					found = True
					found_list += "%s " %(item)
			if found or len(keywords_found) > 0:
				bad_word_found_list = []
				word_found_list = re_found_list + keywords_found
				for word in word_found_list:
					if not word in bad_word_found_list:
						bad_word_found_list.append(word)


				found_list = ",".join(bad_word_found_list)
				self.add_error(
						"post", 
						"Blocked words (%s) found in your post" %(found_list)
					)
		return the_title


class BlockForm(forms.Form):

	post_id = forms.IntegerField()
	words = forms.CharField(required=False)
	is_user_blocked = forms.BooleanField(initial=False, required=False)
	is_post_blocked = forms.BooleanField(initial=False, required=False)



