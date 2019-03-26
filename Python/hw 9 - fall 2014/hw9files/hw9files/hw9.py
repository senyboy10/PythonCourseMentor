def parse_file(f):
    i = -1
    all_char = []
    char = []
    for line in open(f):
        char.append(line.replace('\n','.'))
        i += 1
        if i % 8 == 0:
            all_char.append(char)
            char = []
            
    return all_char

def kerning_parse(f, b_char):
    all_char = parse_file(f)
    new_all_char = ['']
    
    for char in all_char[1:]:
        '''
        char[1] = char[1][:-1]
        char[2] = char[2][:-1]
        char[3] = char[3][:-1]
        char[4] = char[4][:-1]
        char[5] = char[5][:-1]
        char[6] = char[6][:-1]
        char[7] = char[7][:-1]
        '''
        if char[0] == "32 ' '.":
            new_all_char.append(char)
            continue
        i = 5
        while i > 0:
            if char[1][i] == char[2][i] == char[3][i] == char[4][i] == char[5][i] == char[6][i] == char[7][i] == '.' and \
               char[1][i-1] == char[2][i-1] == char[3][i-1] == char[4][i-1] == char[5][i-1] == char[6][i-1] == char[7][i-1] == '.':
                char[1] = char[1][:i]
                char[2] = char[2][:i]
                char[3] = char[3][:i]
                char[4] = char[4][:i]
                char[5] = char[5][:i]
                char[6] = char[6][:i]
                char[7] = char[7][:i]
            i -= 1
        
        j = 0
        while j < 1:
            if char[1][j] == '.' and char[2][j] == '.' and char[3][j] == '.' and char[4][j] == '.' and char[5][j] == '.' and char[6][j] == '.' and char[7][j] == '.':
                char[1] = char[1][j+1:]
                char[2] = char[2][j+1:]
                char[3] = char[3][j+1:]
                char[4] = char[4][j+1:]
                char[5] = char[5][j+1:]
                char[6] = char[6][j+1:]
                char[7] = char[7][j+1:]
            j += 1
        
        char[1] = '.' + char[1]
        char[2] = '.' + char[2]
        char[3] = '.' + char[3]
        char[4] = '.' + char[4]
        char[5] = '.' + char[5]
        char[6] = '.' + char[6]
        char[7] = '.' + char[7]
        
        new_all_char.append(char)   
        
    return new_all_char  
                    

def print_message(message, b_char, f_char, all_char, kerning_bool):
    message_list = list(message)

    sent1 = []
    sent2 = []
    sent3 = []
    sent4 = []
    sent5 = []
    sent6 = []
    sent7 = []
    k = False
    for letter in message_list:
        if letter == ' ':
            sent1.append(all_char[1][1].replace('\n','.'))
            sent2.append(all_char[1][2].replace('\n','.'))
            sent3.append(all_char[1][3].replace('\n','.'))
            sent4.append(all_char[1][4].replace('\n','.'))
            sent5.append(all_char[1][5].replace('\n','.'))
            sent6.append(all_char[1][6].replace('\n','.'))
            sent7.append(all_char[1][7].replace('\n','.'))
        elif letter == "'":
            sent1.append(all_char[8][1].replace('\n','.'))
            sent2.append(all_char[8][2].replace('\n','.'))
            sent3.append(all_char[8][3].replace('\n','.'))
            sent4.append(all_char[8][4].replace('\n','.'))
            sent5.append(all_char[8][5].replace('\n','.'))
            sent6.append(all_char[8][6].replace('\n','.'))
            sent7.append(all_char[8][7].replace('\n','.'))  
        
        for char in all_char[1:]:
            if letter == ' ' or letter == "'":
                continue
            elif letter == char[0][4] or letter == char[0][5]:
                if k == True and kerning_bool == True:
                    sent1.append(char[1] + '.')
                    sent2.append(char[2] + '.')
                    sent3.append(char[3] + '.')
                    sent4.append(char[4] + '.')
                    sent5.append(char[5] + '.')
                    sent6.append(char[6] + '.')
                    sent7.append(char[7] + '.')   
                    k = False
                    '''
                elif k == False and kerning_bool == True:
                    sent1.append('.' + char[1])
                    sent2.append('.' + char[2])
                    sent3.append('.' + char[3])
                    sent4.append('.' + char[4])
                    sent5.append('.' + char[5])
                    sent6.append('.' + char[6])
                    sent7.append('.' + char[7])    
                    '''
                else:
                    sent1.append(char[1])
                    sent2.append(char[2])
                    sent3.append(char[3])
                    sent4.append(char[4])
                    sent5.append(char[5])
                    sent6.append(char[6])
                    sent7.append(char[7])  
    
    sent1[:len(sent1)] = [''.join(sent1[:len(sent1)])]
    sent2[:len(sent2)] = [''.join(sent2[:len(sent2)])]
    sent3[:len(sent3)] = [''.join(sent3[:len(sent3)])]
    sent4[:len(sent4)] = [''.join(sent4[:len(sent4)])]
    sent5[:len(sent5)] = [''.join(sent5[:len(sent5)])]
    sent6[:len(sent6)] = [''.join(sent6[:len(sent6)])]
    sent7[:len(sent7)] = [''.join(sent7[:len(sent7)])]
    
    if b_char == '':
        b_char = '.'
        
    if f_char == '':
        f_char = '#'
    
    if sent1[0][0] != '.':
        sent1[0] = '.' + sent1[0]
        sent2[0] = '.' + sent2[0]
        sent3[0] = '.' + sent3[0]
        sent4[0] = '.' + sent4[0]
        sent5[0] = '.' + sent5[0]
        sent6[0] = '.' + sent6[0]
        sent7[0] = '.' + sent7[0]
        
    print sent1[0][1:-1].replace('#',f_char).replace('.',b_char)
    print sent2[0][1:-1].replace('#',f_char).replace('.',b_char)
    print sent3[0][1:-1].replace('#',f_char).replace('.',b_char)
    print sent4[0][1:-1].replace('#',f_char).replace('.',b_char)
    print sent5[0][1:-1].replace('#',f_char).replace('.',b_char)
    print sent6[0][1:-1].replace('#',f_char).replace('.',b_char)
    print sent7[0][1:-1].replace('#',f_char).replace('.',b_char)
    
        

if __name__ == '__main__':
    all_char = parse_file('simple_font.txt')
    
    message = raw_input("Please enter the message ==> ")
    print message
    
    b_char = raw_input("Please enter the background char (enter for .) ==> ")
    print b_char
    
    f_char = raw_input("Please enter the foreground char (enter for #) ==> ")
    print f_char
    
    kerning_all_char = kerning_parse('simple_font.txt', b_char)
    
    no_kerning = False
    kerning_bool = True
    
    print "No kerning"
    print_message(message, b_char, f_char, all_char, no_kerning)
    
    print "\n With kerning"
    print_message(message, b_char, f_char, kerning_all_char, kerning_bool)    