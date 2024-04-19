import os
import cv2

import numpy as np
import streamlit as st 


from PIL import Image
from keras.models import load_model
from streamlit_drawable_canvas import st_canvas

def softmax(x):

    e_x = np.exp(x - np.max(x))

    return e_x / e_x.sum(axis = 0) 
def format_path(path) : 

    path = path.replace('\n' , '')
    path = path.replace('\t' , '')
    path = path.replace(' ' , '')

    return path
def get_predictions(path , model) : 

    image = cv2.imread(path)
    image = cv2.resize(image, (64, 64))
    image = image / 255
    image = image.reshape(-1, 64, 64, 3)
    result = model.predict(image)

    return result
def predict(username) : 

    saved_images = os.listdir(
        format_path(
            f'''
            Assets/
                Users/
                    {username}/
            '''
        )
    )

    saved_images = [
        format_path(
            f'''
            Assets/
                Users/
                    {username}/
            '''
        ) + path 
        for path 
        in saved_images
    ]
    model = load_model('model.hdf5')

    results = [
        get_predictions(path , model)
        for path 
        in saved_images
    ]

    images = [
        Image.open(path)
        for path 
        in saved_images
    ]

    st.write(saved_images[0].split('.')[0][-1].upper())

    actuals = [
        Image.open(f'Assets/Images/{path.split(".")[0][-1]}.png')
        for path 
        in saved_images
    ]
    

    return images , results , actuals
def get_canvas(key , stroke) : 

    canvas_result = st_canvas(
        fill_color = 'rgba(255, 165, 0, 0.3)' , 
        stroke_width = stroke , 
        stroke_color = '#000000' , 
        background_color = '#EEEEEE' , 
        background_image = stoi[key.lower()] , 
        update_streamlit = True , 
        height = 450 , 
        drawing_mode = 'freedraw' , 
        point_display_radius = 0 , 
        display_toolbar = True , 
        key = key
    )

    return canvas_result
def save_canvas(canvas , username , key) : 

        image = Image.fromarray(canvas.image_data)

        os.makedirs(
            format_path(
                f'''
                Assets/
                    Users/
                        {username}
                ''')     , 
                exist_ok = True
        )

        image.save(format_path(
            f'''
            Assets/
                Users/
                    {username}/
                        {key}.png
            '''
        ))
def get_user_data(username) : 

    saved_images = os.listdir(
        format_path(
            f'''
            Assets/
                Users/
                    {username}/
            '''
        )
    )

    saved_images = [
        format_path(
            f'''
            Assets/
                Users/
                    {username}/
            '''
        ) + path
        for path 
        in saved_images
    ]

    images = [
        Image.open(path)
        for path 
        in saved_images
    ]

    actuals = [
        Image.open(f'Assets/Images/{path.split(".")[0][-1]}.png')
        for path 
        in saved_images
    ]
    
    return images , actuals
def user() : 

    col_1 , col_2 = st.columns(2)
    images , actuals = get_user_data(username)

    for image , actual in zip(images , actuals) : 

        col_1.image(image)
        col_2.image(actual)

