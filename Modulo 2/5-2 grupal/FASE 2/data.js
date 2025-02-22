$(document).ready(function() {
    $('#example').dataTable( {
        "processing": true,
        "ajax": "data/objects_deep.txt",
        "columns": [
            { "data": "name" },
            { "data": "hr.position" },
            { "data": "contact.0" },
            { "data": "contact.1" },
            { "data": "hr.start_date" },
            { "data": "hr.salary" }
        ]
    } );
} );


{
	"data": [
	  {
		"name": "Tiger Nixon",
		"hr": {
		  "position": "System Architect",
		  "salary": "$3,120",
		  "start_date": "2011/04/25"
		},
		"contact": [
		  "Edinburgh",
		  "5421"
		]
	  },
	  {
		"name": "Garrett Winters",
		"hr": {
		  "position": "Director",
		  "salary": "$5,300",
		  "start_date": "2011/07/25"
		},
		"contact": [
		  "Edinburgh",
		  "8422"
		]
	  },
	  {
		"name": "Ashton Cox",
		"hr": {
		  "position": "Technical Author",
		  "salary": "$4,800",
		  "start_date": "2009/01/12"
		},
		"contact": [
		  "San Francisco",
		  "1562"
		]
	  },
	  {
		"name": "Cedric Kelly",
		"hr": {
		  "position": "Javascript Developer",
		  "salary": "$3,600",
		  "start_date": "2012/03/29"
		},
		"contact": [
		  "Edinburgh",
		  "6224"
		]
	  },
	  {
		"name": "Jenna Elliott",
		"hr": {
		  "position": "Financial Controller",
		  "salary": "$5,300",
		  "start_date": "2008/11/28"
		},
		"contact": [
		  "Edinburgh",
		  "5407"
		]
	  },
	  {
		"name": "Brielle Williamson",
		"hr": {
		  "position": "Integration Specialist",
		  "salary": "$4,525",
		  "start_date": "2012/12/02"
		},
		"contact": [
		  "New York",
		  "4804"
		]
	  },
	  {
		"name": "Herrod Chandler",
		"hr": {
		  "position": "Sales Assistant",
		  "salary": "$4,080",
		  "start_date": "2012/08/06"
		},
		"contact": [
		  "San Francisco",
		  "9608"
		]
	  },
	  {
		"name": "Rhona Davidson",
		"hr": {
		  "position": "Integration Specialist",
		  "salary": "$6,730",
		  "start_date": "2010/10/14"
		},
		"contact": [
		  "Edinburgh",
		  "6200"
		]
	  },
	  {
		"name": "Colleen Hurst",
		"hr": {
		  "position": "Javascript Developer",
		  "salary": "$5,000",
		  "start_date": "2009/09/15"
		},
		"contact": [
		  "San Francisco",
		  "2360"
		]
	  },
	  {
		"name": "Sonya Frost",
		"hr": {
		  "position": "Software Engineer",
		  "salary": "$3,600",
		  "start_date": "2008/12/13"
		},
		"contact": [
		  "Edinburgh",
		  "1667"
		]
	  },
	  {
		"name": "Jena Gaines",
		"hr": {
		  "position": "System Architect",
		  "salary": "$5,000",
		  "start_date": "2008/12/19"
		},
		"contact": [
		  "London",
		  "3814"
		]
	  },
	  {
		"name": "Quinn Flynn",
		"hr": {
		  "position": "Financial Controller",
		  "salary": "$4,200",
		  "start_date": "2013/03/03"
		},
		"contact": [
		  "Edinburgh",
		  "9497"
		]
	  },
	  {
		"name": "Charde Marshall",
		"hr": {
		  "position": "Regional Director",
		  "salary": "$5,300",
		  "start_date": "2008/10/16"
		},
		"contact": [
		  "San Francisco",
		  "6741"
		]
	  },
	  {
		"name": "Haley Kennedy",
		"hr": {
		  "position": "Senior Marketing Designer",
		  "salary": "$4,800",
		  "start_date": "2012/12/18"
		},
		"contact": [
		  "London",
		  "3597"
		]
	  },
	  {
		"name": "Tatyana Fitzpatrick",
		"hr": {
		  "position": "Regional Director",
		  "salary": "$2,875",
		  "start_date": "2010/03/17"
		},
		"contact": [
		  "London",
		  "1965"
		]
	  },
	  {
		"name": "Michael Silva",
		"hr": {
		  "position": "Senior Marketing Designer",
		  "salary": "$3,750",
		  "start_date": "2012/11/27"
		},
		"contact": [
		  "London",
		  "1581"
		]
	  },
	  {
		"name": "Paul Byrd",
		"hr": {
		  "position": "Javascript Developer",
		  "salary": "$5,000",
		  "start_date": "2010/06/09"
		},
		"contact": [
		  "New York",
		  "3059"
		]
	  },
	  {
		"name": "Gloria Little",
		"hr": {
		  "position": "Systems Administrator",
		  "salary": "$3,120",
		  "start_date": "2009/04/10"
		},
		"contact": [
		  "New York",
		  "1721"
		]
	  },
	  {
		"name": "Bradley Greer",
		"hr": {
		  "position": "Software Engineer",
		  "salary": "$3,120",
		  "start_date": "2012/10/13"
		},
		"contact": [
		  "London",
		  "2558"
		]
	  },
	  {
		"name": "Dai Rios",
		"hr": {
		  "position": "System Architect",
		  "salary": "$4,200",
		  "start_date": "2012/09/26"
		},
		"contact": [
		  "Edinburgh",
		  "2290"
		]
	  },
	  {
		"name": "Jenette Caldwell",
		"hr": {
		  "position": "Financial Controller",
		  "salary": "$4,965",
		  "start_date": "2011/09/03"
		},
		"contact": [
		  "New York",
		  "1937"
		]
	  },
	  {
		"name": "Yuri Berry",
		"hr": {
		  "position": "System Architect",
		  "salary": "$3,600",
		  "start_date": "2009/06/25"
		},
		"contact": [
		  "New York",
		  "6154"
		]
	  },
	  {
		"name": "Caesar Vance",
		"hr": {
		  "position": "Technical Author",
		  "salary": "$4,965",
		  "start_date": "2011/12/12"
		},
		"contact": [
		  "New York",
		  "8330"
		]
	  },
	  {
		"name": "Doris Wilder",
		"hr": {
		  "position": "Sales Assistant",
		  "salary": "$4,965",
		  "start_date": "2010/09/20"
		},
		"contact": [
		  "Edinburgh",
		  "3023"
		]
	  },
	  {
		"name": "Angelica Ramos",
		"hr": {
		  "position": "System Architect",
		  "salary": "$2,875",
		  "start_date": "2009/10/09"
		},
		"contact": [
		  "London",
		  "5797"
		]
	  },
	  {
		"name": "Gavin Joyce",
		"hr": {
		  "position": "Developer",
		  "salary": "$4,525",
		  "start_date": "2010/12/22"
		},
		"contact": [
		  "Edinburgh",
		  "8822"
		]
	  },
	  {
		"name": "Jennifer Chang",
		"hr": {
		  "position": "Regional Director",
		  "salary": "$4,080",
		  "start_date": "2010/11/14"
		},
		"contact": [
		  "London",
		  "9239"
		]
	  },
	  {
		"name": "Brenden Wagner",
		"hr": {
		  "position": "Software Engineer",
		  "salary": "$3,750",
		  "start_date": "2011/06/07"
		},
		"contact": [
		  "San Francisco",
		  "1314"
		]
	  },
	  {
		"name": "Ebony Grimes",
		"hr": {
		  "position": "Software Engineer",
		  "salary": "$2,875",
		  "start_date": "2010/03/11"
		},
		"contact": [
		  "San Francisco",
		  "2947"
		]
	  },
	  {
		"name": "Russell Chavez",
		"hr": {
		  "position": "Director",
		  "salary": "$3,600",
		  "start_date": "2011/08/14"
		},
		"contact": [
		  "Edinburgh",
		  "8899"
		]
	  },
	  {
		"name": "Michelle House",
		"hr": {
		  "position": "Integration Specialist",
		  "salary": "$3,750",
		  "start_date": "2011/06/02"
		},
		"contact": [
		  "Edinburgh",
		  "2769"
		]
	  },
	  {
		"name": "Suki Burks",
		"hr": {
		  "position": "Developer",
		  "salary": "$2,875",
		  "start_date": "2009/10/22"
		},
		"contact": [
		  "London",
		  "6832"
		]
	  },
	  {
		"name": "Prescott Bartlett",
		"hr": {
		  "position": "Technical Author",
		  "salary": "$6,730",
		  "start_date": "2011/05/07"
		},
		"contact": [
		  "London",
		  "3606"
		]
	  },
	  {
		"name": "Gavin Cortez",
		"hr": {
		  "position": "Technical Author",
		  "salary": "$6,730",
		  "start_date": "2008/10/26"
		},
		"contact": [
		  "San Francisco",
		  "2860"
		]
	  },
	  {
		"name": "Martena Mccray",
		"hr": {
		  "position": "Integration Specialist",
		  "salary": "$4,080",
		  "start_date": "2011/03/09"
		},
		"contact": [
		  "Edinburgh",
		  "8240"
		]
	  },
	  {
		"name": "Unity Butler",
		"hr": {
		  "position": "Senior Marketing Designer",
		  "salary": "$3,750",
		  "start_date": "2009/12/09"
		},
		"contact": [
		  "San Francisco",
		  "5384"
		]
	  },
	  {
		"name": "Howard Hatfield",
		"hr": {
		  "position": "Financial Controller",
		  "salary": "$4,080",
		  "start_date": "2008/12/16"
		},
		"contact": [
		  "San Francisco",
		  "7031"
		]
	  },
	  {
		"name": "Hope Fuentes",
		"hr": {
		  "position": "Financial Controller",
		  "salary": "$4,200",
		  "start_date": "2010/02/12"
		},
		"contact": [
		  "San Francisco",
		  "6318"
		]
	  },
	  {
		"name": "Vivian Harrell",
		"hr": {
		  "position": "System Architect",
		  "salary": "$4,965",
		  "start_date": "2009/02/14"
		},
		"contact": [
		  "San Francisco",
		  "9422"
		]
	  },
	  {
		"name": "Timothy Mooney",
		"hr": {
		  "position": "Financial Controller",
		  "salary": "$4,200",
		  "start_date": "2008/12/11"
		},
		"contact": [
		  "London",
		  "7580"
		]
	  },
	  {
		"name": "Jackson Bradshaw",
		"hr": {
		  "position": "Director",
		  "salary": "$5,000",
		  "start_date": "2008/09/26"
		},
		"contact": [
		  "New York",
		  "1042"
		]
	  },
	  {
		"name": "Miriam Weiss",
		"hr": {
		  "position": "Support Engineer",
		  "salary": "$4,965",
		  "start_date": "2011/02/03"
		},
		"contact": [
		  "Edinburgh",
		  "2120"
		]
	  },
	  {
		"name": "Bruno Nash",
		"hr": {
		  "position": "Software Engineer",
		  "salary": "$4,200",
		  "start_date": "2011/05/03"
		},
		"contact": [
		  "London",
		  "6222"
		]
	  },
	  {
		"name": "Odessa Jackson",
		"hr": {
		  "position": "Support Engineer",
		  "salary": "$3,600",
		  "start_date": "2009/08/19"
		},
		"contact": [
		  "Edinburgh",
		  "9383"
		]
	  },
	  {
		"name": "Thor Walton",
		"hr": {
		  "position": "Developer",
		  "salary": "$3,600",
		  "start_date": "2013/08/11"
		},
		"contact": [
		  "New York",
		  "8327"
		]
	  },
	  {
		"name": "Finn Camacho",
		"hr": {
		  "position": "Support Engineer",
		  "salary": "$4,800",
		  "start_date": "2009/07/07"
		},
		"contact": [
		  "San Francisco",
		  "2927"
		]
	  },
	  {
		"name": "Elton Baldwin",
		"hr": {
		  "position": "Data Coordinator",
		  "salary": "$6,730",
		  "start_date": "2012/04/09"
		},
		"contact": [
		  "Edinburgh",
		  "8352"
		]
	  },
	  {
		"name": "Zenaida Frank",
		"hr": {
		  "position": "Software Engineer",
		  "salary": "$4,800",
		  "start_date": "2010/01/04"
		},
		"contact": [
		  "New York",
		  "7439"
		]
	  },
	  {
		"name": "Zorita Serrano",
		"hr": {
		  "position": "Software Engineer",
		  "salary": "$5,300",
		  "start_date": "2012/06/01"
		},
		"contact": [
		  "San Francisco",
		  "4389"
		]
	  },
	  {
		"name": "Jennifer Acosta",
		"hr": {
		  "position": "Javascript Developer",
		  "salary": "$2,875",
		  "start_date": "2013/02/01"
		},
		"contact": [
		  "Edinburgh",
		  "3431"
		]
	  },
	  {
		"name": "Cara Stevens",
		"hr": {
		  "position": "Sales Assistant",
		  "salary": "$4,800",
		  "start_date": "2011/12/06"
		},
		"contact": [
		  "New York",
		  "3990"
		]
	  },
	  {
		"name": "Hermione Butler",
		"hr": {
		  "position": "Director",
		  "salary": "$4,080",
		  "start_date": "2011/03/21"
		},
		"contact": [
		  "London",
		  "1016"
		]
	  },
	  {
		"name": "Lael Greer",
		"hr": {
		  "position": "Systems Administrator",
		  "salary": "$3,120",
		  "start_date": "2009/02/27"
		},
		"contact": [
		  "London",
		  "6733"
		]
	  },
	  {
		"name": "Jonas Alexander",
		"hr": {
		  "position": "Developer",
		  "salary": "$5,300",
		  "start_date": "2010/07/14"
		},
		"contact": [
		  "San Francisco",
		  "8196"
		]
	  },
	  {
		"name": "Shad Decker",
		"hr": {
		  "position": "Regional Director",
		  "salary": "$5,300",
		  "start_date": "2008/11/13"
		},
		"contact": [
		  "Edinburgh",
		  "6373"
		]
	  },
	  {
		"name": "Michael Bruce",
		"hr": {
		  "position": "Javascript Developer",
		  "salary": "$4,080",
		  "start_date": "2011/06/27"
		},
		"contact": [
		  "Edinburgh",
		  "5384"
		]
	  },
	  {
		"name": "Donna Snider",
		"hr": {
		  "position": "System Architect",
		  "salary": "$3,120",
		  "start_date": "2011/01/25"
		},
		"contact": [
		  "New York",
		  "4226"
		]
	  }
	]
  }