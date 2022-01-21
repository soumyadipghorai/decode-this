import streamlit as st 
import encryption as enc 
import time 
import random 

# Level definition : 
    # easy --> 3 easy | 2 med 
    # medium --> 2 easy | 2 med | 1 hard 
    # hard --> 1 easy | 2 med | 2 hard 

# body
st.title('Decode This')
st.image('static/images/decode_this.gif')
difficulty = st.sidebar.radio('Choose Difficulty', ['Easy', 'Medium', 'Hard'])

# words 
easy_text = ["what's Up", "Let's Go", "Come on"]
medium_text = ["Say my name", 'Help me out']
hard_text = ['difficult question', 'See you again']

flag = True #checker 

# for easy level 
#               ==> 1st 3 questions will be easy
#               ==> rest medium  
if difficulty == 'Easy' : 
    st.subheader('You are playing in easy mode \n start guessing')
    i = 0
    while flag and i < 5  :

        # hint text
        if i >= 0 and i <= 2: 
            actual_text = easy_text[i]
            output_text = enc.easy_encryption(actual_text)
            st.write('Hint : ',output_text)
            
        else : 
            actual_text = medium_text[i-3]
            output_text = enc.medium_encryption(actual_text)
            st.write('Hint : ',output_text)


        i += 1 # increment++ 

        # input area 
        input_text = st.text_input('Enter your guess', key=i)
        check = st.button('Check', i+1)

        # checker 
        if check :
            if input_text == actual_text : 
                st.success('Right Answer')
                continue
            else : 
                st.error('Wrong Answer')
                st.button('Restart!')
                flag = False
                break

# ##################### timer #####################
progress, counter = st.progress(0), 0
for j in range(100) : 
    time.sleep(0.01*(i+1))
    counter += 1 
    progress.progress(j+1)
if not check and counter == 100 : 
    st.warning('Time\'s Up')
    st.button('Restart!')
    # break

# for medium level 
#               ==> 1st 2 questions will be easy
#               ==> 2nd and 3rd medium
#               ==> rest hard 
if difficulty == 'Medium' : 
    st.subheader('You are playing in medium mode \n start guessing')
    i = 0
    while flag and i < 5  :

        # hint text
        if i == 0 or i == 1: 
            actual_text = easy_text[i]
            output_text = enc.easy_encryption(actual_text)
            st.write('Hint : ',output_text)
            
        elif i == 2 or i == 3 : 
            actual_text = medium_text[i-2]
            output_text = enc.medium_encryption(actual_text)
            st.write('Hint : ',output_text)
        else :
            actual_text = hard_text[i-4]
            output_text = enc.hard_encryption(actual_text)
            st.write('Hint : ',output_text)

        i += 1 # increment++ 

        # input area 
        input_text = st.text_input('Enter your guess', key=i)
        check = st.button('Check', i+1)

        # checker
        if check :
            if input_text == actual_text : 
                st.success('Right Answer')
                continue
            else : 
                st.error('Wrong Answer')
                flag = False
                break

# ##################### timer #####################
        progress, counter = st.progress(0), 0
        for j in range(100) : 
            time.sleep(0.15*(i+1))
            counter += 1 
            progress.progress(j+1)
        if not check and counter == 100 : 
            st.warning('Time\'s Up')
            break

# for medium level 
#               ==> 1st question will be easy
#               ==> 2nd and 3rd medium
#               ==> rest hard 
if difficulty == 'Hard' : 
    st.subheader('You are playing in hard mode \n start guessing')
    i = 0
    while flag and i < 5  :
        for i in range(5) : 
            if i == 0 : 
                actual_text = easy_text[i]
                output_text = enc.easy_encryption(actual_text)
                st.write('Hint : ',output_text)
                
            elif i == 1 or i == 2  : 
                actual_text = medium_text[i-1]
                output_text = enc.medium_encryption(actual_text)
                st.write('Hint : ',output_text)

            else :
                actual_text = hard_text[i-3]
                output_text = enc.hard_encryption(actual_text)
                st.write('Hint : ',output_text)

            i += 1 # increment++

            # input area 
            input_text = st.text_input('Enter your guess', key=i)
            check = st.button('Check', i+1)

            # checker
            if check :
                if input_text == actual_text : 
                    st.success('Right Answer')
                    continue
                else : 
                    st.error('Wrong Answer')
                    break

# ##################### timer #####################
        progress, counter = st.progress(0), 0
        for j in range(100) : 
            time.sleep(0.2*(i+1))
            counter += 1 
            progress.progress(j+1)
        if not check and counter == 100 : 
            st.warning('Time\'s Up')
            break