/**
 * 문제추천 분류코드 설정
 * 초기문제추천에서 받아온 값은 쿠키에 설정
 * 풀어본문제/담은문제에서 다시풀기 시에는 DB에서 조회된 값으로 설정
 */
function fnGetPrbmSuggest() {  
	var returnCate;
	var cate_cd_1;
	var cate_cd_2;
	var cate_cd_3;
	var cate_cd_4;
	var cate_cd_5;
	var cateArray;
	var cookieInfo = $.cookie( '_prbm_suggest_' );
	
	if ( typeof( cookieInfo ) === 'undefined') {
		// 쿠키에 정보가 없을 경우 DB에서 조회된 값으로 설정
		cate_cd_1 = $('input[name=cateCd1]').val();
		cate_cd_2 = $('input[name=cateCd2]').val();
		cate_cd_3 = $('input[name=cateCd3]').val();
		cate_cd_4 = $('input[name=cateCd4]').val();
		cate_cd_5 = $('input[name=cateCd5]').val();
		
		var cateArray = new Array();
		cateArray[0] = cate_cd_1+"_"+cate_cd_2+"_"+cate_cd_3+"_"+cate_cd_4+"_"+cate_cd_5;
		var _cookieInfo = {
			'cate_cd_1' : cate_cd_1,
			'cate_cd_2' : cate_cd_2,
			'cate_cd_3' : cate_cd_3,
			'cate_cd_4' : cate_cd_4,
			'cate_cd_5' : cate_cd_5,
			'cateArray' : cateArray
		};
		
		$.cookie('_prbm_suggest_',JSON.stringify(_cookieInfo),{expires:1,path:'/'});
	} else {
		// 쿠키에 정보가 있으면 쿠키값으로 설정
		// 메인화면에서 넘어왔을 때,
		var _cookieInfo = JSON.parse(cookieInfo);
		cate_cd_1 = _cookieInfo.cate_cd_1;
		cate_cd_2 = _cookieInfo.cate_cd_2;
		cate_cd_3 = _cookieInfo.cate_cd_3;
		cate_cd_4 = _cookieInfo.cate_cd_4;
		cate_cd_5 = _cookieInfo.cate_cd_5;
		cateArray = _cookieInfo.cateArray;
	}
	
	returnCate = {
		cate_cd_1 : cate_cd_1,
		cate_cd_2 : cate_cd_2,
		cate_cd_3 : cate_cd_3,
		cate_cd_4 : cate_cd_4,
		cate_cd_5 : cate_cd_5,
		cateArray : cateArray
	};
	
	return returnCate;
}

/**
 * 문제추천 분류코드 삭제 후
 * 문제풀이 화면으로 이동
 */
function fnResetPrbmSuggest(returnUrl) {
	$.removeCookie('_prbm_suggest_', { path: '/' });	
	if ( typeof( returnUrl ) === 'undefined' || returnUrl == '') {
	} else {
		location.href = returnUrl;
	}
}

/**
 * 문제풀이 경로 취득
 */
function fnLoadPrbmSuggest() {
	
	var cate_cd_1;
	var cate_cd_2;
	var cate_cd_3;
	var cate_cd_4;
	var cookieInfo = $.cookie( '_prbm_suggest_' );
	
	if ( typeof( cookieInfo ) === 'undefined') {
		// 쿠키에 정보가 없을 경우 DB에서 조회된 값으로 설정
		cate_cd_1 = $('input[name=cateCd1]').val();
		cate_cd_2 = $('input[name=cateCd2]').val();
		cate_cd_3 = $('input[name=cateCd3]').val();
		cate_cd_4 = $('input[name=cateCd4]').val();
	} else {
		var _cookieInfo = JSON.parse(cookieInfo);
		cate_cd_1 = _cookieInfo.cate_cd_1;
		cate_cd_2 = ( typeof _cookieInfo.cate_cd_2 === 'undefined' ) ? '' : _cookieInfo.cate_cd_2 ;
		cate_cd_3 = ( typeof _cookieInfo.cate_cd_3 === 'undefined' ) ? '' : _cookieInfo.cate_cd_3 ;
		cate_cd_4 = ( typeof _cookieInfo.cate_cd_4 === 'undefined' ) ? '' : _cookieInfo.cate_cd_4 ;
	}
	
	if (cate_cd_3.indexOf(",") > -1) cate_cd_3 = '';
	if (cate_cd_4.indexOf(",") > -1) cate_cd_4 = '';
	
	$.ajax({
		url : '/ebs/ai/aib/selectPrbmCatPath.ajax',
		data : {
			prbmCat : cate_cd_1+"_"+cate_cd_2+"_"+cate_cd_3+"_"+cate_cd_4
		},
		dataType : 'json',
		success : function(result) {
			var fullName = result.prbmCatPath.fullName;
//			var fullNameArray = fullName.split(">");
//			
//			var pathText = "";
//			$.each(fullNameArray, function(idx, item) {
//				pathText += "<span class='cate'>"+item+"</span>";
//			});
			$(".path").html(fullName);
		},
		error : function(e) {
			console.error(e);
		}
	});
}

