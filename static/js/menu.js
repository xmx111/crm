function fillDivCont(url, divId, dataStr, errDivId, beforDivId){
	if(dataStr==null)dataStr="";
	$.ajax({
		url : url,
		type : "POST",
		data : dataStr,
		dataType : 'html',
		timeout : 100000,
		error : function() {
			//if (typeof(errDivId) != undefined)$("#"+divId).html($("#"+errDivId).html());
		},
		success : function(response) {
			$("#"+divId).html(response);
		},
		beforeSend : function() {
			if (typeof(beforDivId) != undefined)$("#"+divId).html($("#"+beforDivId).html());
		}
	});
}
function fillDivContGET(url, divId, dataStr, errDivId, beforDivId){
	if(dataStr==null)dataStr="";
	$.ajax({
		url : url,
		type : "GET",
		data : dataStr,
		dataType : 'html',
		timeout : 100000,
		error : function() {
			//if (typeof(errDivId) != undefined)$("#"+divId).html($("#"+errDivId).html());
		},
		success : function(response) {
			$("#"+divId).html(response);
		},
		beforeSend : function() {
			if (typeof(beforDivId) != undefined)$("#"+divId).html($("#"+beforDivId).html());
		}
	});
}