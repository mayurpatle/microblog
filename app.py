import datetime
from flask import Flask , render_template  , request
from  pymongo import MongoClient  







app  =  Flask(__name__) 
client  =  MongoClient("mongodb://localhost:27017/")
app.db = client.Microblog

 

entries  =  []   


@app.route("/" , methods = ["GET"  , "POST"])
def Home():
    
    
    if request.method ==  "POST":
        entry_content  = request.form.get("content")
        format   =  datetime.datetime.today().strftime("%b -%d")
        entries.append((entry_content   , format))
        app.db.entries.insert_one({
            "content" : entry_content  , 
            "Date" :  format  
        })
        
        
        
    entries_with_date = [ 
                         ( entry[0]  ,  
                          entry[1]  , 
                          
                          
                          
                          )
                         
                         for  entry  in  entries 
                         
    ]
    return render_template("home.html"  ,   entries  = entries_with_date )

if __name__ == "__main__":
    app.run(debug=True)