/**
 * 문제풀이 경로 취득(수학맵)
 */
function fnLoadPrbmSuggestMathMap() {
	var creatCd = $('input[name=creatCd]').val();
	var depth = $('input[name=depth]').val();
	
	$.ajax({
		url : '/ebs/ai/mathMap/selectPrbmCatPathMathMap.ajax',
		data : {
			creatCd : creatCd,
			depth : depth
		},
		dataType : 'json',
		success : function(result) {
			var fullName = result.prbmCatPathMathMap.fullName;
//			var fullNameArray = fullName.split(">");
			
//			var pathText = "";
//			$.each(fullNameArray, function(idx, item) {
//				pathText += "<span class='cate'>"+item+"</span>";
//			});
			$(".path").html(fullName);
		},
		error : function(e) {
			console.error(e);
		}
	});
}

/**
 * 해설영상 조회 팝업
 * @param paperId
 * @param itemId
 */
function fnVodPlayerPopup(paperId, itemId) {
	
	var nWidth = 600;
	var nHeight = 400;
	var LeftPosition = (screen.width - nWidth) / 2;
	var TopPosition = (screen.height - nHeight) / 2;
	window.open("/ebs/ai/aib/selectSaveItemVod.ebs?paperId="+paperId+"&itemId="+itemId,"openPop","width="+nWidth+",height="+nHeight+",top="+TopPosition+",left="+LeftPosition+", scrollbars=no");
}

/**
 * 마이크로사이트 공통 로그(해설영상,해설지,풀어본문제,문제추천) 이력
 * 2019/05/14
 * @param pParam
 */
function fnCommonLog(pParam) {

	$.ajax({
		url : '/ebs/ai/com/comLogging.ajax',
		data : {
			itemId : pParam.itemId
			,logType : pParam.logType
		    ,wrtHistNo : pParam.wrtHistNo
			,sbjtId : pParam.sbjtId
			,etc1 : pParam.etc1
			,etc2 : pParam.etc2
			,etc3 : pParam.etc3
			,cateCd1 : pParam.cateCd1
			,cateCd2 : pParam.cateCd2
			,cateCd3 : pParam.cateCd3
			,cateCd4 : pParam.cateCd4
			,cateCd5 : pParam.cateCd5
		},
		dataType : "json",
		async : false,
		contentType: "application/x-www-form-urlencoded; charset=UTF-8",
		type : 'POST',
		success : function(data) {
			if (data.status != '200') {
				console.error(data.message);
			}
		},
		error : function(e) {
//			alert('error : ' + e.result);
			return;
		}
	});
}

/**
 * 공통 영상플레이어
 * @param pUrl
 * @param pSrTime
 * @param pEdTime
 */
function fnCommonVodPlayerPopup(pUrl,pSrTime,pEdTime,pSbjtId,pItemId) {
	var data={};
	var popVideo;
	if (pUrl == 'NO_URL') {
		if (location.pathname.split('/').slice(2,3).join('/') == "high") {
			data.site_id = 'HSC';	
		} else {
			data.site_id = 'JHS';
		}
	    data.item_id = pItemId;
		
		var popChk ; //= window.open("/cmm_resource/vod.html", "popupVideo", 	"width=680,height=570,location=no");
		 
		commonUtil.ajaxCall('/onestop/high/step1/selectLectInfo.ajax',
				JSON.stringify(data),
				function(result) {
					if (result.status=="200") {
						pUrl = result.data[0].mp4_url;
						pSrTime = result.data[0].start_time;
					}
				},
				"json",
				null,
				false);
	}
	// 공통 인공지능 이력등록
	if (typeof pItemId !== 'undefined' && pItemId != '') {
		var vLogParam = {
			itemId : pItemId
			,logType : 'vod'
			,sbjtId : pSbjtId
		};
		fnCommonLog(vLogParam);
	}
	
	// 공통 영상플레이어 파라미터 설정
	var actionUrl = "https://www.ebsi.co.kr/ebs/lms/player/retrieveLmsPlayerHtml5Simple.ebs?medUrl="+pUrl+"&strStartTm="+pSrTime;
	if (document.domain == 'stg-ai.ebs.co.kr') {//스테이징
		actionUrl = "https://stg-www.ebsi.co.kr/ebs/lms/player/retrieveLmsPlayerHtml5Simple.ebs?medUrl="+pUrl+"&strStartTm="+pSrTime;
	}
	
	// 영상플레이어 타입 설정
	if (_BrowserInfo.deviceGbn != "P") {
		actionUrl += "&pType=3&isPlay=true";
	} else {
		actionUrl += "&pType=2";
	}
	
	// 공통 영상플레이어 실행	
	//window.open(actionUrl, '_fnCmnVopPlayer', 'width=680, height=715, status=no, scrollbars=no, resizable=no');
	
	/* 팝업창 URL 처리 strat */
	var ua = window.navigator.userAgent.toLowerCase();
    var isiOS = ua.indexOf('iphone') > -1 || ua.indexOf('ipad') > -1 || ua.indexOf('macintosh') > -1 && 'ontouchend' in document;
    
    if (!isiOS) {
    	popChk = window.open('/web_resource/vod.html', '_fnCmnVopPlayer', 'width=680, height=715, status=no, scrollbars=no, resizable=no');
    	if (popChk) {
    		popChk.close();
    	}
    }
	setTimeout(function() {
		popVideo = window.open('/web_resource/vod.html', '_fnCmnVopPlayer', 'width=680, height=715, status=no, scrollbars=no, resizable=no');
		
		if (popVideo) {
			$(popVideo.window).on('load', (function() {
				$(popVideo.document).find('iframe#vodFrm').attr('src', actionUrl);
			}));
		}
	}, 50);
	/* 팝업창 URL 처리 end */
}

