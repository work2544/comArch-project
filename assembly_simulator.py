import os


def get_opcode(name_of_instruction):
    
    opcode = ''
    type=''
    if name_of_instruction == 'add':
        opcode = '000'
        type='R'
    elif name_of_instruction == 'nand':
        opcode = '001'
        type='R'
    elif name_of_instruction == 'lw':
        opcode = '010'
        type='I'
    elif name_of_instruction == 'sw':
        opcode = '011'
        type='I'
    elif name_of_instruction == 'beq':
        opcode = '100'
        type='I'
    elif name_of_instruction == 'jalr':
        opcode = '101'
        type='J'
    elif name_of_instruction == 'halr':
        opcode = '110'
        type='O'
    elif name_of_instruction == 'noop':
        opcode = '111'
        type='O'
    else: raise Exception("Unknown instruction: %s" %name_of_instruction)
    return opcode,type


def get_regA(name_of_reg):
    return 1


def get_regB(name_of_reg):
    return 1


def get_desReg(name_of_reg):
    return 1


def get_offset(number_offset):
    return 1




"""Get All Files From Directory"""
assembly_path='assemby_code/'
assembly_code = os.listdir(assembly_path)
#print(assembly_code[0])

"""Open Assembly Files """
f = open(os.path.join(assembly_path,assembly_code[0]) , 'r')

"""Add All Assembly To Array"""
ALL_INSTRUCTION = []
for N in f:
    ALL_INSTRUCTION.append(N.replace("\n", ""))
#print(ALL_INSTRUCTION)

"""Loop through Assembly To Generate Machine_Code"""
for N in ALL_INSTRUCTION:  
    """
    # Current_Instruction[0] is name of instruction , 
    # Current_Instruction[1] is name of regDest ,
    # Current_Instruction[2] is name of regA ,
    # Current_Instruction[3] is  regB or offset.
    
    """
    
    Current_Instruction = N.split()
    
    Machine_Code,opcode,type,regA,regB,destReg,offsetField = ''
    opcode,type = get_opcode(Current_Instruction[0])
    if type == 'R':
        regA=get_regA(Current_Instruction[1])
        regB=get_regB(Current_Instruction[2])
        destReg=get_desReg(Current_Instruction[3])
    elif type == 'I':
        regA=get_regA(Current_Instruction[1])
        regB=get_regB(Current_Instruction[2])
        offsetField=get_offset(Current_Instruction[3])
    elif type == 'J':
        regA=get_regA(Current_Instruction[1])
        regB=get_regB(Current_Instruction[2])
    elif type == 'O':
        print ("Noop")
    
    print(opcode, regA, regB, destReg, offsetField)
    
    
    
