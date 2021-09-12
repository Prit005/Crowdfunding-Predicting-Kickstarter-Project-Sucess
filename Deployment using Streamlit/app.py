#%%writefile app.py
import pickle
import re
import streamlit as st
import nltk
nltk.download('punkt')

# Load trained model
pickle_in = open("gbdt_best_.pkl", 'rb')
classifier = pickle.load(pickle_in)


@st.cache()
# convert sentence to word contain special characters.
def sentence_to_word(x):
    x = re.sub("[^A-Za-z0-9]", " ", x)
    words = nltk.word_tokenize(x)
    return words

cat = ["Product Design", "Documentary" ,"Music" ,"Tabletop Games" ,"Shorts" ,"Video Games" ,"Food" ,"Film & Video" ,"Fiction" ,"Fashion",
                                                     "Nonfiction" ,"Art" ,"Apparel" ,"Theater" ,"Technology" ,"Rock" ,"Children's Books" ,"Apps" ,"Publishing" ,"Webseries" ,"Photography" ,"Indie Rock",
                                                     "Narrative Film" ,"Web" ,"Comics" ,"Crafts" ,"Country & Folk" ,"Design" ,"Hip-Hop" ,"Hardware" ,"Pop" ,"Painting" ,"Games" ,"Illustration" ,"Accessories",
                                                     "Public Art" ,"Software" ,"Gadgets" ,"Restaurants" ,"Mixed Media" ,"Comic Books" ,"Art Books" ,"Classical Music" ,"Animation" ,"Playing Cards" ,"Drinks",
                                                     "Dance" ,"Comedy" ,"Drama" ,"Electronic Music" ,"Performance Art" ,"World Music" ,"Graphic Design" ,"Graphic Novels" ,"Jazz" ,"Sculpture" ,"Small Batch",
                                                     "Mobile Games" ,"Food Trucks" ,"Journalism" ,"Photobooks" ,"Plays" ,"Poetry" ,"Digital Art" ,"Horror" ,"Periodicals" ,"Jewelry" ,"Wearables" ,"DIY",
                                                     "Woodworking" ,"Farms" ,"People" ,"Faith" ,"Live Games" ,"Conceptual Art" ,"Television" ,"Performances" ,"Footwear" ,"Experimental" ,"Radio & Podcasts",
                                                     "Academic" ,"Musical" ,"DIY Electronics" ,"Ready-to-wear" ,"Spaces" ,"Festivals" ,"Young Adult" ,"Events" ,"Anthologies" ,"Fine Art" ,"Architecture" ,"Thrillers",
                                                     "Science Fiction" ,"Action" ,"Places" ,"Print" ,"Metal" ,"Music Videos" ,"3D Printing" ,"Sound" ,"Webcomics", "Vegan" ,"Nature" ,"Robots" ,"Cookbooks" ,"Childrenswear",
                                                     "Installations" ,"R&B" ,"Candles" ,"Gaming Hardware" ,"Video" ,"Flight" ,"Farmer's Markets" ,"Camera Equipment" ,"Audio" ,"Interactive Design" ,"Zines" ,"Fantasy",
                                                     "Family" ,"Immersive" ,"Calendars" ,"Space Exploration" ,"Punk" ,"Ceramics" ,"Community Gardens" ,"Civic Design" ,"Kids" ,"Literary Journals" ,"Textiles" ,"Couture",
                                                     "Blues" ,"Animals" ,"Fabrication Tools" ,"Printing" ,"Makerspaces" ,"Movie Theaters" ,"Puzzles" ,"Bacon" ,"Stationery" ,"Photo" ,"Video Art" ,"Romance" ,"Knitting",
                                                     "Workshops" ,"Crochet" ,"Translations" ,"Pet Fashion" ,"Glass" ,"Latin" ,"Embroidery" ,"Typography" ,"Pottery" ,"Weaving" ,"Quilts" ,"Residencies" ,"Letterpress",
                                                     "Chiptune" ,"Literary Spaces" ,"Taxidermy"]
numcat = [113,39,136,90,129,148,58,55,54,52,95,10,7,141,138,125,19,8,153,104,72,115,93,151,26,32,30,37,68,67,109,96,62,70,2,114,131,61,123,87,25,11,23,5,106,41,36,24,
          42,98,40,156,65,66,75,128,130,88,77,59,103,107,108,38,69,100,76,149,154,34,51,97,47,84,28,99,139,60,120,45,92,1,35,121,53,134,44,157,6,56,9,127,105,142,3,
          111,86,91,0,132,152,145,94,124,29,20,73,119,17,146,63,57,50,16,12,74,158,49,48,71,15,133,116,18,27,22,78,140,82,31,14,4,46,85,112,89,117,13,135,102,147,126,
          79,33,155,143,101,64,80,43,144,110,150,118,122,81,21,83,137]
