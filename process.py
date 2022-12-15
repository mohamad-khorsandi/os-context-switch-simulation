from instruction import Instruction
from state import State
class Process:
    def __init__(self):
        self.id = None
        self.state = None
        self.inst_list = []

        self.PC = 0
        self.IR = None
        self.TMP = None
        self.ACC = None

    def create_process(self, id, file_name):
        self.id = id
        file = open(file_name, 'r')
        line = file.readline()

        while line:
            ins_type = line.split(' ')[0]
            ins_num = line.split(' ')[1]
            inst = Instruction(ins_type, int(ins_num), self)
            self.inst_list.append(inst)
            line = file.readline()
            
    def run_process(self):
        self.inst_list[self.PC].run()
    
    def block_process(self):
        self.state = State.blocked

