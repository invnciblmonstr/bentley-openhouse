import pandas as pd
import streamlit as st
from geopy.geocoders import Nominatim
from PIL import Image
from streamlit_folium import folium_static
import folium as folium
from better_profanity import profanity

if __name__ == "__main__":
    profanity.load_censor_words()
#     censored_text = profanity.censor(text)
#     print(censored_text)

    
    #Image
    image = Image.open("banner.png")
    image2 = Image.open("CISSandbox.png")
    
    st.image(image, use_column_width=True)
    #st.markdown("<img src=image; class='center'>", unsafe_allow_html=True)
    countries = ['', 'Afghanistan', 'Akrotiri', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Ashmore and Cartier Islands', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas, The', 'Bahrain', 'Bangladesh', 'Barbados', 'Bassas da India', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'British Virgin Islands', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burma', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Clipperton Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo, Democratic Republic of the', 'Congo, Republic of the', 'Cook Islands', 'Coral Sea Islands', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Dhekelia', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Europa Island', 'Falkland Islands (Islas Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern and Antarctic Lands', 'Gabon', 'Gambia, The', 'Gaza Strip', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Glorioso Islands', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Holy See (Vatican City)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Jan Mayen', 'Japan', 'Jersey', 'Jordan', 'Juan de Nova Island', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macau', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of', 'Moldova', 'Monaco', 'Mongolia', 'Montserrat', 'Morocco', 'Mozambique', 'Namibia', 'Nauru', 'Navassa Island', 'Nepal', 'Netherlands', 'Netherlands Antilles', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paracel Islands', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn Islands', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Reunion', 'Romania', 'Russia', 'Rwanda', 'Saint Helena', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia and Montenegro', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia and the South Sandwich Islands', 'Spain', 'Spratly Islands', 'Sri Lanka', 'Sudan', 'Suriname', 'Svalbard', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tromelin Island', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam', 'Virgin Islands', 'Wake Island', 'Wallis and Futuna', 'West Bank', 'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe']
    datafile = "file.csv"
    df = pd.read_csv(datafile)
    choices = ['The campus is beautiful!','I want to be in the Boston area','Bentley is the right size school for me','Bentley is #1 in Career Services','Bentley has lots of clubs and organizations',"I can't wait to try the food in the cafeteria",'Bentley is a diverse campus','Bentley offers study abroad' ,'Bentley is a leader in business education']
    st.markdown("<h1 style='text-align: center; color: #23395d ;'>Fill out the information on the form and press the submit button</h1>", unsafe_allow_html=True)
    #st.sidebar.text("Fill in the following information!")
    #st.markdown("<h1 style='text-align: center; color: blue;'>Fill in the information on the form to the right and press the submit button</h1>", unsafe_allow_html=True)
    
    name = st.text_input("Name")
    country = st.selectbox("Country", countries, index= 243)
    if country == 'United States' :
        state_options = ["","Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]
        state = st.selectbox("State",state_options)
    city = st.text_input("City")
    phrase = st.multiselect("Why do you want to come to Bentley? (Select multiple)", choices)
    
    
#     st.dataframe(df)
    l1 = df["Name"].tolist()
    l2 = df["ZIP"].tolist()
    l3 = df["City"].tolist()
    l4 = df["Phrase"].tolist()
    l5 = df['Lat'].tolist()
    l6 = df['Lon'].tolist()
    l7 = df['Country'].tolist()
    l8 = df['NP'].tolist()
    
    if name and country and city and phrase:
        geolocator = Nominatim(user_agent="Bentley")
        if country == 'United States' :
            location = geolocator.geocode(city+', '+state+', '+country)
        else :
            location = geolocator.geocode(city+', '+country)
        
        

        if st.button('Submit'):
            if profanity.contains_profanity(phrase) is False:
                if profanity.contains_profanity(name) is False:
                    l1.append(name)
                    l2.append(state)
                    l3.append(city)
                    l4.append(phrase)
                    l5.append(location.latitude)
                    l6.append(location.longitude)
                    l7.append(country)
                    l8.append(f"{name} says '{phrase}' &&")
    
    df = pd.DataFrame(data={"Name": l1,"ZIP" : l2,"City": l3, "Phrase": l4, "Lat" : l5, "Lon": l6, "Country": l7, "NP": l8})
    df.to_csv("./file.csv", sep=',',index=False)
    dict = df.groupby('City').agg({'NP':'sum', 'Lat':'mean','Lon':'mean'})
#                 st.dataframe(dict)

    st.header('See where the future Falcons :eagle: are from')
    map2 = folium.Map(location=[48, -102], zoom_start=1)
    
    
    for i in range(0,len(dict)):
        icon_url = 'bentleymapmarker.png'
        x = dict.iloc[i]['NP'].split('&&')
        html= f''' '''
        for j in x:
            html = html + j + "<br><br>"
        iframe = folium.IFrame(html = html, width=200, height=70)
        pop = folium.Popup(iframe)
        iconx = folium.features.CustomIcon(icon_url,icon_size=(25, 30))
        folium.Marker([dict.iloc[i]['Lat'], dict.iloc[i]['Lon']], popup= pop , icon = iconx, width=1200, height=500).add_to(map2)
    
    
    folium_static(map2)
    link = '[Undergraduate Admission - Virtual Academic Preview Day | Bentley University](https://www.bentley.edu/undergraduate/virtual-academic-preview-day)'
    st.markdown(link, unsafe_allow_html=True)
    link2 = '[CIS Sandbox | Bentley&#039;s Technology Social Learning Space](https://cis.bentley.edu/sandbox/)'
    st.markdown(link2, unsafe_allow_html=True)
    st.image(image2, use_column_width=False)
    
