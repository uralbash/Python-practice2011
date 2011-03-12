# coding: utf-8

def main(args):
    if len(args) > 3:
        script_name, input_file_name, output_file_name = args
    else:
        input_file_name, output_file_name = "input.txt", "output.txt"
    input_file = open(input_file_name)
    output_file = open(output_file_name, 'w')
    
    string = "1 2 3 4 5 6 7 8 9 10"
    encoded_content = ""
    
    for line in input_file:
        for i in range(len(line)):
            if ord(line[i]) > 191 and ord(line[i]) < 256:
                offset = 0;
                if line[i].islower():
                    offset = 32
                if ord(line[i]) + int(string.split(' ')[i%len(string.split(' '))]) > 223+offset:
                    encoded_content += chr(191+offset+(ord(line[i]) + int(string.split(' ')[i%len(string.split(' '))]))%(223+offset))
                else:
                    encoded_content += chr(ord(line[i]) + int(string.split(' ')[i%len(string.split(' '))]))
            else:
                encoded_content += line[i]
    output_file.write(encoded_content)
    input_file.close()
    output_file.close()


if __name__ == '__main__':
    from sys import argv
    main(argv)
