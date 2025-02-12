import os
from pickletools import opcodes

from numpy import int32


def isNumber(value):
    """ Checks if value is a string or number"""
    try:
        float(value)   # Type-casting the string to `float`.
                   # If string is not a valid `float`, 
                   # it'll raise `ValueError` exception
    except ValueError:
        return False
    return True


def get_opcode(name_of_instruction):

    opcode = 0b0
    type = ''
    if name_of_instruction == 'add':
        opcode = 0b000
        type = 'R'
    elif name_of_instruction == 'nand':
        opcode = 0b001
        type = 'R'
    elif name_of_instruction == 'lw':
        opcode = 0b010
        type = 'I'
    elif name_of_instruction == 'sw':
        opcode = 0b011
        type = 'I'
    elif name_of_instruction == 'beq':
        opcode = 0b100
        type = 'I'
    elif name_of_instruction == 'jalr':
        opcode = 0b101
        type = 'J'
    elif name_of_instruction == 'halt':
        opcode = 0b110
        type = 'O'
    elif name_of_instruction == 'noop':
        opcode = 0b111
        type = 'O'
    else:
        raise Exception("Unknown instruction: %s" % name_of_instruction)

    opcode = opcode 
    return opcode, type


def get_regA(field2):

    if not isNumber(field2):
        pass
    else:
        field2 = int(field2)

    field2 = field2 
    return field2


def get_regB(field3):

    if not isNumber(field3):
        pass
    else:
        field3 = int(field3)

    field3 = field3 
    return field3


def get_desReg(field0):
    field0 = int(field0)
    return field0


def get_offset(name,field3,idx):

    if isNumber(field3):
        field3=int(field3)
    else:
        for i in range(0, len(All_INSTRUCTION)): #get address of the label
            if All_INSTRUCTION[i][0]== field3:
                field3 = i
                break
        if(name == 'beq'):
            field3 = field3 - idx - 1 # because PC + 1 after excution 
    
    if (field3 < 0):
            field3 = field3 % (1<<16)
            
    return field3


"""Get All Files From Directory"""
assembly_path = 'assemby_code/'
assembly_code = os.listdir(assembly_path)
"""Open Assembly Files """
f = open(os.path.join(assembly_path, assembly_code[2]), 'r')


"""Add All Assembly To Array"""
All_INSTRUCTION = []
All_MACHINECODE = []
for N in f:
    All_INSTRUCTION.append(N.replace("\n", "").split())
    
    
    
ZERO = 0
Resgister ={
    '0' :ZERO,
    '1' :0,
    '2' :0,
    '3' :0,
    '4' :0,
    '5' :0,
    '6' :0,
    '7' :0
}

"""Loop through Assembly To Generate Machine_Code"""
for idx in range(0,len(All_INSTRUCTION)):
    Current_Instruction=All_INSTRUCTION[idx]
    Machine_Code = opcode = regA = regB =  0b0
    destReg = offsetField = type = None
    if  Current_Instruction[0] in ['add','nand','lw','sw','beq','jalr','halt','noop','.fill']: # no label in instruction case
        
        """
        # Current_Instruction[0] is name of instruction , 
        # Current_Instruction[1] is name of regDest ,
        # Current_Instruction[2] is name of regA ,
        # Current_Instruction[3] is  regB or offset.

        """
        if(Current_Instruction[0] != '.fill'):
            opcode, type = get_opcode(Current_Instruction[0])
            if type == 'R':
                regA = get_regA(Current_Instruction[1])
                regB = get_regB(Current_Instruction[2])
                destReg = get_desReg(Current_Instruction[3])
                Machine_Code =  (opcode << 22) | (regA<<19) | (regB<<16) | destReg
            elif type == 'I':
                regA = get_regA(Current_Instruction[1])
                regB = get_regB(Current_Instruction[2])
                offsetField = get_offset(Current_Instruction[0],Current_Instruction[3],idx)
                Machine_Code = (opcode<<22) | (regA<<19) | (regB<<16) | offsetField
            elif type == 'J':
                regA = get_regA(Current_Instruction[1])
                regB = get_regB(Current_Instruction[2])
                Machine_Code = (opcode<<22) | (regA<<19) | (regB<<16)
            elif type == 'O':
                Machine_Code = (opcode<<22)
        else:
            Machine_Code = int(Current_Instruction[1])
    else: #label in instruction case

            """
            # Current_Instruction[0] is name of label , 
            # Current_Instruction[1] is name of instruction , 
            # Current_Instruction[2] is name of regA ,
            # Current_Instruction[3] is name of regB ,
            # Current_Instruction[4] is  destReg or offset.

            """
            
            if(Current_Instruction[1] != '.fill'):
                opcode, type = get_opcode(Current_Instruction[1])
                if type == 'R':
                    regA = get_regA(Current_Instruction[2])
                    regB = get_regB(Current_Instruction[3])
                    destReg = get_desReg(Current_Instruction[4])
                    Machine_Code =  (opcode << 22) | (regA<<19) | (regB<<16) | destReg
                elif type == 'I':
                    regA = get_regA(Current_Instruction[2])
                    regB = get_regB(Current_Instruction[3])
                    offsetField = get_offset(Current_Instruction[1],Current_Instruction[4],idx)
                    Machine_Code = (opcode<<22) | (regA<<19) | (regB<<16) | offsetField
                elif type == 'J':
                    regA = get_regA(Current_Instruction[2])
                    regB = get_regB(Current_Instruction[3])
                    Machine_Code = (opcode<<22) | (regA<<19) | (regB<<16)
                elif type == 'O':
                    Machine_Code = (opcode<<22)
            else:
                Machine_Code = get_offset(Current_Instruction[1],Current_Instruction[2],idx)
                    
    #print(f"opcode: {bin(opcode)} regA: {bin(regA)} regB: {bin(regB)} destReg: {bin(destReg) if destReg is not None else None} offsetField: {bin(offsetField) if offsetField is not None else None}")
    print(f"Machine_Code: {Machine_Code} ({format(Machine_Code,'#x')})")
    All_MACHINECODE.insert(0,format((Machine_Code),'032b'))




# for N in ALL_MACHINECODE:
#     hstr = '%0*X' % ((len(N) + 3) // 4, int(N, 2))
#     print(hstr)