catlen = len(numcat)
maincat = ['Film & Video', 'Music', 'Publishing', 'Games', 'Technology', 'Design', 'Art', 'Food', 'Fashion',
           'Theater', 'Comics', 'Photography', 'Crafts', 'Journalism','Dance']
maincatnum = [6.0, 10.0, 12.0, 8.0, 13.0, 4.0, 0.0, 7.0, 5.0, 14.0, 1.0, 11.0, 2.0, 9.0, 3.0]
maincatlen = len(maincat)

countryL = ['US', 'GB', 'CA', 'AU', 'DE', 'N,0"', 'FR', 'IT', 'NL', 'ES', 'SE',
            'MX', 'NZ', 'DK', 'IE', 'CH', 'NO', 'HK', 'BE', 'AT', 'SG', 'LU']
numcount = [21, 9, 3, 1, 5, 8, 16, 12, 7, 19, 15, 18, 6, 11, 4, 17, 2, 10, 0, 20, 14, 13]
countlen = len(countryL)

currenc = ['USD', 'GBP', 'EUR', 'CAD', 'AUD', 'SEK', 'MXN', 'NZD', 'DKK', 'CHF', 'NOK', 'HKD', 'SGD', 'JPY']
numcurren = [13, 5, 4, 1, 0, 11, 8, 10, 3, 2, 9, 6, 12, 7]
currenlen = len(currenc)


# convert whole essay to word list
def essay_to_word(essay):
    essay = essay.strip()
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    raw = tokenizer.tokenize(essay)
    final_words = []
    for i in raw:
        if (len(i) > 0):
            final_words.append(sentence_to_word(i))
    return final_words


# Calculate number of words in essay
def number_Of_Words(essay):
    count = 0
    for i in essay_to_word(essay):
        count += len(i)
    return count


# calculate number of character in essay
def number_Of_Char(essay):
    count = 0
    for i in essay_to_word(essay):
        for j in i:
            count += len(j)
    return count


# calculate average of words in essay
def avg_word_len(essay):
    return number_Of_Char(essay) / number_Of_Words(essay)


def prediction(category,main_category,currency,goal,pledged,backers,country,usd_pledged,usd_pledged_real,
               usd_goal_real,dead_year,dead_hour,dead_minute,dead_day,dead_month,launch_hour, launch_minute,
               launch_day,launch_month,launch_year,duration,name):

    name_char_count = number_Of_Char(name)
    name_word_count = number_Of_Words(name)
    name_avg_word_len = avg_word_len(name)
    for i in range(catlen):
        if category == cat[i]:
            category = numcat[i]

    for i in range(maincatlen):
        if main_category == maincat[i]:
            main_category = maincatnum[i]

    for i in range(countlen):
        if country == countryL[i]:
            country = numcount[i]

    for i in range(currenlen):
        if currency == currenc[i]:
            currency = numcurren[i]

    predicted = classifier.predict([[category,main_category,currency,goal,pledged,
                                      backers,country,usd_pledged,usd_pledged_real,
                                      usd_goal_real,dead_year,dead_hour,dead_minute,dead_day,
                                      dead_month,launch_hour, launch_minute, launch_day,launch_month,launch_year,
                                      duration,name_char_count, name_word_count, name_avg_word_len]])
    if predicted == 1:
        pred = "Succeed"
    else:
        pred = "Not succeed"
    return pred