/**
 * 모바일 영상플레이어
 * @param pUrl
 * @param pSrTime
 * @param pEdTime
 */
function fnCommonVodPlayerMOBPopup(pUrl,pSrTime,pEdTime,pSbjtId,pItemId) {
	
	// 공통 인공지능 이력등록
	if (typeof pItemId !== 'undefined' && pItemId != '') {
		var vLogParam = {
			itemId : pItemId
			,logType : 'vod'
			,sbjtId : pSbjtId
		};
		fnCommonLog(vLogParam);
	}
	
	// 공통 영상플레이어 파라미터 설정
	var actionUrl = "http://www.ebsi.co.kr/ebs/lms/player/retrieveLmsPlayerHtml5Simple.ebs?medUrl="+pUrl+"&strStartTm="+pSrTime;
	
	// 영상플레이어 타입 설정
	if (_BrowserInfo.deviceGbn != "P") {
		actionUrl += "&pType=3&isPlay=true";
	} else {
		actionUrl += "&pType=2";
	}
	// 공통 영상플레이어 실행	
	window.open(actionUrl, '_fnCmnVopPlayer', 'width=680, height=715, status=no, scrollbars=no, resizable=no');
	
}

/**
 * 앱 영상플레이어
 * @param pUrl
 * @param pSrTime
 * @param pEdTime
 */
function fnCommonVodPlayerAppPopup(pUrl,pSrTime,pEdTime,pSbjtId,pItemId,pLecGbn,pBookId,pTxbkQuesId,pLessonId,pTitle,pUserIdEnc,pPrtCd) {
	
	// 공통 인공지능 이력등록
	if (typeof pItemId !== 'undefined' && pItemId != '') {
		var vLogParam = {
			itemId : pItemId
			,logType : 'vod'
			,sbjtId : pSbjtId
		};
		fnCommonLog(vLogParam);
	}
	
	var isANDROID = (navigator.userAgent.match('Android') != null);
	var isIPHONE = (navigator.userAgent.match('iPhone') != null || navigator.userAgent.match('iPod') != null);
	var isIPAD = (navigator.userAgent.match('iPad') != null);
	
	var subtitleUrl = "";
	if (pSbjtId && pLessonId) {
		subtitleUrl += "https://www.ebsi.co.kr/ebs/pot/potb/captionFileDownload.ebs?dir=caption&path=/";
		subtitleUrl += pSbjtId + "/";
		subtitleUrl += pLessonId + "&file=";
		subtitleUrl += pLessonId.substring(1,14)+"_UTF";
	}
	
	var param = {
		type: 'PREVIEW',
		title: pTitle,
		url: pUrl,
		startTime : pSrTime,
		endTime : pEdTime,
		subjectId: pSbjtId,
		lessonId: pLessonId,
		previewCatCd: 'A003',
		subtitleUrl : subtitleUrl
	}
	
	if (isANDROID) {
		window.EBSiHybridInterface.openMoviePlayer(JSON.stringify(param));
	}else if (isIPHONE || isIPAD) {
		window.webkit.messageHandlers.openMoviePlayer.postMessage(JSON.stringify(param));
	}
	
	/*
	// 공통 영상플레이어 파라미터 설정
	var actionUrl = 
		"cnebsiapp://?type=munhang_play&user_id="+pUserIdEnc
		+"&txbk_ques_id="+pTxbkQuesId+"&book_id="+pBookId+"&sbjt_id="+pSbjtId+"&mov_sbjt_id="+pSbjtId
		+"&lesson_id="+pLessonId+"&index_id=1&start_time="+pSrTime+"&end_time="+pEdTime+"&search="+pPrtCd
		+"&play_type=munhang_index_play&tab_gbn=munhang&imgCode=&rate=1.0&vod_gbn="+pLecGbn
		+"&vod_title="+pTitle+"&vod_url="+pUrl+"&item_id="+pItemId;
	
	window.location.href = actionUrl;
	*/
	
}

/**
 * 문제풀이현황 사용자 풀어본 수 조회
 */
