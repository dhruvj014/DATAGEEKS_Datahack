import streamlit as st
import numpy as np
import xgboost
import pickle
from  PIL import Image, ImageEnhance
import requests
import urllib.request
from streamlit_option_menu import option_menu

st.markdown(
"""
<style>
:root {
    --primary-color: black;
    }
body{
    background-color: #c9e9f6;
    font-color: black;
    font-size: 40px;
}

.stButton>button{
    background-color: #f4f0db;
    width: 205.383px;
    height: 60px;
    color: white;
    box-sizing: 5%;
    font-size:50px;
    border: 5px solid;
    border-radius: 5px;
    padding: 10px;
    border-bottom-color: black;
    border-left-color: black;
    border-right-color: black;
    border-top-color: black;
}
.stButton>button:hover {
    padding: 15px;
    border: 4px solid;
    background-color: #f4f0db;
    border-bottom-color: grey;
    border-left-color: grey;
    border-right-color: grey;
    border-top-color: grey;
    color: white;
}

.center{
    display: block;
    margin-left: auto;
    margin-right: auto;
  }

div[role="listbox"]{
    background-color: blue;
}

div[class="css-5uatcg edgvbvh10"]{
    background-color:black;
}

div[class="css-zt5igj e16nr0p33"]{
    color:black;
}
div[class="css-1yy6isu e16nr0p34"]{
    color:black;
}
div[class="nav-item"]{
        color:black;
}

div[class="css-183lzff eyqtai90"]{
    color:black;
}

div[class="css-1fv8s86 e16nr0p34"]{
    color:black;
}


div[class="css-6qob1r e1fqkh3o3"]{
    background-color: #f4f0db;
}

div[class="appview-container css-1wrcr25 egzxvld6"]{
        background-color: #ecd9ba;
}

</style>
""",
    unsafe_allow_html = True
    )
with st.sidebar:
    selected = option_menu(
        menu_title = 'Main Menu',
        options = ['HomePage','Car Prediction','Team Github'],
        icons = ['house','graph-up-arrow','github'],
        menu_icon = 'list',
        default_index = 0,
        # orientation = 'horizontal'
        )

df = pickle.load(open('df.pkl','rb'))
pipe = pickle.load(open('pipe.pkl','rb'))

