# CHAT-GPT-PLUGIN-FOR-GDELT
This plugin can access data(Articles) from GDELT based on keywords  given as input. This description is mentioned inside the JSON File.
This can be hosted on a server by adding the URL details:-
     1. IN OPENAPI.YAML =>url
     2. IN AI.PLUGIN.JSON =>url
     3. IN MAIN.PY => (In Hashtag(#) line )
I used (GDELT BASE API) Mentioned in the (MAIN.PY) File as (base_url).

Finally, for connection  with ChatGpt,  we have to use the Url from (openAPI.yaml) file and paste it into the ChatGpt Plugin builder.
Note:- How can you run the application locally? 

Go to:- https://textkeywordchatgptplugin.naveenjakhad1.repl.co/gdelt_search
gdelt_search end point leads to default keyword (china) results 

In case to  search for any  other keyword format the URL:-  https://textkeywordchatgptplugin.naveenjakhad1.repl.co/gdelt_search?keyword=your_keyword
