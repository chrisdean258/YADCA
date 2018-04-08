
(function ($) {
	"use strict";


	/*==================================================================
	  [ Focus Contact2 ]*/
	$('.input3').each(function(){
		$(this).on('blur', function(){
			if($(this).val().trim() != "") {
				$(this).addClass('has-val');
			}
			else {
				$(this).removeClass('has-val');
			}
		})
	})


	/*==================================================================
	  [ Chose Radio ]*/
	$("#radio1").on('change', function(){
		if ($(this).is(":checked")) {
			$('.input3-select').slideUp(300);
		}
	});

	$("#radio2").on('change', function(){
		if ($(this).is(":checked")) {
			$('.input3-select').slideDown(300);
		}
	});



	/*==================================================================
	  [ Validate ]*/
	var name = $('.validate-input input[name="name"]');
	var email = $('.validate-input input[name="email"]');
	var message = $('.validate-input textarea[name="message"]');


	$('.validate-form').on('submit',function(){
		var check = true;

		if($("#radio1").is(":checked"))
		{
			$('#name').each(function(){
				if(!$(this).hasClass("has-val"))
				{
					check = false;
					showValidate(this);
				}
			});
		}
		else if($("#radio2").is(":checked"))
		{
			$('.validate-form .input3').each(function(){
				if(!$(this).hasClass("has-val"))
				{
					check = false;
					showValidate(this);
				}
			});
		}
		else check = false;

		return check;
	});


	$('.validate-form .input3').each(function(){
		$(this).focus(function(){
			hideValidate(this);
		});
	});

	function showValidate(input) {
		var thisAlert = $(input).parent();

		$(thisAlert).addClass('alert-validate');
	}

	function hideValidate(input) {
		var thisAlert = $(input).parent();

		$(thisAlert).removeClass('alert-validate');
	}



})(jQuery);
