import sys
from collections import defaultdict

# Map instructions and registers to their hex values
MAP_INS_OPC = {
    "sw": "0", "j": "1", "add": "2", "sll": "3", 
    "sub": "4", "srl": "5", "and": "6", "beq": "7", 
    "addi": "8", "andi": "9", "subi": "a", "ori": "b", 
    "or": "c", "nor": "d", "lw": "e", "bneq": "f"
}

MAP_REG_ADD = {
    "$zero": "0", "$t0": "1", "$t1": "2", "$t2": "3", 
    "$t3": "4", "$t4": "5", "$t5": "6", "$sp": "7"
}

instructionsR = {"add", "sub", "and", "or", "sll", "srl", "nor"}
instructionsI = {"addi", "subi", "andi", "ori", "sw", "lw", "beq", "bneq"}

# Helper functions
def dec_to_hex(n):
    return f"{int(n):x}".zfill(2)

def dec_to_hex_pad_trim(d_s):
    t = dec_to_hex(d_s)
    return t[-2:]

def tokenize(string, delim):
    return [s.strip() for s in string.split(delim) if s.strip()]

# Main assembler class
class Assembler:
    def __init__(self):
        self.machine_code = []
        self.line_label = []
        self.label_map = {}
        self.instruction_counter_map = {}
        self.counter = 0

    def process_instruction(self, ins, info):
        info = info.replace(" ", "")
        parts = tokenize(info, ',')

        if ins in instructionsR:  # R-type
            dest_reg, src_reg_1, src_reg_2 = parts
            sh_amt = "0"
            if ins in {"sll", "srl"}:
                sh_amt = dec_to_hex(src_reg_2)
                src_reg_2 = "0"

            output = (MAP_INS_OPC[ins] + MAP_REG_ADD[src_reg_1] + 
                      MAP_REG_ADD[src_reg_2] + MAP_REG_ADD[dest_reg] + sh_amt)
            self.machine_code.append(output)

        elif ins in instructionsI:  # I-type
            dest_reg, src_reg, imm_or_label = parts[0], parts[1], parts[2]

            if ins in {"addi", "subi", "andi", "ori"}:
                imm = dec_to_hex_pad_trim(imm_or_label)
                output = (MAP_INS_OPC[ins] + MAP_REG_ADD[src_reg] + 
                          MAP_REG_ADD[dest_reg] + imm)
            elif ins in {"sw", "lw"}:
                if "(" in imm_or_label:
                    offset, base = tokenize(imm_or_label, '(')
                    base = base.replace(")", "")
                    imm = dec_to_hex_pad_trim(offset)
                    output = (MAP_INS_OPC[ins] + MAP_REG_ADD[base] + 
                              MAP_REG_ADD[dest_reg] + imm)
                else:
                    output = MAP_INS_OPC[ins] + MAP_REG_ADD[src_reg] + MAP_REG_ADD[dest_reg] + "00"
            elif ins in {"beq", "bneq"}:
                label = imm_or_label
                if label not in self.label_map:
                    output = MAP_INS_OPC[ins] + MAP_REG_ADD[src_reg] + MAP_REG_ADD[dest_reg]
                    self.line_label.append((self.counter, label))
                    self.instruction_counter_map[output] = self.counter
                else:
                    offset = self.label_map[label] - self.counter - 1
                    offset_hex = dec_to_hex_pad_trim(str(offset))
                    output = (MAP_INS_OPC[ins] + MAP_REG_ADD[src_reg] + 
                              MAP_REG_ADD[dest_reg] + offset_hex)
            self.machine_code.append(output)

        elif ins == "j":  # J-type
            label = parts[0]
            if label not in self.label_map:
                output = MAP_INS_OPC[ins]
                self.line_label.append((self.counter, label))
            else:
                output = MAP_INS_OPC[ins] + self.label_map[label] + "00"
            self.machine_code.append(output)

        elif ":" in ins:  # Label
            label = tokenize(ins, ":")[0]
            addr = dec_to_hex(self.counter)
            self.label_map[label] = addr

    def resolve_labels(self):
        for idx, label in self.line_label:
            if label in self.label_map:
                str_code = self.machine_code[idx]
                if str_code.startswith(MAP_INS_OPC["j"]):
                    self.machine_code[idx] = str_code + self.label_map[label] + "00"
                else:
                    offset = int(self.label_map[label], 16) - idx - 1
                    offset_hex = dec_to_hex_pad_trim(str(offset))
                    self.machine_code[idx] += offset_hex

    def assemble(self, instructions):
        for ins, info in instructions:
            self.counter = len(self.machine_code)
            self.process_instruction(ins, info)
        self.resolve_labels()
        return self.machine_code

# Example Usage
if __name__ == "__main__":
    instructions = [
        ("add", "$t1,$t2,$t3"), 
        ("addi", "$t0,$t1,5"), 
        ("sw", "$t0,4($sp)"), 
        ("j", "target"), 
        ("target:", "")
    ]

    assembler = Assembler()
    machine_code = assembler.assemble(instructions)
    
    print("v2.0 raw")
    print(" ".join(machine_code))