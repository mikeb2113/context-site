from .pdf_extract import pdf_to_text,unstick_library_prefixes
from .rule_validation import Rule_Validation

pdf = unstick_library_prefixes(pdf_to_text("TheKingInYellow.pdf"))
z = Rule_Validation(pdf)

# print(z.shallow_search("madness", False))
# print(z.shallow_search("Hauser", False))
z.print_where_found("yellow")



#This is currently case sensitive. It realies on strict equality
#maybe add some checking that checks with some margin of error, regardless of case?