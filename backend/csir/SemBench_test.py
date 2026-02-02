from .document import Document
from .pdf_extract import pdf_to_text,unstick_library_prefixes,clean_text
from .rule_validation import Rule_Validation
from . import libs

pdf = unstick_library_prefixes(pdf_to_text("SemBench.pdf"))
z = Rule_Validation(pdf)
#z.sentence_cleaner_by_dict("llms")
#query=input("Please input a query: \n")
#query = query.lower()
#print(query)
query = Document(input("Please input a query: \n")) #Make sure to strip question marks aswell
for sentence in query.text:
    for word in sentence:
        if word not in libs.DET and word not in libs.PREP and word not in libs.CONJ and word not in libs.COMP and word not in libs.MOD and word not in libs.AUX:
                print("Word: ",end="")
                print(word)
                print(z.context_finder(word))
                print()


#print(z.cleaned_sentences["llms"])


#print(z.subj_and_sentences["llms"])


#print(z.subj_and_sentences)
# print(z.shallow_search("benchmark", False))
# print(z.shallow_search("benchmark", True))

# print(z.shallow_search("semantics", False))
# print(z.shallow_search("semantics", True))

# print(z.shallow_search("evaluation", False))
# print(z.shallow_search("evaluation", True))

# print(z.shallow_search("retrieval", False))
# print(z.shallow_search("retrieval", True))

# print(z.shallow_search("embedding", False))
# print(z.shallow_search("embedding", True))
# "==========================================="
# print(z.shallow_search("context", False))
# print(z.shallow_search("tokenization", False))
# print(z.shallow_search("semantic", True))
# print(z.shallow_search("vector", False))
# print(z.shallow_search("representation", True))
# print(z.shallow_search("alignment", False))
# print(z.shallow_search("baseline", True))
# print(z.shallow_search("model", False))
# print(z.shallow_search("dataset", True))

# print(z.shallow_search("ontology", False))
# print(z.shallow_search("pipeline", False))
# print(z.shallow_search("parsing", True))
# print(z.shallow_search("inference", False))
# print(z.shallow_search("knowledge", True))

# print(z.shallow_search("astronomy", False))
# print(z.shallow_search("economics", False))
# print(z.shallow_search("biology", True))
# print(z.shallow_search("quantum", False))
# print(z.shallow_search("mythology", True))

# print(z.shallow_search("sembench", True))   # usually exact match needed
# print(z.shallow_search("semantic", True))   # strict = exact token? should be False
# print(z.shallow_search("semantic", False))  # loose should catch "semantics", "semantic-based"
# print(z.shallow_search("Lotus", False))  # loose should catch "semantics", "semantic-based"
# print(z.shallow_search("palimpzest", False))  # loose should catch "semantics", "semantic-based"
# print(z.shallow_search("thalamusdb", False))  # loose should catch "semantics", "semantic-based"
# print(z.shallow_search("comparison", False))  # loose should catch "semantics", "semantic-based"
# print(z.shallow_search("bigquery", False))  # loose should catch "semantics", "semantic-based"
# print(z.shallow_search("AI", False))  # loose should catch "semantics", "semantic-based"
# print(z.shallow_search("cocaine", True))


#This is currently case sensitive. It realies on strict equality
#maybe add some checking that checks with some margin of error, regardless of case?