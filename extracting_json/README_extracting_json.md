Site used: https://www.petsathome.com/

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
3) To get params, visit Fetch/XHR in Network Tab. The URL with params will appear after the Search button has
been clicked