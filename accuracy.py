def accu(sample_text, input_text):
    splited_sample_text = sample_text.split()
    word_count = len(splited_sample_text)
    splited_input_text = input_text.split()
    correct = 0
    input_word_count = len(splited_input_text)


    if word_count > input_word_count:
        for i in range(0,input_word_count-1):
            if splited_input_text[i] == splited_sample_text[i]:
                correct = correct+1

    else:
        for i in range(0,word_count-1):
            if splited_input_text[i] != splited_sample_text[i]:
                correct = correct+1

    accuracy = correct*100/word_count
    print(f'Your accuracy is {round(accuracy)} %')
    return correct