$(function(){
	var error_name = false;
	var error_pwd = false;
	var error_cpwd = false;
	var error_phone = false;
	var error_check = false;
	$('#user_name').blur(function(){
		check_user_name();
	});

	$('#pwd').blur(function(){
		check_pwd();
	});

	$('#cpwd').blur(function(){
		check_cpwd();
	});

	$('#phone').blur(function() {
		check_phone();
	});

	$('#allow').click(function() {
		if($(this).is(':checked'))
		{
			error_check = false;
			$(this).siblings('span').hide();
		} else
		{
			error_check = true;
			$(this).siblings('span').html('请勾选同意');
			$(this).siblings('span').show();
		}
	});

	function check_user_name(){
		var len = $('#user_name').val().length;
		if(len<5||len>20)
		{
			$('#user_name').next().html('请输入5-20个字符的用户名');
			$('#user_name').next().show();
			error_name = true;
		} else
		{
            var name = $('#user_name').val();
            data = {"name":name};
            $.get("/user/register_exist/",data,function(data){
                if(data!=0){
                    $('#user_name').next().html('此名已被注册');
                    $('#user_name').next().show();
                    error_name = true;
                }else{
                    $('#user_name').next().hide();
                    error_name = false;
                }
            },"json");
		}
	}

	function check_pwd(){
		var len = $('#pwd').val().length;
		if(len<8||len>20)
		{
			$('#pwd').next().html('密码最少8位，最长20位');
			$('#pwd').next().show();
			error_pwd = true;
		} else
		{
			$('#pwd').next().hide();
			error_pwd = false;
		}		
	}

	function check_cpwd(){
		var pass = $('#pwd').val();
		var cpass = $('#cpwd').val();
		if(cpass.length<1){
            $('#cpwd').next().html('请再次输入密码');
			$('#cpwd').next().show();
			error_cpwd = true;
		}else{
		    if(pass!=cpass)
		{
			$('#cpwd').next().html('两次输入的密码不一致');
			$('#cpwd').next().show();
			error_cpwd = true;
		} else
		{
			$('#cpwd').next().hide();
			error_cpwd = false;
		}
        }
	}

	function check_phone(){
		var reg_phone = /(^1[3|4|5|7|8]\d{9}$)|(^09\d{8}$)/;
		if(reg_phone.test($('#phone').val()))
		{
			$('#phone').next().hide();
			error_phone = false;
		} else
		{
			$('#phone').next().html('你输入的手机号格式不正确');
			$('#phone').next().show();
			error_phone = true;
		}
	}

	$('#reg_form').submit(function(){
	    check_user_name();
	    check_pwd();
	    check_cpwd();
	    check_phone();
		if(error_name==false&&error_pwd==false&&error_cpwd==false&&error_phone==false&&error_check==false)
		{
		    var code_indetify = $("#code_identify").val();
	        if (code_indetify.length<1){
	            $("#code_identify").next().next().html("请输入验证码");
	            $("#code_identify").next().next().show();
	            return false;
            }else if($("#code").val()!=code_indetify){
	            $("#code_identify").next().next().html("验证码错误");
	            $("#code_identify").next().next().show();
	            return false;
            }else{
	            return true;
            }
		} else {
		    return false;
		}
	});
});