function fnGetPrbmUserCount() {
	$.ajax({
		url : '/ebs/ai/aib/resultPopupAjax.ajax',
		dataType : "json",
		async : false,
		contentType: "application/x-www-form-urlencoded; charset=UTF-8",
		type : 'POST',
		success : function(data) {
			var result = data.resultStatus;
			if (result == 'SUCCESS') {
				$("#prbmTotalCnt").text(data.userCountInfo.cnt);
			} else {
				alert(data.resultMsg);
			}
			
			var prbmNowCnt = fnLoadPrbmCount();
			$("#prbmNowCnt").text(prbmNowCnt);
		},
		error : function(e) {
			alert('error : ' + e.result);
			return;
		}
	});
}

/**
 * 문제풀이현황 조회
 */
function fnLoadPrbmCount(flag) {

	var resultCount = 0;
	var _prbm_cnt = {
		count : resultCount
		,list : ''
	};

	if (flag == 'reset') {
		$.cookie('_prbm_cnt',JSON.stringify(_prbm_cnt),{expires:1,path:'/'});
	} else {
		var cookieInfo = $.cookie( '_prbm_cnt' );
		if ( typeof( cookieInfo ) === 'undefined') {
			// 쿠키에 정보가 없을 경우
			$.cookie('_prbm_cnt',JSON.stringify(_prbm_cnt),{expires:1,path:'/'});
		} else {
			var _prbm_cnt = JSON.parse(cookieInfo);
			resultCount = _prbm_cnt.count;
		}
	}
	
	return resultCount;
}

/**
 * 문제풀이현황 갱신
 */
function fnUpdatePrbmCount(itemId) { 

	var _prbm_cnt = {
		count : 0
		,list : ''
	};
	
	var cookieInfo = $.cookie( '_prbm_cnt' );
	if ( typeof( cookieInfo ) === 'undefined') {
		$.cookie('_prbm_cnt',JSON.stringify(_prbm_cnt),{expires:1,path:'/'});
	} else {
		var isPrbmNew = true;
		_prbm_cnt = JSON.parse(cookieInfo);
		
		if (_prbm_cnt.list != '') {
			var prbmArray = _prbm_cnt.list.split(',');
			for(var i=0;i<prbmArray.length;i++) {
				if (prbmArray[i] == itemId) {
					isPrbmNew = false;
				}
			}
		}
		
		if (isPrbmNew) {
			_prbm_cnt.count = _prbm_cnt.count + 1;
			_prbm_cnt.list = _prbm_cnt.list + "," + itemId;
			$.cookie('_prbm_cnt',JSON.stringify(_prbm_cnt),{expires:1,path:'/'});
		}
	}
	
	fnGetPrbmUserCount();
}

/**
 * 풀이시간 미전송을 위하여, 동일문제 풀었는지 여부 확인
 */
function fnIsSamePrbm(itemId) {
	
	var isSame = false;

	var _prbm_cnt = {
		count : 0
		,list : ''
	};
	
	var cookieInfo = $.cookie( '_prbm_cnt' );
	if ( typeof( cookieInfo ) === 'undefined') {
		isSame = false;
	} else {
		
		_prbm_cnt = JSON.parse(cookieInfo);
		
		if (_prbm_cnt.list != '') {
			var prbmArray = _prbm_cnt.list.split(',');
			for(var i=0;i<prbmArray.length;i++) {
				if (prbmArray[i] == itemId) {
					isSame = true;
				}
			}
		}
	}
	
	return isSame;
}

// 해설지 보기
function fnViewNewExamInfo(pItemId, pItemOnlyFlag, pSiteGbn, pChatbot) {

	var pParam = {
		itemId : pItemId
		,logType : 'cmt'
		,etc1 : ''
		,etc2 : ''
		,etc3 : ''	
	};
	fnCommonLog(pParam);
	
    $.ajax({
        type: "POST",
        url: "/ebs/ai/aib/PopupSolveView.ebs",
		data : {
			itemId : pItemId,
			itemOnly : pItemOnlyFlag,
			siteGbn : (pSiteGbn != '' ? pSiteGbn : 'HSC'),
			chatbot : pChatbot
		},
        dataType: "html", 
        async : false,
        success: function(data) {
        	$("#solvePop").html(data);
        }
	});
	
	// 모달팝업 중 html,body의 scroll을 hidden시킴
	$('html, body').css({'overflow': 'hidden', 'height': '100%'});
}

// 옵션 해설지 보기
function fnViewNewSolveInfo(pItemId, pItemOnlyFlag, pItemCommFlag, pGroupFlag, pSiteGbn, pChatbot) {

	var pParam = {
		itemId : pItemId
		,logType : 'cmt'
		,etc1 : ''
		,etc2 : ''
		,etc3 : ''	
	};
	fnCommonLog(pParam);
	
    $.ajax({
        type: "POST",
        url: "/ebs/ai/aib/PopupSolveView.ebs",
		data : {
			itemId : pItemId,
			itemOnly : pItemOnlyFlag,
			itemCommFlag : pItemCommFlag,
			groupFlag : pGroupFlag,
			siteGbn : (pSiteGbn != '' ? pSiteGbn : 'HSC'),
			chatbot : pChatbot
		},
        dataType: "html", 
        async : false,
        success: function(data) {
        	$("#solvePop").html(data);
        }
	});
	
	// 모달팝업 중 html,body의 scroll을 hidden시킴
	if (contextPath().indexOf('onestop') > -1) {
		$('body').css({'overflow': 'hidden', 'height': '100%'});
	} else {
		$('html, body').css({'overflow': 'hidden', 'height': '100%'});		
	}
}

