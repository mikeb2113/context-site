from . import libs
from enum import Enum
#NPLIST is populated, BREAKDOWN_LIST is not?
class Document():
    def __init__(self,text):
        self.text = self.breakdown(text) #Array of sentences. Then sub-arrays of words (belonging to each sentence)
        for array in self.text:
            self.BREAKDOWN_LIST.append(array)
            #print(self.NP_Identifier(array))
            #self.BREAKDOWN_LIST.append(self.NP_Identifier(self.text[i]))
        for array in self.BREAKDOWN_LIST:
            self.NPLIST.append(self.NP_Identifier(array))
            #sentence = sentence(array)
        #print(self.NPLIST)
        # for i in self.BREAKDOWN_LIST:
        #     print(i)

    BREAKDOWN_LIST = []
    NPLIST = []
    PPLIST = []

    DETLIST = []
    PREPLIST = []
    MODLIST = []
    AUXLIST = []
    CONJLIST = []
    COMPLIST = []

    ODDWRAPPER = ""

    seperators = {'-','/','\n'}
    #Maybe: refactor this so that the input is only one array? The maybe some larger function to trigger subcalls into the 
    #smaller arrays?
    #To this end, change breakdown
    def NP_Identifier(self,input):
        NP_intermediate = []
        NP_Builder = []
        PP_Builder = []
        overflow = []
        for item in input:
                if item not in libs.DET and item not in libs.PREP and item not in libs.AUX and item not in libs.MOD and item not in libs.COMP and item not in libs.CONJ:
                    #if len(NP_Builder) < 2:
                            NP_Builder.append(item)
                    #else:
                        # overflow.append(item)
                        # if len(overflow) == 2:
                        #     NP_intermediate.append(NP_Builder)
                        #     NP_intermediate.append(overflow)
                        #     overflow = []
                        #     NP_Builder = []
                else:
                    # if NP_Builder:
                    if len(NP_Builder)>0:
                        NP_intermediate.append(NP_Builder)
                        NP_Builder=[]
                        
                    if self.isPREP(item):
                        self.PREPLIST.append(item)
                        NP_intermediate.append(item)
                    elif self.isAUX(item):
                        self.AUXLIST.append(item)
                        NP_intermediate.append(item)
                    elif self.isMOD(item):
                        self.MODLIST.append(item)
                        NP_intermediate.append(item)
                    elif self.isCONJ(item):
                        self.CONJLIST.append(item)
                        NP_intermediate.append(item)
                    elif self.isCOMP(item):
                        self.COMPLIST.append(item)
                        NP_intermediate.append(item)
                    elif self.isDET(item):
                        self.DETLIST.append(item)
                        NP_intermediate.append(item)
        if NP_Builder:
            NP_intermediate.append(NP_Builder)
        if overflow:
            NP_intermediate.append(overflow)
        if PP_Builder:
            self.PPLIST.append(PP_Builder)

        return NP_intermediate

    def breakdown(self,input):
        sentences = self.split_input(input,self.TYPE.Period)
        words = []
        for i in range(len(sentences)):
            x = sentences[i]
            breakdown = self.split_input(x,self.TYPE.Space)
            words.append(breakdown)
        return words

    def split_input(self,text: str,in_mode: "Document.TYPE") -> list[str]:
        if in_mode == self.TYPE.Period:
            mode = self.TYPE.Period
        elif in_mode == self.TYPE.Space:
            mode = self.TYPE.Space
        text = text.lower()
        sentences = []
        buf = []
        if mode is self.TYPE.Period:
            for ch in text:
                if ch == '.':
                    sentence = ''.join(buf).strip()
                    if sentence:
                        sentences.append(sentence)
                    buf = []
                else:
                    buf.append(ch)
            # leftover
            sentence = ''.join(buf).strip()
            if sentence:
                sentences.append(sentence)

            return sentences
        elif mode is self.TYPE.Space:
            for ch in text:
                if ch.isspace() or ch in self.seperators:
                    sentence = ''.join(buf).strip()
                    if sentence:
                        sentences.append(sentence)
                    buf = []
                else:
                    buf.append(ch)
            # leftover
            sentence = ''.join(buf).strip()
            if sentence:
                sentences.append(sentence)

            return sentences

    def isDET(self,x):
        if x in libs.DET:
            return True
        return False
    def isPREP(self,x):
        if x in libs.PREP:
            return True
        return False
    def isAUX(self,x):
        if x in libs.AUX:
            return True
        return False
    def isMOD(self,x):
        if x in libs.MOD:
            return True
        return False
    def isCONJ(self,x):
        if x in libs.CONJ:
            return True
        return False
    def isCOMP(self,x):
        if x in libs.CONJ:
            return True
        return False
    
    def isEXISTENTIALDET(self,x):
        if x in libs.EXISTENTIAL_DET:
            return True
        return False
    def isUNIVERSALDET(self,x):
        if x in libs.UNIVERSAL_DET:
            return True
        return False
    def isNEGATIVEQUANT(self,x):
        if x in libs.NEGATIVE_QUANT:
            return True
        return False
        
    class TYPE(Enum):
            Period = 1
            Space = 2