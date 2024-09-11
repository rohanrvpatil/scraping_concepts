Site used: https://www.petsathome.com/
YouTube link: https://www.youtube.com/watch?v=tuf9KoZ6JyI

Implementation steps:
1) Visited the website: https://www.petsathome.com/ and pressed F12
2) Clicked on Fetch/XHR in Network Tab
3) Typed "dog" in the search box of the website and clicked on Search
4) Right clicked on the request and copied the cURL (as bash)
5) Visited curl convertor website and pasted the curl command and generated the python code
6) Copied the code in the project and generated the response json
7) Converted the json into a xlsx file

Tips:
1) Experiment with limit, start with limit=100 and go higher
2) yielding is a good way to avoid lists of lists
3) To get params, visit Fetch/XHR in Network Tab. The URL with params will appear after the Search button(if available on the site) has been clicked
4) Use https://curlconverter.com/ to generate the code from cURL command
5) Use Postman to analyse response, headers and save the POST, GET requests for future reference

