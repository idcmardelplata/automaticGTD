class InboxText:
    def __init__(self, **options):
        self.path = options.get("path", "/tmp/inputs.txt")
        self.inputs = []

    def add(self, text):
        if text in self.inputs:
            return
        self.inputs.append(text)
        with open(self.path, "a+") as file:
            file.write(text)

    def count(self):
        return len(self.inputs)

    def load(self):
        with open(self.path, "r+") as file:
            self.inputs = file.readlines()
        return self.inputs
   
    def clean(this):
        this.cleanList()
        this.cleanDisk()

    def cleanList(self):
        if self.inputs!=0:
            self.inputs.clear()

    def cleanDisk(self):
        with open(self.path, "r+") as file:
            file.truncate(0)
