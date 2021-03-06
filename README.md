# ๐ฆ  allocine_scrapping_data
## ๐ Description
AlloCinรฉ is an information company on French cinema and reviews of the press and its users for a large number of films. In this code we offer the possibility to scrap all information about movies

## ๐๏ธ The Visualization Data
๐๐๐ **Update** : the link to visualize analysis of data from allocinรฉ is available [here](https://share.streamlit.io/amoungui/allocine_visualization_data/app.py)

๐๐๐ **Update** : source code of data visualization using streamlit is available [here](https://github.com/amoungui/allocine_visualization_data)

### ๐ Description of the data
We provide the dataset in csv version (brut and clean versions) : [allocine_movies_brute.csv](https://samoungui.com/wp-content/uploads/2022/01/allocine_movies_brute.csv)

#### โน๏ธ The Columns :
- `title` : the movies title (in french)
- `release_year`: the original release date
- `re_release_date`: the re-release date
- `duration`: the movies length
- `genres` : the movies types (as an array, up to three different types)
- `directors` : movies directors (as an array)
- `actors` : main movie characters (as an array)
- `nationality`: nationality of the movies (as an array)
- `press_rating`: press ratings (from 0 to 5 stars)
- `nb_press_vote`: number of press votes
- `spec_rating`:  AlloCinรฉ users ratings (from 0 to 5 stars)
- `nb_user_vote`: number of users votes

### ๐ Getting Started

 streamlit run app.py
