## todos

* egal as answer in form
* cool title search
  * partial matches
* implement error handling
* implement unit-tests

## ideas
* find movie with mood
* add rating values: trash or top notch, super bewertet, schlecht bewertet, trash, shlefaz, preisgewinner, arthouse, pedagogisch wertfoll, oscar film, jugendfilm

# DBs
# Vector Search
https://github.com/facebookresearch/faiss

# Movies
https://www.omdbapi.com/
API Key [http://www.omdbapi.com/?i=tt3896198&apikey=792cc651](http://www.omdbapi.com/?i=tt3896198&apikey=792cc651)
792cc651
## Example Response
```json
{"Title":"GoldenEye","Year":"1995","Rated":"PG-13","Released":"17
 Nov 1995","Runtime":"130 min","Genre":"Action, Adventure, 
Thriller","Director":"Martin Campbell","Writer":"Ian Fleming, Michael 
France, Jeffrey Caine","Actors":"Pierce Brosnan, Sean Bean, Izabella 
Scorupco","Plot":"Years after a friend and fellow 00 agent is killed on a
 joint mission, a Russian crime syndicate steals a secret space-based 
weapons program known as \"GoldenEye\" and James Bond has to stop them 
from using it.","Language":"English, Russian, Spanish","Country":"United
 Kingdom, United States","Awards":"Nominated for 2 BAFTA 2 wins & 8 
nominations 
total","Poster":"https://m.media-amazon.com/images/M/MV5BOWI0MTJlMjEtYTI0ZS00NWZiLWE1ZmItYzBlZTE5YTk3NTJiXkEyXkFqcGdeQXVyMTEwNDU1MzEy._V1_SX300.jpg","Ratings":[{"Source":"Internet
 Movie Database","Value":"7.2/10"},{"Source":"Rotten 
Tomatoes","Value":"80%"},{"Source":"Metacritic","Value":"65/100"}],"Metascore":"65","imdbRating":"7.2","imdbVotes":"264,093","imdbID":"tt0113189","Type":"movie","DVD":"01
 Oct 
2016","BoxOffice":"$106,429,941","Production":"N/A","Website":"N/A","Response":"True"}
```

Chars to strip:
,
"
.
!
?

Chars to replace
& and

# What to embedd?
Title: GoldenEye
Year: 1995
Rated: PG-13
Released: 17 Nov 1995
Runtime: 130 min
Genre: Action, Adventure, Thriller
Director: Martin Campbell
Writer: Ian Fleming, Michael France, Jeffrey Caine
Actors: Pierce Brosnan, Sean Bean, Izabella Scorupco
Plot: When a deadly satellite weapon system falls into the wrong hands, only Agent James Bond 007 (Pierce Brosnan) can save the world from certain disaster. Armed with his licence to kill, Bond races to Russia in search of the stolen access codes for "GoldenEye", an awesome space weapon that can fire a devastating electromagnetic pulse toward Earth. But 007 is up against an enemy who anticipates his every move: a mastermind motivated by years of simmering hatred. Bond also squares off against Xenia Onatopp (Famke Janssen), an assassin who uses pleasure as her ultimate weapon.
Language: English, Russian, Spanish
Country: United Kingdom, United States
Awards: Nominated for 2 BAFTA 2 wins & 8 nominations total
Poster: https://m.media-amazon.com/images/M/MV5BOWI0MTJlMjEtYTI0ZS00NWZiLWE1ZmItYzBlZTE5YTk3NTJiXkEyXkFqcGdeQXVyMTEwNDU1MzEy._V1_SX300.jpg
Ratings: [{'Source': 'Internet Movie Database', 'Value': '7.2/10'}, {'Source': 'Rotten Tomatoes', 'Value': '80%'}, {'Source': 'Metacritic', 'Value': '65/100'}]
Metascore: 65
imdbRating: 7.2
imdbVotes: 264,093
imdbID: tt0113189
Type: movie
DVD: 01 Oct 2016
BoxOffice: $106,429,941
Production: N/A
Website: N/A
Response: True

| id  | title     | year | genre                       | rated | runtime | embedding                                 | director        | writer                                     | actors                                       | plot        | awards                                             | ratings                                                                                                                                                                                         | type  |
| --- | --------- | ---- | --------------------------- | ----- | ------- | ----------------------------------------- | --------------- | ------------------------------------------ | -------------------------------------------- | ----------- | -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| 10  | goldeneye | 1995 | Action, Adventure, Thriller | PG-13 | 130     | plot + genre + director + writer + actors | Martin Campbell | Ian Fleming, Michael France, Jeffrey Caine | Pierce Brosnan, Sean Bean, Izabella Scorupco | description | Nominated for 2 BAFTA 2 wins & 8 nominations total | 'Source': 'Internet Movie Database', 'Value': '7.2/10', 'Source': 'Rotten Tomatoes', 'Value': '80%', 'Source': 'Metacritic', 'Value': '65/100' Metascore: 65 imdbRating: 7.2	imdbVotes: 264,093 | movie |
