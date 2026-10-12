# polymorphism
class Llm:
    def __init__(self, model, version):
        self.model = model
        self.version = version
    def tokens(self):
        return '1 million tokens'

class Llm2(Llm):
    def __init__(self, model, version):
        super().__init__(model, version)
        self.tokens = self.tokens
    def tokens(self):
        return '10 million tokens'     

llm_record = Llm('gpt',  3.5)
print(llm_record.tokens())

llm_record2 = Llm2('claude-sonnet',  5.5)
print(llm_record2.tokens())