if selected == 'HomePage':
    st.title('Lets see a few Visualisations on the dataset - ')
    if st.button('Price Analysis'):
        url1 = 'https://raw.githubusercontent.com/dhruvj014/dhruvj014/main/picsmisc/out.png'
        f = open('onlinepic1.jpg','wb')
        f.write(requests.get(url1).content)
        f.close()
        url2 = 'https://raw.githubusercontent.com/dhruvj014/dhruvj014/main/picsmisc/out1.png'
        f = open('onlinepic2.jpg','wb')
        f.write(requests.get(url2).content)
        f.close()
        new_image = Image.open('onlinepic1.jpg')
        st.image(new_image)
        st.write('The graph is very clearly skewed. Let us visualized an exponential form of the graph.')
        new_image1 = Image.open('onlinepic2.jpg')
        st.image(new_image1)
        st.write('The graph is now normalized and evenly spread throughout.')

    if st.button('Brand vs Price Analysis'):
        url1 = 'https://raw.githubusercontent.com/dhruvj014/dhruvj014/main/picsmisc/out6.png'
        f = open('onlinepic1.jpg','wb')
        f.write(requests.get(url1).content)
        f.close()
        new_image = Image.open('onlinepic1.jpg')
        st.image(new_image)
        st.write('From the graph we can clearly see that BMW, Land Rover and Mercedes-Benz are the most expensive resale cars.')
        st.write('Porsche, Audi and Jaguar are slightly less expensive resale cars than the former 3.')

    if st.button('Age of Car vs Price Analysis'):
        url1 = 'https://raw.githubusercontent.com/dhruvj014/dhruvj014/main/picsmisc/out3.png'
        f = open('onlinepic1.jpg','wb')
        f.write(requests.get(url1).content)
        f.close()
        new_image = Image.open('onlinepic1.jpg')
        st.image(new_image)
        st.write('As expected, the price of a car falls as it gets older.')
        st.write('However an interesting point is that around the 20 year mark, the vehicle probably becomes Vintage as its price increases slightly for 2-3 years.')

    if st.button('Brand Analysis'):
        url1 = 'https://raw.githubusercontent.com/dhruvj014/dhruvj014/main/picsmisc/out4.png'
        f = open('onlinepic1.jpg','wb')
        f.write(requests.get(url1).content)
        f.close()
        new_image = Image.open('onlinepic1.jpg')
        st.image(new_image)
        st.write('From the graph we can see that Maruti, Hyundai and Honda are the most resold cars.')
        st.write('Unsurprisngly, due to their high costs, Porsche, Land Rover and Jaguar are comparatively rarely resold.(check Brand vs Price Analysis)')

    if st.button('Brand vs Age of Car Analysis'):
        url1 = 'https://raw.githubusercontent.com/dhruvj014/dhruvj014/main/picsmisc/out5.png'
        f = open('onlinepic1.jpg','wb')
        f.write(requests.get(url1).content)
        f.close()
        new_image = Image.open('onlinepic1.jpg')
        st.image(new_image)
        st.write('From the graph, we can see that Maruti, Honda and Mahindra\'s cars sold are the oldest.')
        st.write('This is also probaby why their cars are the most resold.')

    if st.button('Fuel Source Analysis'):
        url1 = 'https://raw.githubusercontent.com/dhruvj014/dhruvj014/main/picsmisc/out7.png'
        f = open('onlinepic1.jpg','wb')
        f.write(requests.get(url1).content)
        f.close()
        new_image = Image.open('onlinepic1.jpg')
        st.image(new_image)
        st.write('More than half the cars resold are Diesel cars. A very big portion of the remaining vehicles are Petrol Cars.')
        st.write('The number of cars of LPG and CNG that are resold is very small compared to Petrol and Diesel.')

    if st.button('Gear Analysis'):
        url1 = 'https://raw.githubusercontent.com/dhruvj014/dhruvj014/main/picsmisc/out8.png'
        f = open('onlinepic1.jpg','wb')
        f.write(requests.get(url1).content)
        f.close()
        new_image = Image.open('onlinepic1.jpg')
        st.image(new_image)
        st.write('Almost 75% of the cars resold are Manual Gear Shift Vehicles.')

    if st.button('Car Ownership Analysis'):
        url1 = 'https://raw.githubusercontent.com/dhruvj014/dhruvj014/main/picsmisc/out9.png'
        f = open('onlinepic1.jpg','wb')
        f.write(requests.get(url1).content)
        f.close()
        new_image = Image.open('onlinepic1.jpg')
        st.image(new_image)
        st.write('More than 80% of the cars are 1st owner vehicles. Of the remaining 20%, 16% are second owner resellers.')
        st.write('The number of third and higher owners selling is pretty small.')

    if st.button('Mileage vs Price Analysis'):
        url1 = 'https://raw.githubusercontent.com/dhruvj014/dhruvj014/main/picsmisc/out10.png'
        f = open('onlinepic1.jpg','wb')
        f.write(requests.get(url1).content)
        f.close()
        new_image = Image.open('onlinepic1.jpg')
        st.image(new_image)
        st.write('From the scatter plot we can see that majority of the cars have Mileage betwen 10 and 25.')

    if st.button('Price with Count Analysis'):
        url1 = 'https://raw.githubusercontent.com/dhruvj014/dhruvj014/main/picsmisc/out11.png'
        f = open('onlinepic1.jpg','wb')
        f.write(requests.get(url1).content)
        f.close()
        new_image = Image.open('onlinepic1.jpg')
        st.image(new_image)
        st.write('90% of the Cars are between 0 and 20 Lacs.')
        st.write('Very few cars are more expensive than 50 Lacs')

    if st.button('Engine vs Price Analysis'):
        url1 = 'https://raw.githubusercontent.com/dhruvj014/dhruvj014/main/picsmisc/out12.png'
        f = open('onlinepic1.jpg','wb')
        f.write(requests.get(url1).content)
        f.close()
        new_image = Image.open('onlinepic1.jpg')
        st.image(new_image)
        st.write('Most of the Cars have Engine Capacity between 1000 CC and 3000 CC.')

    if st.button('Power vs Price Analysis'):
        url1 = 'https://raw.githubusercontent.com/dhruvj014/dhruvj014/main/picsmisc/out13.png'
        f = open('onlinepic1.jpg','wb')
        f.write(requests.get(url1).content)
        f.close()
        new_image = Image.open('onlinepic1.jpg')
        st.image(new_image)
        st.write('Most of the cars have Power value between 50 and 300.')
        st.write('The vehicles with Power Value between 300 to 400 are Premium Vehicles and are pretty expensive.')

    if st.button('Seats vs Price Analysis'):
        url1 = 'https://raw.githubusercontent.com/dhruvj014/dhruvj014/main/picsmisc/out14.png'
        f = open('onlinepic1.jpg','wb')
        f.write(requests.get(url1).content)
        f.close()
        new_image = Image.open('onlinepic1.jpg')
        st.image(new_image)
        st.write('All cars with 2 seats are Luxury Cars with rather high costs.')

