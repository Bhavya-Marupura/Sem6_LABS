$(document).ready(function(){
	$('.SubmitButton').click(function(){
		var fee=0;
		$('body').css({"background-color":"pink"});
		if(parseInt($("#age").val())>3 && parseInt($("#age").val())<=15){
			fee=fee+25;
		}
		else if(parseInt($("#age").val())>15){
			fee=fee+50;
		}
		if($("#camera").prop("checked")==true){
			fee=fee+10;
		}
		if($("#buggy").prop("checked")==true){
			if(parseInt($("#age").val())>3 && parseInt($("#age").val())<=15){
				fee=fee+100;
			}
			else if(parseInt($("#age").val())>15){
				fee=fee+200;
			}
		}
		$("#result").html("The result is : " + fee);
	});
});