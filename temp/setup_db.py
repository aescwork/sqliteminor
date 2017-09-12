import sqlite3

def setup_db():

	conn = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
	cursor = conn.cursor()
	cursor.execute("CREATE TABLE trees(tree_id INT, name TEXT, qualities TEXT, age INT, sample_date DATE)")
	cursor.executescript("""
			INSERT INTO trees VALUES(1, "Ash", "deciduous, European, American, leaves, ancient", 200, '2017-05-20');
			INSERT INTO trees VALUES(2, "Yew", "evergreen, European, needles, ancient", 1000, '2017-05-10');
			INSERT INTO trees VALUES(3, "White Pine", "evergreen, needles, American, beautiful", 50, '2017-05-05');
			INSERT INTO trees VALUES(4, "Scots Pine", "evergreen, needles, European, beautiful", 120, '2017-02-11');
			INSERT INTO trees VALUES(5, "Elm", "deciduous, American", 100, '2017-02-11');
			INSERT INTO trees VALUES(6, "Sugar Maple", "deciduous, American, leaves", 120, '2017-04-25');
			INSERT INTO trees VALUES(7, "Sycamore", "deciduous, American, historic", 75, '2017-04-10');
			INSERT INTO trees VALUES(8, "Black Cherry", "deciduous, fruit-bearing, beautiful, American", 80, '2017-04-09');
			INSERT INTO trees VALUES(9, "Douglas Fir", "evergreen, American, needles", 500, '2017-03-20');
			INSERT INTO trees VALUES(10, "American Chestnut", "deciduous, fruit-bearing, American", 150, '2017-03-10');
			INSERT INTO trees VALUES(11, "Elder", "deciduous, American, medicinal, fruit-bearing", 40, '2017-02-11');
			INSERT INTO trees VALUES(12, "Northern Red Oak", "deciduous, hard, American", 240, '2017-02-11');
			INSERT INTO trees VALUES(13, "Alder Buckthorn", "deciduous, European", 900, '2017-04-14');
			INSERT INTO trees VALUES(14, "Common Hawthorn", "deciduous, European", 900, '2017-02-11');
			INSERT INTO trees VALUES(15, "Common Hazel", "deciduous, fruit-bearing, shrub", 30, '2017-05-02');
			INSERT INTO trees VALUES(16, "Midland Hawthorn", "deciduous, American", 900, '2017-02-11');
			INSERT INTO trees VALUES(17, "Redwood (Cupressaceae)", "evergreen", 900, '2017-02-11');
			INSERT INTO trees VALUES(18, "Guelder Rose", "deciduous, shrub, medicinal, beautiful" , 900, '2017-02-11');
			""")


	return conn
