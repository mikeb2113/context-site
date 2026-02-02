from enum import Enum
from .document import Document
from . import libs
import json
import copy
#NOTE: For input "The  quick brown fox jumped over the lazy dog. Then the dog howled
#The NP "Then" is missing! :ikely an issue with NP_absorb? Look into this later!
class Types(Enum):
    DET = 1
    PREP = 2
    CONJ = 3
    COMP = 4
    MOD = 5
    AUX = 6

    NP = 7
    PP = 8

class Skeletons:
    #maybe refactor skeletons into document? This is a problem for later - it's not important
    json_output = "skeleton_list.json"
    skeleton_list = "skeleton_list_filtered.json"
    sentence_shape = []
    abstracted_shape = []
    COMP_count = 0
    sentences = []

    filtered_array = [] #This is what stores the candidate subject strings!
    cleaned_array = [] #This stores text contents with an identical line count to filtered array, but without the delimiters!

    DELIMITER_LIST={
        "[DET]:",
        "[PREP]:",
        "[CONJ]:",
        "[COMP]:",
        "[MOD]:",
        "[AUX]:"
    }

    def is_np_only(self,entry):
        # Must be a list of two items: ["[NP]:", something]
        if not (isinstance(entry, list) and len(entry) == 2):
            return False
        return entry[0] == "[NP]:"
    
    def output_handler(self):
            with open(self.json_output, "w") as outfile:
                outfile.write("[\n")
                for i, sentence in enumerate(self.sentences):
                    json.dump(sentence, outfile)
                    if i < len(self.sentences) - 1:
                        outfile.write(",\n")
                    else:
                        outfile.write("\n")
                outfile.write("]\n")

            return self.sentences
    
    def filtered_copy(self,original):
            #Break it down two levels
            #When you have individual words: remove the evens for the array copy
            filtered = copy.deepcopy(original)
            filtered_array = []
            filtered = [entry for entry in filtered if not self.is_np_only(entry)]
            with open(self.skeleton_list, "w") as outfile:
                outfile.write("[\n")
                for i, entry in enumerate(filtered):
                    temp = []
                    for i2, word in enumerate(entry):
                        if i2%2==1:
                            temp.append(word)
                    self.cleaned_array.append(temp)
                    filtered_array.append(entry)
                    outfile.write("  ")
                    json.dump(entry, outfile)
                    if i < len(filtered) - 1:
                        outfile.write(",\n")
                    else:
                        outfile.write("\n")
                outfile.write("]\n")
            return filtered_array

                
    def __init__(self,text):
        self.document = Document(text)
        for sentence in self.document.NPLIST:
             append = True
             temp = []
             NP_absorb = False
             for phrase in sentence:
                if isinstance(phrase,list):
                         if not NP_absorb:
                            appendThis="[NP]:"
                            temp.append(appendThis)
                            temp.append(phrase)
                         NP_absorb = True
                else:
                    NP_absorb = False
                    if phrase in libs.COMP:
                        appendThis="[COMP]:"
                        temp.append(appendThis)
                        temp.append(phrase)
                        self.COMP_count = self.COMP_count+1
                    elif phrase in libs.MOD:
                        appendThis="[MOD]:"
                        temp.append(appendThis)
                        temp.append(phrase)
                    elif phrase in libs.AUX:
                        appendThis="[AUX]:"
                        temp.append(appendThis)
                        temp.append(phrase)
                    elif phrase in libs.CONJ:
                        appendThis="[CONJ]:"
                        temp.append(appendThis)
                        temp.append(phrase)
                    elif phrase in libs.PREP:
                        appendThis="[PREP]:"
                        temp.append(appendThis)
                        temp.append(phrase)
                    elif phrase in libs.DET:
                        appendThis="[DET]:"
                        temp.append(appendThis)
                        temp.append(phrase)
                if(append):
                    self.sentences.append(temp)
                    append = False
        generateSkeletonList = self.output_handler()
        self.filtered_array = self.filtered_copy(generateSkeletonList)