Python Collection Types 

Python provides several built-in collection types for storing multiple values. The four important collection types are:

List
Tuple
Set
Dictionary


List vs Tuple vs Set vs Dictionary
Feature	List	Tuple	Set	Dictionary
Syntax	[]	()	{}	{key: value}
Example	[10, 20, 30]	(10, 20, 30)	{10, 20, 30}	{"name": "Ram", "age": 20}
Ordered	✅ Yes	✅ Yes	❌ No	✅ Yes*
Mutable	✅ Yes	❌ No	✅ Yes	✅ Yes
Allows duplicates	✅ Yes	✅ Yes	❌ No	Keys ❌, Values ✅
Indexing	✅ Yes	✅ Yes	❌ No	❌ No
Slicing	✅ Yes	✅ Yes	❌ No	❌ No
Key-value pairs	❌ No	❌ No	❌ No	✅ Yes
Access using	Index	Index	Membership	Key
Can change elements	✅ Yes	❌ No	✅ Yes	✅ Yes
Main purpose	General collection	Fixed data	Unique data	Related key-value data

*Dictionaries preserve insertion order in modern Python versions.