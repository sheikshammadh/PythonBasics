from pymongo import MongoClient
cleint=MongoClient('mongodb://localhost:27017')
db=cleint['6pm']
user_col=db['users']
users=[{"id":1,"first_name":"Adelaide","gender":"Female"},
{"id":2,"first_name":"Rhona","gender":"Female"},
{"id":3,"first_name":"Cordey","gender":"Female"},
{"id":4,"first_name":"Erny","gender":"Male"},
{"id":5,"first_name":"Rodd","gender":"Male"},
{"id":6,"first_name":"Marilee","gender":"Female"},
{"id":7,"first_name":"Jilly","gender":"Non-binary"},
{"id":8,"first_name":"Hugues","gender":"Male"},
{"id":9,"first_name":"Roosevelt","gender":"Male"},
{"id":10,"first_name":"Yelena","gender":"Female"},
{"id":11,"first_name":"Peterus","gender":"Male"},
{"id":12,"first_name":"Lorri","gender":"Female"},
{"id":13,"first_name":"Babb","gender":"Non-binary"},
{"id":14,"first_name":"Yardley","gender":"Male"},
{"id":15,"first_name":"Saw","gender":"Male"},
{"id":16,"first_name":"Edin","gender":"Female"},
{"id":17,"first_name":"Garvey","gender":"Male"},
{"id":18,"first_name":"Elvera","gender":"Female"},
{"id":19,"first_name":"Flin","gender":"Male"},
{"id":20,"first_name":"Heidi","gender":"Female"},
{"id":21,"first_name":"Carny","gender":"Male"},
{"id":22,"first_name":"Janice","gender":"Female"},
{"id":23,"first_name":"Curtice","gender":"Genderfluid"},
{"id":24,"first_name":"Trina","gender":"Female"},
{"id":25,"first_name":"Wright","gender":"Male"},
{"id":26,"first_name":"Myron","gender":"Male"},
{"id":27,"first_name":"Hubert","gender":"Male"},
{"id":28,"first_name":"Lothario","gender":"Male"},
{"id":29,"first_name":"Dani","gender":"Male"},
{"id":30,"first_name":"Syman","gender":"Male"},
{"id":31,"first_name":"Elka","gender":"Female"},
{"id":32,"first_name":"Shoshana","gender":"Female"},
{"id":33,"first_name":"Jarrod","gender":"Male"},
{"id":34,"first_name":"Ruby","gender":"Male"},
{"id":35,"first_name":"Nico","gender":"Male"},
{"id":36,"first_name":"Otis","gender":"Male"},
{"id":37,"first_name":"Jannel","gender":"Bigender"},
{"id":38,"first_name":"Marijn","gender":"Male"},
{"id":39,"first_name":"Johnny","gender":"Male"},
{"id":40,"first_name":"Randolph","gender":"Male"},
{"id":41,"first_name":"Mikey","gender":"Male"},
{"id":42,"first_name":"Bev","gender":"Female"},
{"id":43,"first_name":"Udell","gender":"Male"},
{"id":44,"first_name":"Filia","gender":"Female"},
{"id":45,"first_name":"Wynn","gender":"Female"},
{"id":46,"first_name":"Emmey","gender":"Female"},
{"id":47,"first_name":"Mandel","gender":"Male"},
{"id":48,"first_name":"Pier","gender":"Female"},
{"id":49,"first_name":"Urbanus","gender":"Male"},
{"id":50,"first_name":"Matilda","gender":"Agender"},
{"id":51,"first_name":"Petronilla","gender":"Female"},
{"id":52,"first_name":"Shawn","gender":"Female"},
{"id":53,"first_name":"Rupert","gender":"Male"},
{"id":54,"first_name":"Aron","gender":"Bigender"},
{"id":55,"first_name":"Ariel","gender":"Male"},
{"id":56,"first_name":"Otes","gender":"Male"},
{"id":57,"first_name":"Ingunna","gender":"Female"},
{"id":58,"first_name":"Elaine","gender":"Female"},
{"id":59,"first_name":"Leonelle","gender":"Female"},
{"id":60,"first_name":"Lou","gender":"Male"},
{"id":61,"first_name":"Sheri","gender":"Female"},
{"id":62,"first_name":"Parsifal","gender":"Male"},
{"id":63,"first_name":"Blithe","gender":"Female"},
{"id":64,"first_name":"Yolanthe","gender":"Female"},
{"id":65,"first_name":"Iorgos","gender":"Male"},
{"id":66,"first_name":"Sherline","gender":"Female"},
{"id":67,"first_name":"Birgitta","gender":"Female"},
{"id":68,"first_name":"Ninnetta","gender":"Female"},
{"id":69,"first_name":"Alick","gender":"Bigender"},
{"id":70,"first_name":"Lamont","gender":"Male"},
{"id":71,"first_name":"Thurstan","gender":"Male"},
{"id":72,"first_name":"Perri","gender":"Female"},
{"id":73,"first_name":"Karlan","gender":"Male"},
{"id":74,"first_name":"Ransell","gender":"Bigender"},
{"id":75,"first_name":"Gavra","gender":"Female"},
{"id":76,"first_name":"Alphonse","gender":"Male"},
{"id":77,"first_name":"Wallis","gender":"Non-binary"},
{"id":78,"first_name":"Ase","gender":"Male"},
{"id":79,"first_name":"Shaun","gender":"Male"},
{"id":80,"first_name":"Selig","gender":"Male"},
{"id":81,"first_name":"Erhart","gender":"Male"},
{"id":82,"first_name":"Maryjo","gender":"Non-binary"},
{"id":83,"first_name":"Emilie","gender":"Female"},
{"id":84,"first_name":"Amory","gender":"Male"},
{"id":85,"first_name":"Tonia","gender":"Female"},
{"id":86,"first_name":"Lev","gender":"Male"},
{"id":87,"first_name":"Kim","gender":"Male"},
{"id":88,"first_name":"Mord","gender":"Male"},
{"id":89,"first_name":"Thom","gender":"Male"},
{"id":90,"first_name":"Symon","gender":"Male"},
{"id":91,"first_name":"Oona","gender":"Female"},
{"id":92,"first_name":"Rachele","gender":"Female"},
{"id":93,"first_name":"Ody","gender":"Bigender"},
{"id":94,"first_name":"Bab","gender":"Female"},
{"id":95,"first_name":"Leroi","gender":"Male"},
{"id":96,"first_name":"Mathilda","gender":"Female"},
{"id":97,"first_name":"Alexandros","gender":"Male"},
{"id":98,"first_name":"Daphna","gender":"Female"},
{"id":99,"first_name":"Lorrin","gender":"Female"},
{"id":100,"first_name":"Dela","gender":"Female"}]
user_col.insert_many(users)
print("inserted succesfully")