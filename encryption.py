import random 

# --simply reverse the text character by character
def easy_encryption(text) : 
    ans = ''
    for i in reversed(range(len(text))) : 
        ans += text[i]
    return ans 

# --mix up the words first 
# --then prints them character by character in reverse order 
def medium_encryption(text) : 
    text = text.split(' ')
    ans = ''
    n = random.randint(0, len(text)-1) 

    times = random.randint(1,3)
    for i in range(times) : 
        to_remove = text[n]
        text.remove(to_remove)
        text.append(to_remove)
        
    for word in text : 
        new_word = ''
        for i in reversed(range(len(word))) : 
            new_word += word[i]
        ans += new_word + ' '

    return ans 

    
def hard_encryption(text):
    
    count = 0
    for i in range(len(text)) : 
        if text[i] == '' : 
            count += 1
    
    correct_length = len(text) - count 
    
    if int(pow(correct_length, 0.5)) < pow(correct_length, 0.5) : 
        row = int(pow(correct_length, 0.5))
        column = int(pow(correct_length, 0.5)) + 1
    
    else :
        row = int(pow(correct_length, 0.5))
        column = int(pow(correct_length, 0.5))
    
    if (row*column) < len(text) : 
        row += 1
    itter = 0
    split_list = []
    
    while itter < correct_length : 
    
        if itter + column < correct_length : 
    
            for i in range(itter,len(text)) : 
    
                if text[i] != '' : 
                    split_list.append(text[i:i+column])
                    break
    
        else : 
    
            for i in range(itter,len(text)) : 
                if text[i] != 0 : 
                    split_list.append(text[i:])
                    break

        itter = itter + column 
    final_list = []

    if len(split_list[-1]) < column : 
        diff = column-len(split_list[-1])
        split_list[-1] = split_list[-1] + diff*' '

    for i in range(column) : 
        sum = ''
        for j in range(row) : 

            if split_list[j][i] != ' ' : 
                sum += split_list[j][i]
        final_list.append(sum)

    ans = ''
    for i in range(len(final_list)) : 
        ans += final_list[i] + ' '

    return ans 


def harder_encryption(text) : 
    count = 0
    for i in range(len(text)) : 
        if text[i] == '' : 
            count += 1
    correct_length = len(text) - count 
    if int(pow(correct_length, 0.5)) < pow(correct_length, 0.5) : 
        row = int(pow(correct_length, 0.5))
        column = int(pow(correct_length, 0.5)) + 1
    else :
        row = int(pow(correct_length, 0.5))
        column = int(pow(correct_length, 0.5))
    # print(row)
    # print(column)
    if (row*column) < len(text) : 
        row += 1
    itter = 0
    split_list = []
    while itter < correct_length : 
        if itter + column < correct_length : 
            for i in range(itter,len(text)) : 
                # print(s[i:i+4])
                if text[i] != '' : 
                    split_list.append(text[i:i+column])
                    break
        else : 
            for i in range(itter,len(text)) : 
                # print(s[i:i+4])
                if text[i] != 0 : 
                    split_list.append(text[i:])
                    break
        # print(itter)
        itter = itter + column 
    final_list = ""
    if len(split_list[-1]) < column : 
        diff = column-len(split_list[-1])
        split_list[-1] = split_list[-1] + diff*' '
    # print(split_list)
    for i in range(column) : 
        sum = ''
        for j in range(row) : 
            # print(j,i)
            if split_list[j][i] != ' ' : 
                sum += split_list[j][i]
            # continue
        # for k in range(len(split_list[-1])) : 
        #     sum += split_list[k]
        #     break
        final_list += sum + " "
    # print(final_list)
    return final_list

# i l o v
# e i n d 
# i a