if selected == 'Car Prediction':
    seats = df['Seats'].unique()
    seats.sort()

    st.title('Used Car Price Predictor')
    brand = st.selectbox('Car Brand',df['Car Brand'].unique())
    age = st.number_input('How old is the car?')
    location = st.selectbox('Where are you from?',df['Location'].unique())
    kms = st.number_input('How many KMs have you driven in the car?')
    fuel = st.selectbox('What does your car run on?',df['Fuel_Type'].unique())
    owner = st.selectbox('Which owner are you?',['First','Second','Third','Fourth or Above'])
    transm = st.selectbox('What kind of Transmission does your car have?',['Manual','Automatic'])
    mileage = st.number_input('What is the mileage of the car(in km/kg)?')
    engine = st.number_input('What is the Engine Capacity of the car(in CC)?')
    power = st.number_input('What is the power of the car(in bhw)?')
    seats = st.selectbox('How many seats does your car have?',seats)

    if st.button('Predict Price'):
        if owner == 'First':
            owner = 1
        if owner == 'Second':
            owner = 2
        if owner == 'Third':
            owner = 3
        if owner == 'Fourth or Above':
            owner = 4
        if transm == 'Manual':
            transm = 0
        if transm == 'Automatic':
            transm = 1
        # X_res = int(reso.split('x')[0])
        # Y_res = int(reso.split('x')[1])
        # ppi = ((X_res**2) + (Y_res**2))**0.5/scrsiz
        query = np.array([age,brand,location,kms,fuel,transm,owner,mileage,engine,power,seats], dtype=object)
        query = query.reshape(1,11)
        st.title("The predicted price of this configuration is " + str(np.exp(pipe.predict(query)[0]))+ " Lac Rupees")
if selected == 'Team Github':
    url = "https://github.com/dhruvj014/DATAGEEKS_Datahack"
    url2 = "https://raw.githubusercontent.com/dhruvj014/DATAGEEKS_Datahack/main/pics/Teampic.jpg"
    f = open('teampic.jpg','wb')
    f.write(requests.get(url2).content)
    f.close()
    new_image = Image.open('teampic.jpg')
    st.image(new_image)
    st.write("Thank you for giving us this opportunity to participate in this Hackathon.")
    st.write("You can check out our Github [here](%s)" % url)
