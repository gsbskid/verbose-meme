import streamlit as st 

import base64
import json
import os
import re
import time
import uuid
from io import BytesIO
from pathlib import Path
from PIL import Image

# import keras
import cv2

import numpy as np
import pandas as pd
import streamlit as st
from streamlit_drawable_canvas import st_canvas
from svgpathtools import parse_path

# from keras.models import load_model

import os 



canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=3,
    stroke_color= '#000000',
    background_color='#EEEEEE',
    background_image= None,
    update_streamlit=True,
    height=150,
    drawing_mode='freedraw',
    point_display_radius=0 ,
    display_toolbar=False,
    key="full_app",
)

# Do something interesting with the image data and paths
if canvas_result.image_data is not None:
    st.image(canvas_result.image_data)