// 다음추천레벨에 따른 문제추천
function fnNextRecmd(pLevel) {
	var cateInfo = fnGetPrbmSuggest();
	var depth = cateInfo.cate_cd_5 == '' ? cateInfo.cate_cd_4 == '' ? cateInfo.cate_cd_3 == '' ? cateInfo.cate_cd_2 == '' ? 1 : 2 : 3 : 4 : 5;
	var input = {
		'item_id' : $('#ItemID').val(), 	
		'is_moc' : 0,
		'cate_cd_1' : cateInfo.cate_cd_1,
		'cate_cd_2' : cateInfo.cate_cd_2,
		'cate_cd_3' : cateInfo.cate_cd_3,
		'cate_cd_4' : cateInfo.cate_cd_4,
		'cate_cd_5' : cateInfo.cate_cd_5,
		'last_item_level' : $('input[name=itemLevel]').val(),
		'is_correct' : $("input[name=cnsrYn]").val(),
		'level' : pLevel,
		'depth' : depth,
		'logType' : 'nxt',
		'continueWrtFlag' : $("input[name=continueWrtFlag]").val(),
		'selectedMenuAr' : $("input[name=mainMenu]").val(),
		'groupHistNo' : $("input[name=groupHistNo]").val(),
		'item_type' : $("input[name=itemType]").val(),
	};
	
	fnRecommend(input);
}

// 분류 및 분류명으로 문항 추천
function fnCategoryRecmd(str, ar) {
	
	var arrStr = str.split('##');
	
	var input = {};
	
	input.is_moc = 0;
	
	var arrStrLength = arrStr.length;
	input.cate_cd_1 = arrStr[0];
	if (arrStrLength == 2) {
		input.cate_cd_2 = arrStr[1];
	} else if (arrStrLength == 3) {
		input.cate_cd_3 = arrStr[2];
	} else if (arrStrLength == 4) {
		input.cate_cd_4 = arrStr[3];
	}
	input.last_item_level = '';
	input.is_correct = 0;
	input.level = 0;
	
	if (confirm('인공지능 단추가 추천하는 맞춤 추천문제를 풀어보세요.\n\n추천문제 영역 : '+ar)) {
		fnRecommend(input);
	}
};

// 분류코드로 문항 추천
function fnCategoryCodeRecmd(pCateCdArr, ar) {
	var arrStr = pCateCdArr.split('_');
	
	var input = {};
	
	input.is_moc = 0;
	
	var arrStrLength = arrStr.length;
	input.cate_cd_1 = arrStr[0];
	if (arrStrLength == 2) {
		input.cate_cd_2 = arrStr[1];
	} else if (arrStrLength == 3) {
		input.cate_cd_3 = arrStr[2];
	} else if (arrStrLength == 4) {
		input.cate_cd_4 = arrStr[3];
	}
	input.last_item_level = '';
	input.is_correct = 0;
	input.level = 0;
	input.selectedMenuAr = arrStr[0];
	
	var arrTxt = '영역';
	if (arrStrLength > 2) arrTxt = '단원';
	
	if (confirm('인공지능 단추가 추천하는 맞춤 추천문제를 풀어보세요.\n\n추천문제 '+arrTxt+' : '+ar)) {
		fnRecommend(input);
	}
};

