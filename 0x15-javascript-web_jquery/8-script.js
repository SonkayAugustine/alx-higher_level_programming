$.get("https://swapi-api.hbtn.io/api/films/?format=json", function (data) {    
    $.each(data.results, function (i, val) {	
	$("UL#list_movies").append("<li>" + val.title + "</li>");	
    });   
});
