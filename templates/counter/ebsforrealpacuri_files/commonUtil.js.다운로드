/************************************************
전체 업무에 적용되는 기능 정의
*************************************************/

var commonUtil= {

   		/*************************************************************************************************
		설명   : 공통 ajax Call (일반적인 ajax call 일때 이용)
		입력값 : url - 호출될 url (필수값)
		         data - 호출시 전송될 입력 파라메터  (필수값-공백 가능)
		         callback - 결과 전송시 호출될 callback (필수값)
		         contentType - contentType 설정(옵션값-기본은 post)
		         methodType - post나 get등 전송 type (옵션값-기본은 post)
		         async - 비동기화여부. true(비동기)/false비동기전송) (옵션값-기본은 true)
		         cache - cache 여부. true(cache 함)/false(cache 안함)  (옵션값-기본은 false)
		**************************************************************************************************/
		resourceURLRoot : "",
		
		ajaxCall : function(url, data, callback,contentType,methodType,async,cache){ 
			
			if(methodType != 'post' && methodType != 'get' ){
				methodType = 'post';
			}
			if(async != true && async != false){
				async = true;
			}
			if(cache != true  && cache != false){
				cache = false;
			}
			if(contentType == "json"){
				contentType = "application/json; charset=utf-8";
			} else {
				contentType = "application/x-www-form-urlencoded; charset=UTF-8";
			}
			
			var loadingImg = '<img  src='+this.resourceURLRoot+'/web_resource/image/loading.gif />';
			
			if($("body").hasClass("theme_white")){
				loadingImg = '<img  src='+this.resourceURLRoot+'/web_resource/images/loading_w.gif />';
			}
			
			var option = {
					url: url,
					data : (data?data:""),
					type : methodType,
					async : async,
					cache : cache,						
					dataType: "json",
					contentType : contentType,
					beforeSend : function(xhr, opts) {			
				        $.blockUI({ message: loadingImg, css: {border : '0px solid #ffffff' ,backgroundColor : '-', left : '50%', transform: 'translateX(-50%)' }});
				    },
			        success: function(result) {		
			        	$.unblockUI();
			        	
			        	if(result.returnCode == 'FAIL'){
			        		if(result.returnStatusCode == '320'){
			        			if(confirm("더 이상 어려운 문제가 없습니다. 비슷한 문제를 추천 받으시겠습니까?")){
			        				$("input[name=level]").val("0");
			        				selectItem();
			        			} else{
			        				if($thisSite == "PRI"){
			        					location.href="/pri/itemrcmd/itemrcmd.ebs";
			        				} else if($thisSite == "JHS"){
			        					location.href="/mid/itemrcmd/itemrcmd.ebs";
			        				} 
			        			}
			        		} else if(result.returnStatusCode == '321'){
			        			if(confirm("더 이상 쉬운 문제가 없습니다. 비슷한 문제를 추천 받으시겠습니까?")){
			        				$("input[name=level]").val("0");
			        				selectItem();
			        			} else{
			        				if($thisSite == "PRI"){
			        					location.href="/pri/itemrcmd/itemrcmd.ebs";
			        				} else if($thisSite == "JHS"){
			        					location.href="/mid/itemrcmd/itemrcmd.ebs";
			        				} 
			        			}
			        		} else if(result.returnStatusCode == '322'){
			        			alert("선택한 단원의 추천 문제를 모두 풀었습니다. 다른 단원을 선택해주세요.");		        				
			        		} else {
			        			if(result.returnStatusCode != '319'){
			        				alert(result.returnMessage);
			        			}
			        		}		
			        	} else {
			        		if(callback) {
                                callback(result);
                            }
			        	}
			        },
			        error : function(req, status, error) {	
			       		$.unblockUI();	
			       		
			       		console.info("code:"+req.status+"\nmessage:"+req.responseText+"\nerror:"+error);
			       		if(req.status == "403"){
							location.reload();
						} else {
							alert('서비스에 문제가 발생하였습니다.\n잠시 뒤에 다시 이용 부탁드립니다');	
						}
			        },
				};
			$.ajax(option); 
		},		
		
		/*************************************************************************************************
		설명   : 공통 ajax Html Call
		입력값 : url - 호출될 url (필수값)
		         data - 호출시 전송될 입력 파라메터  (필수값-공백 가능)
		         callback - 결과 전송시 호출될 callback (필수값)
		         contentType - contentType 설정(옵션값-기본은 post)
		         methodType - post나 get등 전송 type (옵션값-기본은 post)
		         async - 비동기화여부. true(비동기)/false비동기전송) (옵션값-기본은 true)
		         cache - cache 여부. true(cache 함)/false(cache 안함)  (옵션값-기본은 false)
		**************************************************************************************************/
		ajaxHtmlCall : function(url, data, callback,contentType,methodType,async,cache){ 
			if(methodType != 'post' && methodType != 'get' ){
				methodType = 'post';
			}
			if(async != true && async != false){
				async = true;
			}
			if(cache != true  && cache != false){
				cache = false;
			}
			if(contentType == "json"){
				contentType = "application/json; charset=utf-8";
			} else {
				contentType = "application/x-www-form-urlencoded; charset=UTF-8";
			}
			var option = {
					url: url,
					data : (data?data:""),
					type : methodType,
					async : async,
					cache : cache,						
					dataType: "html",
					contentType : contentType,
					beforeSend : function(xhr, opts) {	
				        $.blockUI({ message: '', baseZ:9999 });				       
				    },
			        success: function(result) {		
			        	$.unblockUI();
			        	
			        	if(result.returnCode=='FAIL'){
			        		alert(result.returnMessage);						
			        	} else {
                            if(callback) {
                                callback(result);
                            }
			        	}
			        },
			        error : function(req, status, error) {	
			        	$.unblockUI();	
			        	
			        	alert('서비스에 문제가 발생하였습니다.\n잠시 뒤에 다시 이용 부탁드립니다');			        	
			        },
				};
			$.ajax(option); 
		},	
	
		/*************************************************************************************************
		설명   : 공통 ajaxSubmit Call (첨부파일이 잇을시에 이것을 이용 요망)
		입력값 : formId - form Id  (필수값)
				 url - 호출될 url (필수값)
		         callback - 결과 전송시 호출될 callback (필수값)
		         methodType - post나 get등 전송 type (옵션값-기본은 post)		       
		**************************************************************************************************/
		ajaxSubmitCall : function(formId,url,callback,contentType,methodType){ 
			if(methodType != 'post' && methodType != 'get' ){
				methodType = 'post';
			}		
			if(contentType == "json"){
				contentType = "application/json; charset=utf-8";
			} else {
				contentType = "application/x-www-form-urlencoded; charset=UTF-8";
			}
			var option = {
					url: url,
					type : methodType,					
					dataType: "json",
					contentType : contentType,
					beforeSend : function(xhr, opts) {						
				        $.blockUI({ message: '', baseZ:9999 });
				    },
			        success: function(result) {		
			        	$.unblockUI();
			        	
			        	if(result.returnCode=='FAIL'){
			        		alert(result.returnMessage);						
			        	} else {
                            if(callback) {
                                callback(result);
                            }
			        	}
			        },
			        error : function(req, status, error) {		
			        	$.unblockUI();
			        	
			        	alert('서비스에 문제가 발생하였습니다.\n잠시 뒤에 다시 이용 부탁드립니다');			        	
			        },
				};
			$('#'+formId).ajaxSubmit(option); 
		},

        /*************************************************************************************************
        설명   : 브라우저 Alert 랩핑 함수
        입력값 : msg - 출력메시지, title - 타이틀, alertType - (WINDOW_ALERT:기본값, JQUERY_UI) , modal : modal여부
        **************************************************************************************************/
        alert: function (msg) {           
        	alert(msg);
        },

        /*************************************************************************************************
        설명   : 브라우저 open 랩핑 함수
        입력값 : url - 호출경로, title - 타이틀, option - pop option , frm - form,  modal : modal여부
        **************************************************************************************************/
        open: function (url, title, option) {
            window.open(url,title, option);
        },
        
        /*************************************************************************************************
        설명   : popup
        입력값 : id - popup id
         	    url - 호출될 url (필수값)
		        data - 호출시 전송될 입력 파라메터  (필수값-공백 가능)
        **************************************************************************************************/
        popup: function (id, url, data) {
            	commonUtil.ajaxHtmlCall(
            	url,  
            	data,
            	function(result){
	            	$(".layer_area").html(result);
					uiLayerSet.init(id);
            	});
        },         
        
        rePopup: function (id, url, data) {
            	commonUtil.ajaxHtmlCall(
            	url,  
            	data,
            	function(result){
	            	$(".layer_area").html(result);
	            	$(".layer_area").css("display", "block")
//	            	uiLayerStatus = 0;
//					uiLayerSet.init(id,'fback');
				    var modalWrap = document.getElementById(id);
				    modalWrap.style.display = "block"; // Show the modal
					
            	});
        }, 
        
        popupLit: function (url, data) {
            	commonUtil.ajaxHtmlCall(
            	url,  
            	data,
            	function(result){
	            	$("#litFinish").html(result);
					$('#litFinish').addClass("active");
            	});
        }, 
        
        popupNum: function (url, data) {
            	commonUtil.ajaxHtmlCall(
            	url,  
            	data,
            	function(result){            		
	            	$("#numFinish").html(result);
					$('#numFinish').addClass("active");
            	});
        }, 
};