//문항 추천
function fnRecommend(input) {
	var is_moc = '0'; // 당분간 고정값
	var cate_cd_1 = input.cate_cd_1;
	var cate_cd_2 = input.cate_cd_2;
	var cate_cd_3 = input.cate_cd_3;
	var cate_cd_4 = input.cate_cd_4;
	var cate_cd_5 = input.cate_cd_5;
	var last_item_level = input.last_item_level;
	var is_correct = input.is_correct;
	var level = input.level;
	var depth = input.depth;
	var option = input.option;
	var sugRandom = input.sugRandom;
	var continueWrtFlag = input.continueWrtFlag;
	var selectedMenuAr = input.selectedMenuAr;
	var groupHistNo = input.groupHistNo;
	var lastItemId = input.item_id;
	var sourceGbn = input.sourceGbn;
	var itemType = input.item_type;
	
	var depth = 2;
	if (cate_cd_3 != '') depth = 3;
	if (cate_cd_4 != '') depth = 4;
	if (cate_cd_5 != '') depth = 5;
	
	if (typeof continueWrtFlag === 'undefined' || continueWrtFlag == null) {
		continueWrtFlag = '';
	}
	if (typeof sourceGbn === 'undefined' || sourceGbn == null || sourceGbn == '') {
		sourceGbn = 'DEF';
	}
	if (typeof itemType === 'undefined' || itemType == null || itemType == '') {
		itemType = '21';//객관식
	}
	
	// 결과값
	var itemId;
	var user_grade;
	var cate_cd_3;
	var avg_time;
	var item_level;
	
	$.ajax({
		url: '/ebs/ai/aib/retrievePrbmGateAi.ajax',
		contentType: "application/x-www-form-urlencoded; charset=EUC-KR",			
		type : 'get',
		dataType: 'json',
		data : {
				'is_moc' : is_moc
				, 'cate_cd_1' : cate_cd_1
				, 'cate_cd_2' : cate_cd_2
				, 'cate_cd_3' : cate_cd_3
				, 'cate_cd_4' : cate_cd_4
				, 'cate_cd_5' : cate_cd_5
				, 'last_item_level' : last_item_level
				, 'last_item_id' : lastItemId
				, 'is_correct' : is_correct
				, 'level' : level
				, 'option' : option
				, 'sugRandom' : sugRandom
				, 'item_type' : itemType
		},
		success: function(data) {
			if (data.resultStatus == 'FAIL') {
				alert(data.resultMsg);
			} else {
				var jsonData = data.result;
				user_grade = jsonData.user_grade;
				var status = jsonData.status;
				
				if (status == 301) {
					if (confirm("선택한 분류체계 내 학습수준에 맞는 문제가 존재하지 않습니다.\n다른 수준의 문제를 추천 받으시겠습니까?\n(취소 선택 시, 분류 선택 화면으로 이동합니다.)")) {
						input.sugRandom = 'Y';
						input.option = 'Y';
						input.level = 0;
						fnRecommend(input);
					} else {
						var returnUrl = '/ebs/ai/aib/ItemMain.ebs'+'?globalGradeCd='+$('input[name=globalGradeCd]').val();	
					
						if($("input[name=referrerSite]").val()){
							
						returnUrl =	$("input[name=referrerSite]").val()
							
						}
						
						location.href = returnUrl;
					}
				} else if (status == 302) {
					if (confirm("선택한 분류에 준비된 추천 문제를 모두 풀었습니다.\n'추천 문제 풀기' 영역을 다시 선택해주세요.\n(확인시 선택 화면으로 이동합니다)")) {
						var returnUrl = '/ebs/ai/aib/ItemMain.ebs'+'?globalGradeCd='+$('input[name=globalGradeCd]').val();	
						
						if($("input[name=referrerSite]").val()){
								returnUrl =	$("input[name=referrerSite]").val()
						}
						
						location.href = returnUrl;
					
					}
				} else {
						
					var returnObj = {};
					try {
						returnObj = fnRecommendSort(jsonData);
					}catch(e) {
						returnObj = jsonData.item[0];
					}
					
					var pCateCd1 = "", pCateCd2 = "", pCateCd3 = "", pCateCd4 = "", pCateCd5 = "";
					itemId = returnObj.item_id;
					pCateCd1 = returnObj.category[0].cate_cd_1;
					pCateCd2 = returnObj.category[0].cate_cd_2;
					pCateCd3 = (returnObj.category[0].cate_cd_3 != 'null')?returnObj.category[0].cate_cd_3:'';
					pCateCd4 = (returnObj.category[0].cate_cd_4 != 'null')?returnObj.category[0].cate_cd_4:'';
					pCateCd5 = (returnObj.category[0].cate_cd_5 != 'null')?returnObj.category[0].cate_cd_5:'';
					avg_time = returnObj.avg_time;
					item_level = Math.round(returnObj.item_level);		
					
					/*
					국어 및 영어>독해 경우에 알림 문구표시
					var loadingTextOption = true;
					if (pCateCd1 == '1000001' || pCateCd1 == '2000001') {
						loadingTextOption = false;
					} else if ((pCateCd1 == '1004737' && pCateCd2 == '1004795') || (pCateCd1 == '2000004' && pCateCd3 == '2000397')) {
						loadingTextOption = false;
					}
					
					if (loadingTextOption) {
						$("#loadingTextOption").remove();
					}
					*/
					
					$('#modalLoading').addClass('active');
					
					// 추천이력 로그 생성
					input.item_id = itemId;
					fnPrbmSuggestLog(input);
					
					var referrerSite = $("input[name=referrerSite]").val()
					
					// n초후 문제풀이 화면으로 이동
					setTimeout(function() {
						$("#frmItemCmm").attr("action","/ebs/ai/aib/ItemInfo"+continueWrtFlag+".ebs"+'?globalGradeCd='+$('input[name=globalGradeCd]').val());
						$("<input>",{type:'hidden',name:'itemId',value:itemId}).appendTo("#frmItemCmm");
						$("<input>",{type:'hidden',name:'cate_cd_1',value:pCateCd1}).appendTo("#frmItemCmm");
						$("<input>",{type:'hidden',name:'cate_cd_2',value:pCateCd2}).appendTo("#frmItemCmm");
						$("<input>",{type:'hidden',name:'cate_cd_3',value:pCateCd3}).appendTo("#frmItemCmm");
						$("<input>",{type:'hidden',name:'cate_cd_4',value:pCateCd4}).appendTo("#frmItemCmm");
						$("<input>",{type:'hidden',name:'cate_cd_5',value:pCateCd5}).appendTo("#frmItemCmm");
						$("<input>",{type:'hidden',name:'continueWrtFlag',value:continueWrtFlag}).appendTo("#frmItemCmm");
						$("<input>",{type:'hidden',name:'mainMenu',value:selectedMenuAr}).appendTo("#frmItemCmm");
						$("<input>",{type:'hidden',name:'groupHistNo',value:groupHistNo}).appendTo("#frmItemCmm");
						$("<input>",{type:'hidden',name:'sourceGbn',value:sourceGbn}).appendTo("#frmItemCmm");
						$("<input>",{type:'hidden',name:'itemType',value:itemType}).appendTo("#frmItemCmm");
						$("<input>",{type:'hidden',name:'referrerSite',value:referrerSite}).appendTo("#frmItemCmm");
						$("#frmItemCmm").submit();
					}, 1000);
					
					
				}
			}
		},
		error: function( e ) {
			alert("선택한 분류에 준비된 추천 문제를 모두 풀었습니다.\n'추천 문제 풀기' 영역을 다시 선택해주세요.");
			$( '#cate3' ).find( '.ok' ).click();
		}
	});
};