def predictions() :

        stroke = st.slider('Stroke Width' , 1 , 25 , 15)

        canvas_a = get_canvas('A' , stroke)
        if st.button('Capture A') : save_canvas(canvas_a , username , 'A')

        canvas_b = get_canvas('B' , stroke)
        if st.button('Capture B') : save_canvas(canvas_b , username , 'B')

        canvas_c = get_canvas('C' , stroke)
        if st.button('Capture C') : save_canvas(canvas_c , username , 'C')

        canvas_d = get_canvas('D' , stroke)
        if st.button('Capture D') : save_canvas(canvas_d , username , 'D')

        canvas_e = get_canvas('E' , stroke)
        if st.button('Capture E') : save_canvas(canvas_e , username , 'E')

        canvas_f = get_canvas('F' , stroke)
        if st.button('Capture F') : save_canvas(canvas_f , username , 'F')

        canvas_g = get_canvas('G' , stroke)
        if st.button('Capture G') : save_canvas(canvas_g , username , 'G')

        canvas_h = get_canvas('H' , stroke)
        if st.button('Capture H') : save_canvas(canvas_h , username , 'H')

        canvas_i = get_canvas('I' , stroke)
        if st.button('Capture I') : save_canvas(canvas_i , username , 'I')

        canvas_j = get_canvas('J' , stroke)
        if st.button('Capture J') : save_canvas(canvas_j , username , 'J')

        canvas_k = get_canvas('K' , stroke)
        if st.button('Capture K') : save_canvas(canvas_k , username , 'K')

        canvas_l = get_canvas('L' , stroke)
        if st.button('Capture L') : save_canvas(canvas_l , username , 'L')

        canvas_m = get_canvas('M' , stroke)
        if st.button('Capture M') : save_canvas(canvas_m , username , 'M')

        canvas_n = get_canvas('N' , stroke)
        if st.button('Capture N') : save_canvas(canvas_n , username , 'N')

        canvas_o = get_canvas('O' , stroke)
        if st.button('Capture O') : save_canvas(canvas_o , username , 'O')

        canvas_p = get_canvas('P' , stroke)
        if st.button('Capture P') : save_canvas(canvas_p , username , 'P')

        canvas_q = get_canvas('Q' , stroke)
        if st.button('Capture Q') : save_canvas(canvas_q , username , 'Q')

        canvas_r = get_canvas('R' , stroke)
        if st.button('Capture R') : save_canvas(canvas_r , username , 'R')

        canvas_s = get_canvas('S' , stroke)
        if st.button('Capture S') : save_canvas(canvas_s , username , 'S')

        canvas_t = get_canvas('T' , stroke)
        if st.button('Capture T') : save_canvas(canvas_t , username , 'T')

        canvas_u = get_canvas('U' , stroke)
        if st.button('Capture U') : save_canvas(canvas_u , username , 'U')

        canvas_v = get_canvas('V' , stroke)
        if st.button('Capture V') : save_canvas(canvas_v , username , 'V')

        canvas_w = get_canvas('W' , stroke)
        if st.button('Capture W') : save_canvas(canvas_w , username , 'W')

        canvas_x = get_canvas('X' , stroke)
        if st.button('Capture X') : save_canvas(canvas_x , username , 'X')

        canvas_y = get_canvas('Y' , stroke)
        if st.button('Capture Y') : save_canvas(canvas_y , username , 'Y')

        canvas_z = get_canvas('Z' , stroke)
        if st.button('Capture Z') : save_canvas(canvas_z , username , 'Z')

        if st.sidebar.button('Submit') : 

            count = 0
            total_scores = 0

            mades , scors ,  preds = predict(username)                
            col_1 , col_2 , col_3 = st.columns(3)

            for made in mades : col_1.image(made)
            for scor in scors :

                score = np.argmax(softmax(scor[0]))

                if score == count : 
                    sc = 1
                    total_scores += sc
                else : sc = 0

                col_2.write(f'You got Score : {sc}')
                col_2.write('\n')
                col_2.write('\n')
                col_2.write('\n')
                col_2.write('\n')
                col_2.write('\n')
                col_2.write('\n')
                col_2.write('\n')
                col_2.write('\n')
                col_2.write('\n')
                col_2.write('\n')
                col_2.write('\n')
            for pred in preds : col_3.image(pred)

        st.sidebar.write(f'Your total score was : {total_scores}')



users = [
    'Ervin' , 
    'Ayush'
]
username = st.selectbox('Choose the User' , users)
options = st.sidebar.selectbox(
    'NAV' , options = [
        'Home' , 
        'Predictions' , 
        'User' 
    ])

def get_image_path(key) : 

    return format_path(
        f'''
        Assets/ 
            Images/
                {key}.png
        '''
    )


stoi = {
    'a' : Image.open(get_image_path('A')) , 
    'b' : Image.open(get_image_path('B')) ,
    'c' : Image.open(get_image_path('C')) ,
    'd' : Image.open(get_image_path('D')) ,
    'e' : Image.open(get_image_path('E')) ,
    'f' : Image.open(get_image_path('F')) ,
    'g' : Image.open(get_image_path('G')) ,
    'h' : Image.open(get_image_path('H')) ,
    'i' : Image.open(get_image_path('I')) ,
    'j' : Image.open(get_image_path('J')) ,
    'k' : Image.open(get_image_path('K')) ,
    'l' : Image.open(get_image_path('L')) ,
    'm' : Image.open(get_image_path('M')) ,
    'n' : Image.open(get_image_path('N')) ,
    'o' : Image.open(get_image_path('O')) ,
    'p' : Image.open(get_image_path('P')) ,
    'q' : Image.open(get_image_path('Q')) ,
    'r' : Image.open(get_image_path('R')) ,
    's' : Image.open(get_image_path('S')) ,
    't' : Image.open(get_image_path('T')) ,
    'u' : Image.open(get_image_path('U')) ,
    'v' : Image.open(get_image_path('V')) ,
    'w' : Image.open(get_image_path('W')) ,
    'x' : Image.open(get_image_path('X')) ,
    'y' : Image.open(get_image_path('Y')) ,
    'z' : Image.open(get_image_path('Z'))}

if options == 'Predictions' : predictions()
elif options == 'User' : user()