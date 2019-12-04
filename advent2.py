
def open_input(filename):
    data = []
    with open(filename) as f:
        for line in f:
            data.append(line)
    return data

def process_intcode(intcode, byte_seq):
    byte_seq_updated = byte_seq[:]
    if intcode[0] == 1:
        byte_seq_updated[intcode[3]] = byte_seq[intcode[1]] + byte_seq[intcode[2]]
    elif intcode[0] == 2:
        byte_seq_updated[intcode[3]] = byte_seq[intcode[1]] * byte_seq[intcode[2]]
    else:
        print("Wrong opcode" + str(intcode[0]))
    return byte_seq_updated

def process_byte_seq(byte_seq):
    pc = 0
    byte_seq_updated = byte_seq[:]
    try :
        while(byte_seq[pc] != 99):
            byte_seq_updated = process_intcode(byte_seq_updated[pc:pc+4], byte_seq_updated)
            pc += 4
    except IndexError:
        print(len(byte_seq))
        print(byte_seq)
        print("pc to big :" + str(pc))
        exit()
    return byte_seq_updated
        
if __name__ == "__main__":
    data = str(open_input('input2.txt')[0])
    main_byte_seq = [int(x) for x in data.split(',')]
    # Update before running 
    main_byte_seq[1] = 12
    main_byte_seq[2] = 2    
    # example 
    # byte_seq = [1,9,10,3,2,3,11,0,99,30,40,50]
    # byte_seq = [1,1,1,4,99,5,6,0,99]

    # first star
    # process_byte_seq(byte_seq)
    # print('The answer is ' + str(byte_seq[0]))

    # second star
    magic_number = 19690720
    noun = 0
    verb = 0
    it = 0
    while((noun < 99) or (verb < 99)):
        byte_seq_new = main_byte_seq[:]
        byte_seq_new[1] = noun
        byte_seq_new[2] = verb
        byte_seq_new = process_byte_seq(byte_seq_new)
        if(byte_seq_new[0] == magic_number):
            break
        if(noun == 99):
            verb += 1
            noun = 0
        else:
            noun += 1
        print("Iteration: " + str(it) + str(byte_seq_new[0]))            
        it+=1
    print('The answer is ' + str((100 * noun) + verb))
    pass