$(document).ready(function(){

	// boxes
	$('.book-wrapper').hover(function(){
		$(".boxcaption", this).stop().animate({top:'0'},{queue:false,duration:300});
		$(".boxcaption").css("cursor", "pointer")
	}, function() {
		height = $(".book-box").height();
		$(".boxcaption", this).stop().animate({top:(height-61)+'px'},{queue:false,duration:300});
	});

	// Animate in the books when the page loads
	// $('.book-box').hide().first().show("fast", function showNext() {
	// 	$(this).next(".book-box").show("fast", showNext);
	// });


	$("input[type=text], input[type=email], input[type=password]").addClass('form-control')
	$("#login-btn").addClass('form-control')

});

$(window).on('resize', function(){
	height = $(".book-box").height();
	$(".boxcaption", ".book-box").stop().animate({top:(height-61)+'px'},{queue:false,duration:300});
});

function setRate(rate){
	$('.glyphicon-star').css("color", "#333")

	for (var i = rate; i > 0; i--) {
		$('#'+i).css("color", "gold")
	}
}



$('.glyphicon-star').click(function(e){
	$('#rate').val(e.target.id);
	$('#rate-frm').submit();
});

$('.glyphicon-star').hover(function(e){
	setRate(e.target.id)
});

$('.glyphicon-star').mouseleave(function(e){
	setRate( Math.round($('#rate').val()) )
});

setRate( Math.round($('#rate').val()) );