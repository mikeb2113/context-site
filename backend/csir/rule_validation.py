from .skeletons import Skeletons
from . import libs
class Rule_Validation:
    candidate_subjects = []
    phrases = []
    subj_and_sentences = {}

    cleaned_sentences = []
    def __init__(self,text):
        self.skeleton = Skeletons(text)
        self.shallow_subject_dict = []
        self.subject_identification()
        #for key in self.shallow_subject_dict:
            #self.sentence_cleaner_by_dict(key)

    def shallow_search(self,word,strict):
        word=str.lower(word)
        print(word,end="")
        print(": ",end="")
        if strict:
            if word in self.shallow_subject_dict:
                return True
            else:
                return False
        else:
            if word in self.shallow_subject_dict or word[:-1] in self.shallow_subject_dict or word[:-2] in self.shallow_subject_dict or word+"s" in self.shallow_subject_dict or word+"ing" in self.shallow_subject_dict or word+"ed" in self.shallow_subject_dict:
                return True
            else:
                return False
            
    def delistify(self,input):
        phrase=input
        de_listed = []
        if isinstance(phrase,str):
                    de_listed.append(phrase)
        else:
            for i in phrase:
                if isinstance(i,str):
                    de_listed.append(i)
                else:
                    for i2 in i:
                        if isinstance(i2,str):
                            de_listed.append(i2)
        return de_listed

    def context_finder(self,word):
        cleaned = ""
        if word in self.subj_and_sentences:
            for phrase in self.subj_and_sentences[word]:
                cleaned_phrase = self.delistify(phrase)
                #self.cleaned_sentences.append(cleaned_phrase)
                #cleaned.append(cleaned_phrase)
                for word in cleaned_phrase:
                    cleaned += word + " "
                cleaned = cleaned[:-1]
                cleaned += ". "
        # else:
        #     print("error: keyword not found")
        return(cleaned)
        
    def subject_identification(self):
        print_toggle = False
        previous_phrase = ""
        for index,sentence_structures in enumerate(self.skeleton.filtered_array):
            #consider this: What if you loop through the sentence until you find a NP? The first NP should hypothetically contain the subject
            for phrase in sentence_structures:
                self.phrases.append(phrase)
                if isinstance(phrase,str) and phrase in libs.DET:
                    previous_phrase = phrase
                if phrase == "[NP]:":
                    print_toggle = True
                    continue
                if print_toggle:
                    if previous_phrase != "":
                        previous_phrase = ""
                    if isinstance(phrase,list):
                        for i in phrase:
                            self.shallow_subject_dict.append(i)
                            if i not in self.subj_and_sentences:
                                self.subj_and_sentences[i]=[self.skeleton.cleaned_array[index]]
                            else:
                                temp = self.subj_and_sentences[i]
                                temp.append(self.skeleton.cleaned_array[index])
                                self.subj_and_sentences[i]=temp  

                else:
                    self.shallow_subject_dict.append(phrase)
                print_toggle = False
                break