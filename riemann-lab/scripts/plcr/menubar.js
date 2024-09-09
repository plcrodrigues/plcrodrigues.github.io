//<li class="active"><a href="./index.html">Home <span class="sr-only">(current)</span></a></li>

function makemenubar(pageselect){

	var content = `<ul class="nav nav-sidebar">
			      	<li id="index"><a href="./index.html">Home</a></li>
			      	<li id="algorithm"><a href="./algorithm.html">The algorithm</a></li>
			      	<li><hr/></li>			      	
				  	<li id="video"><a href="./video.html">Example 0 : Video frames</a></li>			      	
				  	<li id="bci"><a href="./bci.html">Example 1 : BCI</a></li>
				  	<li id="sleep"><a href="./sleep.html">Example 2 : Sleep</a></li>
				  	<li id="epilepsy"><a href="./epilepsy.html">Example 3 : Epilepsy</a></li>
			      	<li><hr/></li>			      					  	
				  	<li id="references"><a href="./references.html">References</a></li>				  	
				  	<li id="faq"><a href="./faq.html">FAQ</a></li>				  					  	
				  </ul>`;
			   
	$("#menubar").html(content);
	
	switch(pageselect) {
	    case "index":
	        $("#index").addClass("active").html('<a href="./index.html">Home<span class="sr-only">(current)</span></a>');
	        break;
	    case "algorithm":
	        $("#algorithm").addClass("active").html('<a href="./algorithm.html">The algorithm<span class="sr-only">(current)</span></a>');
	        break;		        
	    case "video":
	        $("#video").addClass("active").html('<a href="./video.html">Example 0 : Video frames<span class="sr-only">(current)</span></a>');
	        break;		        
	    case "bci":
	        $("#bci").addClass("active").html('<a href="./bci.html">Example 1 : BCI<span class="sr-only">(current)</span></a>');
	        break;
	    case "sleep":
	        $("#sleep").addClass("active").html('<a href="./sleep.html">Example 2 : Sleep<span class="sr-only">(current)</span></a>');
	        break;
	    case "epilepsy":
	        $("#epilepsy").addClass("active").html('<a href="./epilepsy.html">Example 3 : Epilepsy<span class="sr-only">(current)</span></a>');
	        break;	
	    case "references":
	        $("#references").addClass("active").html('<a href="./references.html">References<span class="sr-only">(current)</span></a>');
	        break;	
	    case "faq":
	        $("#faq").addClass("active").html('<a href="./faq.html">FAQ<span class="sr-only">(current)</span></a>');
	        break;		        	              	             	        
	}	
	
}

