## What was the theme you chose?
The theme that I chose for this project is israeli food. This is because I was in 
Israel for a month over winter break.

## How did you pick your searches to fit the theme?
I queried my three favorite foods in israel through the "Search Recipies" endpoint then put all the 
ids in the "Get Recipies Information Bulk" endpoint to get the information. 

## What are at least 3 issues you encountered with your project? How did you fix them?
1. css and javascript were not being read<br />
  solution: cmd+shift+r which hard refreshed the page. then the changed showed up
  
2. Requests and requests_oauthlib were installed but the terminal said no module named requests_oauthlib found<br />
  solution: pip uninstalled the libraries and pip3 installed them
  
3. config vars wouldnt authenticate me.<br />
  solution: I removed the quotes from config vars

4. Odd index out of range error where index 1 had an error but not any index above or before it.<br />
  solution: I realized that the index was an outlier and the recipie had no steps or directions so I removed it.

## What are known problems, if any, with your project?
Forgot to remove 12.50 price in html.

## What would you do to improve your project in the future?
Add more pictures for the step by step directions.

### App Walkthough GIF

<img src="http://g.recordit.co/8BkYm1Y38d.gif" width=250><br>