//추천이력 로그 생성
function fnPrbmSuggestLog(pData) {
	
	// 분류에서 문제추천 한 경우에는 배열이 생성되어 있고, 바로가기에서는 배열이 존재하지 않음
	var cateArray = pData.cateArray;
	if (typeof( cateArray ) === 'undefined' || cateArray == '') {
		cateArray = new Array();
		var cate_cd_2 = (typeof( pData.cate_cd_2 ) === 'undefined' || pData.cate_cd_2 == '') ? '' : pData.cate_cd_2;
		var cate_cd_3 = (typeof( pData.cate_cd_3 ) === 'undefined' || pData.cate_cd_3 == '') ? '' : pData.cate_cd_3.split(',')[0];
		var cate_cd_4 = (typeof( pData.cate_cd_4 ) === 'undefined' || pData.cate_cd_4 == '') ? '' : pData.cate_cd_4.split(',')[0];
		cateArray[0] = pData.cate_cd_1+"_"+cate_cd_2+"_"+cate_cd_3+"_"+cate_cd_4;
		pData.cateArray = cateArray;
	}

	// 이력이 복수 건일 경우
	var pEtc1 = (cateArray.length > 1)?'COMBO':'';
	
	$.each(cateArray,function(idx) {
		
		var cateArrayStr = cateArray[idx];
		var cdArray = cateArrayStr.split('_');
		
		var pParam = {
			itemId : pData.item_id
			,logType : (pData.logType == '')? 'sug' : pData.logType
			,cateCd1 : (cdArray.length > 0)? cdArray[0]:''
			,cateCd2 : (cdArray.length > 1)? cdArray[1]:''
			,cateCd3 : (cdArray.length > 2)? cdArray[2]:''
			,cateCd4 : (cdArray.length > 3)? cdArray[3]:''
			,cateCd5 : (cdArray.length > 4)? cdArray[4]:''
			,etc1 : pEtc1
		};
		
		$.ajax({
			url : '/ebs/ai/com/comLogging.ajax',
			type : 'post',
			data : pParam,
			success : function(data) {
	
			}, 
			error : function() {
				console.error('error');
			}
		});
	});
	
	// 추천이력 로그 생성
	$.cookie('_prbm_suggest_',JSON.stringify(pData),{expires:1,path:'/'});
}

// 문항뷰 화면 조절
function fnPrbmLoadSize() {
	var mm = window.matchMedia("screen and (max-width:821px)");
	if (mm.matches) {
		var itemHeight = 0;
		$.each($("#divItemPool dl"), function() {
			itemHeight += $(this).height();
		});
		$(".box-exam").css("height",itemHeight+150);
	} else {
		var itemHeight = 0;
		$.each($("#divItemPool dl"), function() {
			if (itemHeight < $(this).height()) itemHeight = $(this).height();
		});
		$(".box-exam").css("height",itemHeight+150);
	}
}

function fnRecommendSort(recomData) {
	var chkArray = [];
	
	for (var i=0 ; i < recomData.item.length ; i++) {
		chkArray.push(recomData.item[i]);
	}
	
	chkArray.sort(function(a, b) {
		return a.year > b.year ? -1 : a.year < b.year ? 1 : 0;
	});
	
	return chkArray[0];
}

