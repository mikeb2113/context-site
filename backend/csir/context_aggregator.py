from .document import Document
from .pdf_extract import pdf_to_text,unstick_library_prefixes,clean_text
from .rule_validation import Rule_Validation
from . import libs
import os
from dotenv import load_dotenv
class ContextAggregator:        
    isEmpty = True
    context = {}
    text = ""
    def run(self,query,document):
        load_dotenv()
        pdf = unstick_library_prefixes(pdf_to_text(document))
        z = Rule_Validation(pdf)

        query_dict = {}
        context = []
        query = Document(query)
        for sentence in query.text:
            for word in sentence:
                if word not in libs.DET and word not in libs.PREP and word not in libs.CONJ and word not in libs.COMP and word not in libs.MOD and word not in libs.AUX and word not in libs.EXISTENTIAL_DET and word not in libs.NEGATIVE_QUANT and word not in libs.UNIVERSAL_DET and z.context_finder(word)!="":
                    self.empty=False
                    query_dict[word]=z.context_finder(word)
        self.context = query_dict

        self.text = pdf
        return query_dict
    def __init__(self,query,document):
        self.run(query,document)
    def pdf_to_text(path_to_pdf):
        return pdf_to_text(path_to_pdf)