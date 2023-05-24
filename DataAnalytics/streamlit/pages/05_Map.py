##################################################################################################
#################################   Start of Importing Section   #################################
import streamlit as st
import pandas as pd
import mysql.connector
import folium
from streamlit_folium import folium_static



##################################   End of Importing Section   ##################################
##################################################################################################

# TO RUN STREAMLIT IN LOCAL SERVER WRITE THIS IN YOUR COMMAND LINE:

# $ streamlit run introduction.py


##################################################################################################
###################    Retrieving the information from the database from AWS   ###################


# Information of the AMAZON REDSHIFT database.
host = "database-alertas-sismicas.crcnepco0igw.us-east-1.rds.amazonaws.com"
user = "admin"
password = "admin4168"
database = "alertasSismicas"

# Opening the connection to the database
connection = mysql.connector.connect(
    host = host,
    user = user,
    password = password,
    database = database
)

# SELECTING the table "FACTS" and giving the info to a pandas data frame
query = ("SELECT * FROM FACTS2;")
# query = ("SELECT * FROM FACTS;")
facts = pd.read_sql(query, connection)

# Closing the connection with the database
connection.close()


#############################    Closing connection with database   ##############################
##################################################################################################





##################################################################################################
##################################   Start of STREAMLIT CODE   ###################################

st.markdown('<p class = "title_1">Test</p>', unsafe_allow_html=True)
st.markdown("***")




# ================================================================
# 05 - Creating TEST Map
# ================================================================
st.markdown("***")
st.markdown('<div class="block_intro"><p class="text">The second graph, titled "Seismic Magnitude-Time Distribution", depicts the relationship between seismic magnitude and time for three countries: Japan, Chile, and the United States. This metric helps identify temporal trends and changes in seismic magnitudes over the specified time period, providing valuable insights into the overall seismic activity and potential risks within each country or region.<br><br> Understanding the magnitude-time distribution is crucial for seismic forecasting, hazard assessment, and preparedness efforts. By visualizing the variations in seismic magnitudes over time, this graph provides a broader perspective on the temporal behavior of seismic activity in Japan, Chile, and the United States. It aids in identifying potential patterns, trends, or anomalies that can contribute to a better understanding of the seismic activity and inform risk mitigation strategies.<br><br> Please have in mind that the IDs for the countries are:<br> USA[1] - Japan[2] - Chile[3]</p></div>', unsafe_allow_html=True)


# Changing numbers to the actual country name.
facts['idcountry'] = facts['idcountry'].replace(1, "USA")
facts['idcountry'] = facts['idcountry'].replace(2, "Japan")
facts['idcountry'] = facts['idcountry'].replace(3, "Chile")

# facts['lon'] = facts['lng'].rename("lon")

df = pd.DataFrame(facts, columns=['idcountry', 'time', 'lng', 'lat', 'danger'])
df_map = pd.DataFrame(df, columns=['lat', 'lon'])
st.map(df)

# Set up Streamlit
st.title("Earthquake Events Map")


###################################   End of STREAMLIT CODE   ####################################
##################################################################################################





##################################################################################################
#####################################    Start "CSS" Code   ######################################

st.markdown(""" <style>
.title_1 {
font-size:50px;
color: #92B8FF;
font-weight: bold;
}

.title_2 {
font-size:30px;
color: #92B8FF;
margin: 8px;
font-weight: bold;

}

.title_3 {
font-size:22px;
color: #92B8FF;
font-weight: bold;
}

.text {
font-size:16px;
color: #92B8FF;
}

.block_intro {
background-color: #003B8E;
border: 2px solid #92B8FF;
border-radius: 5px;
padding: 15px;
}

.block_kpis {
background-color: #003B8E;
border: 2px solid #92B8FF;
border-radius: 5px;
padding: 15px;
margin: 8px;
height: 350px;
}
</style> """, unsafe_allow_html=True)

######################################    End "CSS" Code   #######################################
##################################################################################################