# Main function:
def main():
    # Front end Elements:
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:aqua;text-align:center;">Kickstarter Project Success Prediction ML App</h1>
    </div>
    """
    # Display aspect of front end
    st.markdown(html_temp, unsafe_allow_html=True)
    name = st.text_input("Name of Project")
    category = st.selectbox('Project sub-category',( "Product Design" ,"Documentary" ,"Music" ,"Tabletop Games" ,"Shorts" ,"Video Games" ,"Food" ,"Film & Video" ,"Fiction" ,"Fashion",
                                                     "Nonfiction" ,"Art" ,"Apparel" ,"Theater" ,"Technology" ,"Rock" ,"Children's Books" ,"Apps" ,"Publishing" ,"Webseries" ,"Photography" ,"Indie Rock",
                                                     "Narrative Film" ,"Web" ,"Comics" ,"Crafts" ,"Country & Folk" ,"Design" ,"Hip-Hop" ,"Hardware" ,"Pop" ,"Painting" ,"Games" ,"Illustration" ,"Accessories",
                                                     "Public Art" ,"Software" ,"Gadgets" ,"Restaurants" ,"Mixed Media" ,"Comic Books" ,"Art Books" ,"Classical Music" ,"Animation" ,"Playing Cards" ,"Drinks",
                                                     "Dance" ,"Comedy" ,"Drama" ,"Electronic Music" ,"Performance Art" ,"World Music" ,"Graphic Design" ,"Graphic Novels" ,"Jazz" ,"Sculpture" ,"Small Batch",
                                                     "Mobile Games" ,"Food Trucks" ,"Journalism" ,"Photobooks" ,"Plays" ,"Poetry" ,"Digital Art" ,"Horror" ,"Periodicals" ,"Jewelry" ,"Wearables" ,"DIY",
                                                     "Woodworking" ,"Farms" ,"People" ,"Faith" ,"Live Games" ,"Conceptual Art" ,"Television" ,"Performances" ,"Footwear" ,"Experimental" ,"Radio & Podcasts",
                                                     "Academic" ,"Musical" ,"DIY Electronics" ,"Ready-to-wear" ,"Spaces" ,"Festivals" ,"Young Adult" ,"Events" ,"Anthologies" ,"Fine Art" ,"Architecture" ,"Thrillers",
                                                     "Science Fiction" ,"Action" ,"Places" ,"Print" ,"Metal" ,"Music Videos" ,"3D Printing" ,"Sound" ,"Webcomics", "Vegan" ,"Nature" ,"Robots" ,"Cookbooks" ,"Childrenswear",
                                                     "Installations" ,"R&B" ,"Candles" ,"Gaming Hardware" ,"Video" ,"Flight" ,"Farmer's Markets" ,"Camera Equipment" ,"Audio" ,"Interactive Design" ,"Zines" ,"Fantasy",
                                                     "Family" ,"Immersive" ,"Calendars" ,"Space Exploration" ,"Punk" ,"Ceramics" ,"Community Gardens" ,"Civic Design" ,"Kids" ,"Literary Journals" ,"Textiles" ,"Couture",
                                                     "Blues" ,"Animals" ,"Fabrication Tools" ,"Printing" ,"Makerspaces" ,"Movie Theaters" ,"Puzzles" ,"Bacon" ,"Stationery" ,"Photo" ,"Video Art" ,"Romance" ,"Knitting",
                                                     "Workshops" ,"Crochet" ,"Translations" ,"Pet Fashion" ,"Glass" ,"Latin" ,"Embroidery" ,"Typography" ,"Pottery" ,"Weaving" ,"Quilts" ,"Residencies" ,"Letterpress",
                                                     "Chiptune" ,"Literary Spaces" ,"Taxidermy"))
    main_category = st.selectbox("Project Main Category", ('Film & Video', 'Music', 'Publishing', 'Games', 'Technology', 'Design', 'Art', 'Food', 'Fashion',
                                                           'Theater', 'Comics', 'Photography', 'Crafts', 'Journalism','Dance'))
    currency = st.selectbox("Select Currency", ('USD', 'GBP', 'EUR', 'CAD', 'AUD', 'SEK', 'MXN', 'NZD',
                                                'DKK', 'CHF', 'NOK', 'HKD', 'SGD', 'JPY'))
    goal = st.number_input("Ideal Goal Amount")
    pledged = st.number_input("Ideal Pledged Amount")
    backers = st.number_input("Number of Backers")
    country = st.selectbox("Select Country", ('US', 'GB', 'CA', 'AU', 'DE', 'N,0"', 'FR', 'IT', 'NL', 'ES', 'SE',
                                              'MX', 'NZ', 'DK', 'IE', 'CH', 'NO', 'HK', 'BE', 'AT', 'SG', 'LU'))
    usd_pledged = st.number_input("Amount pledged in USD")
    usd_pledged_real = st.number_input("Real amount pledged in USD")
    usd_goal_real = st.number_input("Real Goal amount in USD")
    st.markdown("""
                <div>
                <h4 style ="color:green;text-align:left;">Deadline Date</h4>
                </div>"""
                , unsafe_allow_html=True)
    dead_year = st.number_input("Deadline Year")
    dead_month = st.number_input("Deadline Month")
    dead_day = st.number_input("Deadline Day")
    dead_hour = st.number_input("Deadine Hour")
    dead_minute = st.number_input("Deadline Minute")
    st.markdown("""
                    <div>
                    <h4 style ="color:green;text-align:left;">Launch Date</h4>
                    </div>"""
                , unsafe_allow_html=True)
    launch_year = st.number_input("Launch Year")
    launch_month = st.number_input("Launch Month")
    launch_day = st.number_input("Launch Day")
    launch_hour = st.number_input("Launch Hour")
    launch_minute = st.number_input("Launch Minute")
    duration = st.number_input("Project Duration")

    # When Predict is clicked:
    if st.button("Predict"):
        result = prediction(category,main_category,currency,goal,pledged,backers,country,usd_pledged,usd_pledged_real,
               usd_goal_real,dead_year,dead_hour,dead_minute,dead_day,dead_month,launch_hour, launch_minute,
               launch_day,launch_month,launch_year,duration,name)
        st.success(f"Your Project will {result}")


if __name__ == '__main__':
    main()
