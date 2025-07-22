import streamlit as st
import pickle
import pandas as pd
import os

st.set_page_config(page_title="Cricket Score Predictor", layout="wide")

# Default Page
if 'page' not in st.session_state:
    st.session_state.page = 'home'


# Navigation Buttons
if st.session_state.page == 'home':
    # st.title('Cricket Score Predictor')

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.title(" 🏏 Cricket Score Predictor")

    # Create columns for side-by-side buttons
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("###")
        if st.button("🔹 T20_Predictor", use_container_width=True):
            st.session_state.page = 'T20_Predictor'
            st.rerun()

    with col2:
        st.markdown("###")
        if st.button("🔹 ODI_Predictor", use_container_width=True):
            st.session_state.page = 'ODI_Predictor'
            st.rerun()


elif st.session_state.page == 'T20_Predictor':
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.title(" 🏏 T20_Prediction")
    st.markdown("###")
    model_path = os.path.join(os.path.dirname(__file__), 'T20.pkl')
    pipe_1 = pickle.load(open(model_path, 'rb'))
    # pipe_1 = pickle.load(open('T20.pkl', 'rb'))

    teams = ['India', 'Bangladesh', 'Sri Lanka', 'West Indies', 'South Africa',
             'Pakistan', 'New Zealand', 'England', 'Australia']

    cities_1 = ['Centurion', 'Melbourne', 'Kolkata', 'Abu Dhabi', 'Mirpur',
                'Southampton', 'Christchurch', 'Johannesburg', 'Sydney', 'London',
                'Durban', 'Pallekele', 'Karachi', 'Rajkot', 'Colombo', 'Sylhet',
                'Bangalore', 'Hamilton', 'Mount Maunganui', 'Manchester', 'Lahore',
                'Gros Islet', 'Auckland', 'Kandy', 'Adelaide', 'Mumbai',
                'Chandigarh', 'Wellington', 'Barbados', 'Nottingham', 'Dubai',
                'Dambulla', 'Nagpur', 'Sharjah', 'St Lucia', 'Dhaka', 'Bridgetown',
                'Perth', 'Cape Town', 'Cardiff', 'Birmingham', 'Chittagong',
                'Providence', 'Trinidad', 'Brisbane', 'Kingston', 'Delhi',
                'Ahmedabad', "St George's", 'Lauderhill', 'Napier', 'Hobart',
                'Tarouba']

    col1, col2 = st.columns(2)

    with col1:
        batting_team = st.selectbox('Select batting team', sorted(teams))
    with col2:
        bowling_team = st.selectbox('Select bowling team', sorted(teams))

    city = st.selectbox('Select city', sorted(cities_1))

    col3, col4, col5 = st.columns(3)

    with col3:
        current_score = st.number_input('Current Score')
    with col4:
        overs = st.number_input('Overs done(works for over>5)')
    with col5:
        wickets = st.number_input('Wickets out')

    last_five = st.number_input('Runs scored in last 5 overs')

    if st.button('Predict Score'):
        balls_left = 120 - (overs * 6)
        wickets_left = 10 - wickets
        current_run_rate = current_score / overs

        input_df = pd.DataFrame(
            {'batting_team': [batting_team], 'bowling_team': [bowling_team], 'city': [city],
             'current_score': [current_score], 'balls_left': [balls_left], 'wickets_left': [wickets_left],
             'current_run_rate': [current_run_rate], 'last_five': [last_five]})
        result = pipe_1.predict(input_df)
        st.header("Predicted Score - " + str(int(result[0])))

    if st.button("Home"):
        st.session_state.page = 'home'
        st.rerun()

elif st.session_state.page == 'ODI_Predictor':
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.title(" 🏏 ODI_Prediction")
    st.markdown("###")
    pipe_2 = pickle.load(open('ODI.pkl', 'rb'))

    teams = ['India', 'Bangladesh', 'Sri Lanka', 'West Indies', 'South Africa',
             'Pakistan', 'New Zealand', 'England', 'Australia']

    cities_2 = ['Mirpur', 'Rangiri', 'Pallekele', 'Dhaka', 'Colombo', 'Ranchi',
                'Dubai', 'St Lucia', 'Adelaide', 'Leeds', 'Chester-le-Street',
                'Fatullah', 'Perth', 'Karachi', 'Barbados', 'Nottingham',
                'Chennai', 'Mumbai', 'Auckland', 'Melbourne', 'Port Elizabeth',
                'Cuttack', 'Johannesburg', 'Guwahati', 'Durban', 'Mount Maunganui',
                'Brisbane', 'Sydney', 'Antigua', 'Potchefstroom', 'Napier',
                'Centurion', 'Kochi', 'Rawalpindi', 'Hamilton', 'Delhi',
                'Cape Town', 'Chattogram', 'Lahore', 'Lucknow', 'Taunton',
                'Abu Dhabi', 'Gwalior', 'Rajkot', 'St Kitts', 'Birmingham',
                'East London', 'London', 'Hyderabad', 'Bridgetown', 'Kolkata',
                'Guyana', 'Paarl', 'Kanpur', 'Indore', 'Hobart', 'Cardiff',
                'Bloemfontein', 'Southampton', 'St Vincent', 'Jaipur',
                'Wellington', 'Kuala Lumpur', 'Jamaica', 'Nelson', 'Nagpur',
                'Dunedin', 'Hambantota', 'Bengaluru', 'Pune', 'Vadodara', 'Dublin',
                'Kandy', 'Kimberley', 'Ahmedabad', 'Port of Spain', 'Trinidad',
                'Cairns', 'Dambulla', 'Sharjah', 'Chittagong', 'Manchester',
                'Queenstown', 'Canberra', 'Dominica', 'Kingstown', 'Visakhapatnam',
                'Faisalabad', 'Benoni', 'Gqeberha', 'Grenada', 'North Sound',
                'Margao', 'Bangalore', 'Harare', 'Christchurch', 'Peshawar',
                'Darwin', 'Chandigarh', 'Multan', 'Bristol', 'Dharamsala',
                "St George's", 'Belfast', 'Providence', 'Bulawayo']

    col1, col2 = st.columns(2)

    with col1:
        batting_team = st.selectbox('Select batting team', sorted(teams))
    with col2:
        bowling_team = st.selectbox('Select bowling team', sorted(teams))

    city = st.selectbox('Select city', sorted(cities_2))

    col3, col4, col5 = st.columns(3)

    with col3:
        current_score = st.number_input('Current Score')
    with col4:
        overs = st.number_input('Overs done (works for over>10)')
    with col5:
        wickets = st.number_input('Wickets out')

    last_ten = st.number_input('Runs scored in last 10 overs')

    if st.button('Predict Score'):
        balls_left_2 = 300 - (overs * 6)
        wickets_left_2 = 10 - wickets
        current_run_rate_2 = current_score / overs

        input_df = pd.DataFrame(
            {'batting_team': [batting_team], 'bowling_team': [bowling_team], 'city': [city],
             'current_score': [current_score], 'balls_left': [balls_left_2], 'wickets_left': [wickets_left_2],
             'current_run_rate': [current_run_rate_2], 'last_ten': [last_ten]})
        result = pipe_2.predict(input_df)
        st.header("Predicted Score - " + str(int(result[0])))


    if st.button("Home"):
        st.session_state.page = 'home'
        st.rerun()
