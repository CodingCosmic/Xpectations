from capstone import *

class X86Analyzer:
    def __init__(self, binary_code):
        self.binary_code = binary_code
        self.disassembler = Cs(CS_ARCH_X86, CS_MODE_64)  # For 64-bit x86

    def identify_instructions(self):
        instructions = []
        try:
            for i in self.disassembler.disasm(self.binary_code, 0x1000):
                instr_str = f"0x{i.address:x}:\t{i.mnemonic}\t{i.op_str}"
                instructions.append(instr_str)
                print(instr_str)
        except Exception as e:
            print(f"Error during disassembly: {e}")
        return instructions