// 샘플문항 추천
function fnNextSampleRecmd(selectedAr, flag) {

	var randomLen = 20;
	var applyNo ='7';
	//22분류체계일때
	if(selectedAr.length == 9 && (selectedAr.substring(0,2) == '22') ){
		randomLen = 5;
		applyNo ='22';
	}

	var groupHistItems = $("input[name=groupHistItems]").val();
	var itemId = $("input[name=itemId]").val();
	var groupHistNo = $("input[name=groupHistNo]").val();

	groupHistItems = (typeof(groupHistItems) === 'undefined') ? '' : groupHistItems;
	itemId = (typeof(itemId) === 'undefined') ? '' : itemId;
	groupHistNo = (typeof(groupHistNo) === 'undefined') ? '' : groupHistNo;
	
	if (groupHistItems == '') {
		groupHistItems = itemId;
	} else {
		groupHistItems += "," + itemId;
	}
	var groupArray = groupHistItems.split(',');
	randomLen = randomLen - groupArray.length;
	
	var selectedIndex = 1;

	//22분류체계 샘플문항이 5개 밖에없어서 로직추가 #20250411
	if (flag == 'itemRcmd' && !(applyNo =='22')) {
		selectedIndex = 5;

	} else {
		try{
			var rdInt = Math.floor(Math.random() * randomLen) +1;
			selectedIndex = rdInt;
		} catch(e) {
			console.error(e.message);
		}
	}

	$.ajax({
		url : '/ebs/ai/aib/selectGuestItemRecmd.ajax',
		type : 'post',
		data : {'selectedAr' : selectedAr, 'selectedIndex' : selectedIndex, 'groupItems' : groupHistItems},
		dataType : 'json',
		success : function(data) {
			if (data.item != null) {
				var itemId = data.item.itemId;
				var continueWrtFlag = 'continue';
				
				$("#frmItemCmm").attr("action","/ebs/ai/aib/ItemInfo"+continueWrtFlag+".ebs");
				$("<input>",{type:'hidden',name:'itemId',value:itemId}).appendTo("#frmItemCmm");
				$("<input>",{type:'hidden',name:'continueWrtFlag',value:continueWrtFlag}).appendTo("#frmItemCmm");
				$("<input>",{type:'hidden',name:'mainMenu',value:selectedAr}).appendTo("#frmItemCmm");
				$("<input>",{type:'hidden',name:'groupHistNo',value:groupHistNo}).appendTo("#frmItemCmm");
				$("<input>",{type:'hidden',name:'sourceGbn',value:'SAM'}).appendTo("#frmItemCmm");
				$("#frmItemCmm").submit();
			}
		}, 
		error : function() {
			console.error('error');
		}
	});

}

// 랜덤단원 추천
function fnNextRdmRecmd(pGroupHistNo, lastItemLevel, lastItemID) {
	var cookieInfo = $.cookie( '_rndPrbmContinue' );
	var randomArray;
	
	if ( typeof( cookieInfo ) !== 'undefined') {
		var _cookieInfo = JSON.parse(cookieInfo);
		randomArray = _cookieInfo.randomArray;
		var randomLen = randomArray.length;
		var selectedIndex = 1;
		try{
			var rdInt = Math.floor(Math.random() * randomLen) +1;
			selectedIndex = rdInt;
		} catch(e) {
			console.error(e.message);
		}
	} else {
		return false;
	}
	
	var pCateCdArr = randomArray[selectedIndex-1];
	var arrStr = pCateCdArr.split('_');
	
	var input = {};
	input.is_moc = 0;
	
	var arrStrLength = arrStr.length;
	input.cate_cd_1 = arrStr[0];
	if (arrStrLength == 2) {
		input.cate_cd_2 = arrStr[1];
	} else if (arrStrLength == 3) {
		input.cate_cd_3 = arrStr[2];
	} else if (arrStrLength == 4) {
		input.cate_cd_4 = arrStr[3];
	}
	input.last_item_level = lastItemLevel;
	input.item_id = lastItemID;
	input.is_correct = 0;
	input.level = 0;
	input.continueWrtFlag = 'continue';
	input.selectedMenuAr = arrStr[0];
	input.groupHistNo = pGroupHistNo;
	input.sourceGbn = 'RAN';
	
	fnRecommend(input);
}

//세션 연결용
function fnConnectSession() {
	if (stringUtils.isEmpty(window.connectSessionInterval)) {
		var keepSessionInterval = 1740000;//29분
		//var keepSessionInterval = 30000;//30초
		
		window.connectSessionInterval = setInterval(function() {
			$.ajax({
				url : '/ebs/xip/connectSession.ajax',
				type : 'POST',
				data : {},
				contentType: "application/x-www-form-urlencoded; charset=UTF-8",
				error : function() {
					if (stringUtils.isNotEmpty(window.connectSessionInterval)) {
						clearInterval(window.connectSessionInterval);
					}
				}
			});	
		},keepSessionInterval);						
	}
}

// 클리어모의고사 선별문제 랜덤추천
function fnNextRecmdRnd() {
	var itemId = $('#ItemID').val();
	var siteFlag = 'fullService';
	var groupHistNo = $("input[name=groupHistNo]").val();

	$("#frmItemCmm").attr("action","/ebs/ai/aib/retrievePrbmGateRnd.ebs");
	$("<input>",{type:'hidden',name:'itemId',value:itemId}).appendTo("#frmItemCmm");
	$("<input>",{type:'hidden',name:'siteFlag',value:siteFlag}).appendTo("#frmItemCmm");
	$("<input>",{type:'hidden',name:'groupHistNo',value:groupHistNo}).appendTo("#frmItemCmm");
	$("#frmItemCmm").submit();
}