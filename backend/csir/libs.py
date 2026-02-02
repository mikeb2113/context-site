DET = {"the", "a", "an", "this", "that", "these", "those",}

PREP = {"of", "in", "on", "at", "over", "under", "with", "by", "for", "to", "from", "into", "onto"}

CONJ = {"and", "or", "but"}

COMP = {"that", "which", "who", "whom"}

MOD = {"can", "could", "will", "would", "shall", "should", "may", "might", "must"}

AUX = {"be", "am", "is", "are", "was", "were", "been", "being",
        "have", "has", "had",
        "do", "does", "did"}

#Montague Operand Identifiers:
EXISTENTIAL_DET = {
    "a", "an",
    "some",
    "one",          # as in "one student" (often ∃)
    "somebody", "someone", "something", "somewhere",
    "certain"     # multiword, but you can detect "a" + "certain"
}

UNIVERSAL_DET = {
    "every", "each",
    "all", 
    "any",       # context-sensitive; treated as universal in generic contexts
    "whoever", "whatever", "whichever", "what"  # “free-choice” style universals
}

NEGATIVE_QUANT = {
    "no",
    "nobody", "noone", "no-one", "none",
    "nothing",
    "not",
    "nowhere",
    "never"  # temporal but still a negative quantificational flavor
}

OPEN = {}

THE_WHITELIST = {
    "theorem", "theoretical", "theatre", "theater", "therapy",
    "therapist", "thermal", "thermodynamics", "theme", "thematic",
    "thesis", "theology", "theologian", "therefore", "thereby",
    "therein", "thereof", "thereon", "therewith", "thereafter",
    "thence", "thenceforth", "theft", "their", "theirs", "them",
    "themselves", "then", "there", "thereupon","they"
    # add more as you encounter them
}

WITH_WHITELIST = {
    "without", "within", "withstand",
}

OVER_WHITELIST = {
    "overall", "overlap", "overload", "overflow", "overhead",
    "overnight", "overseas", "oversee", "overcome", "overgrown",
    "overly", "overuse", "overestimate", "overwhelm",
}

UNDER_WHITELIST = {
    "undergo", "undergrad", "undergraduate", "underground",
    "understand", "understood", "undertake", "undertaker",
    "underline", "underlying", "underworld", "underestimate",
}

IN_WHITELIST = {
    "in", "inability", "inaccessible", "inaccurate", "inactive",
    "inadequate", "inadmissible", "inadvertent", "inadvisable",
    "inalienable", "inanimate", "inappropriate", "inaugural",
    "inbound", "inbred", "incentive", "incest", "inch", "incident",
    "incidental", "incidence", "incidentally", "incline",
    "inclined", "include", "included", "including", "inclusion",
    "inclusive", "incoherent", "income", "incoming", "incompatible",
    "incomplete", "inconclusive", "incongruent", "incongruous",
    "inconsistent", "inconvenient", "incorporate", "incorporated",
    "incorrect", "increase", "increased", "increasing", "increasingly",
    "incredible", "incredibly", "increment", "incremental",
    "incubate", "incubation", "incumbent", "indebted", "indecent",
    "indecision", "indefinite", "indefinitely", "indelible",
    "indemnity", "indentation", "independent", "independently",
    "index", "indexing", "indicate", "indicated", "indication",
    "indicative", "indicator", "indictment", "indigenous",
    "indigent", "indignant", "indignation", "indirect",
    "indirectly", "indiscreet", "indiscriminate", "indispensable",
    "indistinguishable", "individual", "individualism",
    "individualist", "individuality", "individually", "indivisible",
    "indoctrinate", "indolent", "indoor", "indoors", "induce",
    "induced", "induction", "inductive", "indulge", "indulgence",
    "industrial", "industrialize", "industry", "ineffective",
    "ineffectual", "inefficiency", "inefficient", "inelastic",
    "inept", "inequality", "inequitable", "inert", "inertia",
    "inescapable", "inevitable", "inevitably", "inexact",
    "inexcusable", "inexhaustible", "inexpensive", "inexperience",
    "inexperienced", "inexpert", "inexplicable", "infallible",
    "infamous", "infancy", "infant", "infantry", "infect",
    "infection", "infectious", "infer", "inference", "inferior",
    "inferiority", "infinite", "infinitely", "infinity", "inflame",
    "inflammation", "inflate", "inflated", "inflation", "inflect",
    "inflection", "inflexible", "inflow", "influence", "influential",
    "info", "inform", "informal", "informally", "information",
    "informative", "infrared", "infrastructure", "infrequent",
    "infrequently", "infuriate", "ingenious", "ingenuity",
    "ingredient", "inhabit", "inhabitant", "inhale", "inherent",
    "inherently", "inherit", "inheritance", "inhibit", "inhibition",
    "inhibitor", "inhospitable", "initial", "initially",
    "initiate", "initiation", "initiative", "inject", "injection",
    "injure", "injured", "injury", "injustice", "ink", "inland",
    "inlet", "inline", "inner", "innermost", "innocence",
    "innocent", "innovation", "innovative", "innovator", "innumerable",
    "inordinate", "input", "inputs", "inquire", "inquiry", "inquisition",
    "inquisitive", "insane", "insanity", "insecure", "insecurity",
    "insensitive", "insert", "insertion", "inside", "insider",
    "insight", "insightful", "insignia", "insignificant",
    "insist", "insistence", "insistent", "insoluble", "inspect",
    "inspection", "inspector", "inspiration", "inspire", "inspired",
    "instability", "install", "installation", "instance",
    "instant", "instantaneous", "instantly", "instead", "instinct",
    "instinctive", "institute", "institution", "institutional",
    "instruct", "instruction","instructions", "instructional", "instructor",
    "instrument", "instrumental", "insufficient","insufficiency" "insulate",
    "insulation", "insulin", "insult", "insurance", "insure",
    "intact", "intake", "integer", "integral", "integrate",
    "integrated", "integration", "integrity", "intellect",
    "intellectual", "intelligent", "intelligible", "intend",
    "intended", "intense", "intensely", "intensify", "intensity",
    "intensive", "intent", "intention", "intentional", "interact",
    "interaction", "interactive", "intercept", "interchange",
    "interconnect", "interconnection", "interdependence",
    "interest", "interested", "interesting", "interface",
    "interfere", "interference", "interim", "interior", "interject",
    "interlock", "intermediate", "internal", "internally",
    "international", "internet", "interpersonal", "interpret",
    "interpretation", "interpreter", "interrogate", "interrupt",
    "interruption", "intersection", "interval", "intervene",
    "intervention", "interview", "intestate", "intestinal",
    "intimate", "intimately", "intimidate", "into", "intolerable",
    "intolerance", "intolerant", "intone", "intramural", "intranet",
    "intransitive", "intrinsic", "intrinsically", "introduce",
    "introduction", "introductory", "introspective", "intrude",
    "intrusion", "intuition", "intuitive", "inundate", "invade",
    "invalid", "invaluable", "invasion", "invasive", "invent",
    "invention", "inventive", "inventor", "inverse", "invert",
    "invest", "investigate", "investigation", "investigator",
    "investment", "investor", "invisible", "invitation", "invite",
    "invoke", "involuntary", "involve", "involved", "involvement",
    "invulnerable", "inward", "inwards"
}

PREFIX_WHITELIST = {
    "the": THE_WHITELIST,
    "with": WITH_WHITELIST,
    "over": OVER_WHITELIST,
    "under": UNDER_WHITELIST,
    "in": IN_WHITELIST
    # Add more as needed:
    # "from": FROM_WHITELIST,
    # "into": INTO_WHITELIST,
    # etc.
}
