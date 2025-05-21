/*-------------------------------------------------------------------
	분류순서
	- @Variables	: 전역변수
	- @Init			: 초기실행
	- @Settings		: 기본설정
	- @Utility		: 유틸기능
	- @Layout		: 레이아웃
	- @Components	: 컴포넌트
	- @Content		: 컨텐츠
-------------------------------------------------------------------*/
/*-------------------------------------------------------------------
	@Variables
-------------------------------------------------------------------*/
//Elements
var	$window			= null,
	$document		= null,
	$html			= null,
	$body			= null,
	$html_body		= null,
	$wrap			= null,
	$header			= null,
	$activeFocus	= null,
_;

//Devices
var isIOS			= browser.os == 'ios',
	isANDROID		= browser.os == 'android',
	isMOBILE		= browser.mobile == true,
	isPC			= browser.mobile == false,
	breakPC			= 1024,
	breakTA			= 720,
	isBreakPC		= function(){
		if (breakPC <= $(window).width()){
			return true;
		} else {
			return false;
		}
	}
	isBreakTA		= function(){
		if (breakPC > $(window).width() && breakTA <= $(window).width()){
			return true;
		} else {
			return false;
		}
	}
	isBreakMO		= function(){
		if (breakTA > $(window).width()){
			return true;
		} else {
			return false;
		}
	}
_;

/* 초기실행 (설정, 재실행) */
function set_UI(){
	/* Settings */
	setElements();
	setDevices();
	setEvents();
}
function init_UI(){
	//Layout
	gnbInit();
	mnbInit();
	lnbInit();
	navStickyInit()
	notiLayerInit();
	startLayerInit();
	navSnb();
	siteBg();
	tooltipInit();

	//Components
	modalInit();

	shadowTableInit();
	slider_under1024Init();

}

/*---------------------------------------------------------------
	@Settings
---------------------------------------------------------------*/
/* 엘리먼트 설정 */
function setElements(){
	$window		= $(window);
	$document	= $(document);
	$html		= $('html');
	$body		= $('body');
	$html_body	= $('html, body');
	$wrapper	= $('.wrap');
	$header		= $('header');
	$document.off('focusin.eleEvent click.eleEvent').on('focusin.eleEvent click.eleEvent', function(e){
		$activeFocus = $(e.target);
	})
}

/* 디바이스설정 - OS, Version, Browser */
function setDevices(){
	var cls = 'dv_';
	var browserDevice = function(){ return browser.mobile == true ? 'mobile' : 'pc' }
	var clsBrowser = ''
		+ cls + browser.name
		+ ' ' + cls + browser.name + browser.version
		+ ' ' + cls + browser.os
		+ ' ' + cls + browser.os + Math.floor(browser.osVersion)
		+ ' ' + cls + browserDevice();
	$body.addClass(clsBrowser);
}

/* 윈도우 커스텀이벤트설정 - scrollEnd, resizeEnd */
function setEvents(){
	var resizeEndTime, scrollEndTime;
	//Scroll
	$window.off('scroll.customEvent').on('scroll.customEvent', function(){
		clearTimeout(scrollEndTime); scrollEndTime = setTimeout(function(){ $window.trigger('scrollEnd') }, 100);
	});
	//Resize
	$window.off('resize.customEvent').on('resize.customEvent', function(){
		clearTimeout(resizeEndTime); resizeEndTime = setTimeout(function(){ $window.trigger('resizeEnd') }, 100);
	});
}


/*---------------------------------------------------------------
	@Utilites
---------------------------------------------------------------*/
//스트링을 스크립트 코드로 변환
function getNewFunction(str){
	var callback = (new Function(str))();
	return (new Function(callback))();
}

/*---------------------------------------------------------------
	@Layout
---------------------------------------------------------------*/
/* GNB Navigation Mobile */
var mySwiperGnb = null;
var clsSwiperGnb = '.gnb_wrap .nav ';
function swiperGnbEvent(current){
	$(window).off('resizeEnd.mySwiperGnb').on('resizeEnd.mySwiperGnb', function(){
		if ($(window).width() < breakPC) {
			if (current > -1){
				mySwiperGnb.update({initialSlide: current});
			}
		}
	});
	$(document).off('click.mySwiperGnb').on('click.mySwiperGnb', clsSwiperGnb +' .swiper-slide', function(e){
		swiperGnbReset($(this).index());
	})
}
function swiperGnbReset(current){
	if (current > -1){
		$(clsSwiperGnb).addClass('is-swiper').find('.swiper-slide').find('>a').removeClass('on');
		$(clsSwiperGnb).addClass('is-swiper').find('.swiper-slide').eq(current).find('>a').addClass('on');
	}
}
/*function swiperGnbAction(idx){
	var current = idx;
	mySwiperGnb = new Swiper(clsSwiperGnb, {
		// initialSlide: current,
		slidesPerView: 'auto',
		freeMode: true,
		slideToClickedSlide: true,
		// centeredSlides: true,
		// centeredSlidesBounds: true,
		navigation: false,
		// navigation: {
		// 	nextEl: clsSwiperGnb + '.swiper-button-next',
		// 	prevEl: clsSwiperGnb + '.swiper-button-prev',
		// },
		// breakpoints: {
		// 	961 : {
		// 		centeredSlides: false,
		// 		centeredSlidesBounds: false,
		// 	},
		// },
	});
	if (current > -1){
		mySwiperGnb.update({initialSlide: current})
	}
	swiperGnbEvent(current);
	swiperGnbReset(current);
}*/

/* GNB Navigation PC */
function gnbInit(){
	// resize: 브라우저 창 너비의 변경된 값을 width 변수에 저장
	if ($('.gnb_wrap').length){
		$(window).resize(function () {
			var width = $(window).width();
			if (width>=breakPC) {
				if (mySwiperGnb != null) {
					mySwiperGnb.destroy();
					mySwiperGnb = null;
				}
				gnbUpdate();
				gnbEvnet();
			} else {
				if (mySwiperGnb == null) {
					gnbMobile();
				}
			}
		});
		$(window).trigger("resize");
	}
}
function gnbUpdate(){
	var $depth = $('div.gnb_wrap div.nav ul.depth');
	var maxHei = 0;
	for (var i = 0; i < $depth.length; i++){
		if (maxHei < $depth.eq(i).outerHeight()){
			maxHei = $depth.eq(i).outerHeight();
		}
	}
	$('div.gnb_wrap').data({'active-height':maxHei});
}
function gnbEvnet(){
	var $gnb_wrap = $('div.gnb_wrap');
	var $inner = $gnb_wrap.find('.inner');
	var $bgDepth = $gnb_wrap.find('.bg_depth');
	var gapHei = 30;
	var activeHei = $gnb_wrap.data('active-height') + gapHei;
	var defaultHei = $gnb_wrap.height();

	/*  gnb */
	$gnb_wrap.off('mouseenter focusin').on('mouseenter focusin',function(){
		$inner.css('height', (activeHei+defaultHei)+'px');
		$bgDepth.css({'height':(activeHei)+'px','min-height': '382px'});//배너 높이값 고정
		$bgDepth.addClass('bg_depth_hover');
		$gnb_wrap.addClass('on');
	});
	$gnb_wrap.off('mouseleave').on('mouseleave',function(){
		$inner.css('height', '100%');
		$bgDepth.css({'height': 0,'min-height': 0});//배너 높이값 고정
		$bgDepth.removeClass('bg_depth_hover');
		$gnb_wrap.removeClass('on');
	});

	$document.off('click.gnbEvent focusin.gnbEvent').on('click.gnbEvent focusin.gnbEvent', function(e){
		if ($(e.target).closest('.gnb_wrap').length == 0){
			$gnb_wrap.removeClass('active');
		}
	})
}
function gnbMobile(){
	var $leNav = $('div.gnb_wrap .nav');
	var $leNavLinkOn = $leNav.find('>ul>li>a.on');
	var idx = $leNavLinkOn.parent().index();
	//swiperGnbAction(idx);
	/*
	var $leNav = $('div.gnb_wrap .le_nav');
	var $leNavLinkOn = $leNav.find('>ul>li>a.on');
	var gapLeft = parseInt($('.gnb_wrap .inner').css('padding-left'));
	if ($leNavLinkOn.length) {
		var posX = $leNavLinkOn.parent().offset().left - gapLeft + $leNav.scrollLeft();
		console.log(posX);
		$leNav.scrollLeft(posX);
	}
	*/
}

/* LNB Navigation */
function lnbInit(){
	$('.menu_list .depth > ul').each(function(){
		$(this).prev('a').addClass('on');
	})
	$document.off('click.lnbEvent').on('click.lnbEvent', '.menu_list .depth > a', function(e){
		$(this).toggleClass('on').next().stop().slideToggle('fast');
	});
}

/* MNB Navigation */
function mnbOpen(){
	$('html').addClass('mm-opened');
	$('body').addClass('no_scroll');
	$('.dim').fadeIn(200);
	$('.dim').css({'height':$(window).height(),'width':$(window).width()});
	$('.mobile_menu').animate({'left':'0px'},300,function(){
		$(this).addClass('act');
	});
};
function mnbClose(){
	$('body').removeClass('no_scroll');
	$('.dim').fadeOut(200);
	$('.dim').hide().removeAttr('style');
	$('.mobile_menu').stop().animate({'left':'-100%'},300,function(){
		$(this).removeClass('act');
		$('html').removeClass('mm-opened');
	});
};
function mnbInit(){
	$('header .all_menu').click(mnbOpen);
	$('.mobile_menu_close').click(mnbClose);
	$('.dim').bind('touchstart click', function() {
		mnbClose();
		return false;
	});

	$('.menu_area li.dep01 > div').addClass('submenu_div');
	$('.menu_area').off('click', '.dep_menu li.dep01 a.dep01').on('click', '.dep_menu li.dep01 a.dep01' , function(){
		$(this).parent().addClass('on').siblings().removeClass('on');
		gnbScrollFunc(true);
	});

	var gnbScrollFunc = function(flag) {		// ios bounce scroll prevent!!
		var __div = $('.menu_area').find('li.dep01.on > div');
		var _div = $('.menu_area').find('li.dep01 > div');
		__div.find('a:first').focus().blur();
		$(document).off('mousedown.ft touchstart.ft mousemove.ft touchmove.ft');
		__div.off('mousedown.ft touchstart.ft mousemove.ft touchmove.ft');
		if ( !window.navigator.userAgent.toLowerCase().match(/ipad|iphone/) ) {
			_div.stop().scrollTop(0);
			return false; // iphone, ipad인 경우만 touch event 실행
		} else {
			_div.stop().scrollTop(0);
			__div.addClass('has_scroll');
		}
		_div.off('scroll').on('scroll', function(e) {
			if ( $(this).scrollTop() <= 10 ) {
				$(this).scrollTop(10);
			} else if ( $(this).scrollTop() >= this.scrollHeight-$(this).outerHeight()-10 ) {
				$(this).scrollTop( this.scrollHeight-$(this).outerHeight()-10 );
			}
		});
	};
}

/* Nav Sticky */
function navStickyInit(){
	/* sticky bar */
	if( $("nav").offset() ){

		$(window).on('resize, scroll', function() {
			var navTop = $("header").offset().top + $("header").outerHeight();
			var scrTop = $(this).scrollTop();
			if(navTop <= scrTop) {
				$("nav").addClass("sticky");
			} else {
				$("nav").removeClass("sticky");
			}
		})
	}

	/* layer modal */
	$document.off('click.layerOpen').on('click.layerOpen', '.layer_full_open', function(e){
		e.preventDefault();
		$(".layer_full").stop().fadeIn(300);
	});
	$document.off('click.layerClose').on('click.layerClose', '.layer_full .close', function(e){
		e.preventDefault();
		$(".layer_full").stop().fadeOut(300);
	});
}

/* Snb */
function navSnb(){
	$(".snb_wrap .title").click(function(){
		if($(".snb_wrap").hasClass("on") === true) {
			$(this).parents(".snb_wrap").removeClass("on");
		}else{
			$(this).parents(".snb_wrap").addClass("on");
		}
	});
}

/* siteBg */
function siteBg(){
	$('.btn_white').click(function(){
		$('body').addClass('white_mode');
		$('.btn_black').removeClass('off');
		$(this).addClass('off');
		//$.cookie('_skin_saved','style_white',{expires:365,path:'/'});
	});
	$('.btn_black').click(function(){
		$('body').removeClass('white_mode');
		$('.btn_white').removeClass('off');
		$(this).addClass('off');
		//$.cookie('_skin_saved','style_dark',{expires:365,path:'/'});
	});
}

function notiLayerInit(){
	$document.off('click.notiLayer').on('click.notiLayer', '.btn_noti_close', function(e){
		$(this).closest('.noti_layer').removeClass('active');
		if ($('.noti_layer.active').length == 0){
			$('.noti_layer_wrap').removeClass('active');
		}
	});
}

function startLayerInit(){
	$document.off('click.startLayer').on('click.startLayer', '.btn_start_close', function(e){
		$(this).closest('.start_layer').removeClass('active');
		if ($('.start_layer.active').length == 0){
			$('.start_layer_wrap').removeClass('active');
		}
	});
}

/*---------------------------------------------------------------
	@Components
---------------------------------------------------------------*/
/* Modal : 'data-modal-id', id 연결방식 */
function modalInit(){
	$document.off('click.modalOpen').on('click.modalOpen', '.modal_btn', function(e){
		e.preventDefault();
		var id = $(this).data('modal-id');
		modalOpen(id);
	});
	$document.off('click.modalClose').on('click.modalClose', '.modal_close', function(e){
		e.preventDefault();
		var id = $(this).closest('.modal_wrap').attr('id');
		modalClose(id);
	});
}

function modalResize($obj){
	$obj.filter('.active').each(function(){
		var id = $(this);
		var $modalWrap = $(this);
		var $modal = $(this).find('.modal');
		var $modalContainer = $modal.find('.modal_container');
		var $modalContent = $modal.find('.modal_content');
		var $modalInner = $modal.find('.inner_scroll');
		if ($modalContent.hasClass('has_pad')){
			$modalContent.removeClass('has_pad');
			$modalContainer.addClass('has_pad');
		}
		var resizing = function(){
			var gap = parseInt($modalWrap.css('padding-top')) + parseInt($modalWrap.css('padding-bottom')) + 2;
			var isContainerGap = function(){ return ($modalContent.outerHeight() + 2) < $modalContainer.outerHeight() }
			var isModalGap = function(){ return $window.height() - $modal.outerHeight() > gap }

			//기본스크롤
			//isContainerGap 본문의 빈 공간이 있는지, isModalGap 모달이 늘어날 공간이 있는지
			// console.log(isContainerGap(), isModalGap(), $window.height() - $modal.outerHeight() gap);
			console.log(id);
			if (isContainerGap() == false && isModalGap() == false){
				$modal.css('height', 'auto');
				$modalContainer.css('height', $modalContent.height() + 'px');
			} else if (isContainerGap() == false && isModalGap() == true) {
				$modal.css('height', 'auto');
				$modalContainer.removeAttr('style');
			} else if (isContainerGap() == true && isModalGap() == false) {
				$modal.css('height', '100%');
				$modalContainer.css('height', $modalContent.height() + 'px');
			} else if (isContainerGap() == true && isModalGap() == true) {
				$modal.css('height', 'auto');
				$modalContainer.removeAttr('style');
			}

			//내부스크롤
			if ($modalInner.length){
				$modalContainer.addClass('has_scroll');
				var innerH = $modalContainer.height() - ($modalInner.offset().top - $modalContainer.offset().top) + ($window.height() - gap - $modal.outerHeight());
				$modalInner.css('max-height', innerH+'px');
				// console.log($modalInner.prop('scrollHeight'), innerH);
				if ($modalInner.prop('scrollHeight') <= innerH){
					$modalInner.css('overflow-y', 'hidden');
				} else {
					$modalInner.css('overflow-y', 'auto');
				}
			}

			//마무리
			if (isContainerGap() == false){
				$modalContainer.css('height', ($modalContent.height() + 2) + 'px');
			}

			// console.log(isContainerGap(), isModalGap());
			// console.log($window.height() - $modal.outerHeight(), gap);
			// console.log($modalContent.outerHeight(), $modalContainer.height());
		}
		$window.off('resize.'+id).on('resize.'+id, function(){
			resizing();
		})
		resizing();
	})
}

function modalOpen(id){
	var $modal = $('#' + id);
	//$html.hasClass('modal_open') && $('.modal_wrap').removeClass('active'); // 전환팝업시 사용
	//$html.addClass('modal_open'); 2021-05-03 개발 수정
	if($html != null){
		$html.addClass('modal_open');
	}
	$modal.addClass('active');
	if (browser.name == "ie"){ modalResize($modal) }
	if ($modal.find('.modal_all_teacher').length) { modalResize($modal) }
	$body.addClass('has_modal');
	shadowTableInit();
}
function modalClose(id){
	var $modal = $('#' + id);
	$modal.closest('.modal_wrap').removeClass('active');
	$html.removeClass('modal_open');
	$(".popupArea").html("");
	$window.off('resize.modalInnerScroll');
	if ($('.modal_wrap.active').length == 0){
		$body.removeClass('has_modal');
	}
}

/* Table Scroll Shadow */
function shadowTableInit(){
	$('.table_scroll, .table_scroll2:not(.table_fixed), .table_scroll3').not('.has_shadow').each(function(){
		$(this).wrap('<div class="table_scroll_wrap"></div>');
		$(this).off('resize.axisResize scroll.axisScroll').on('resize.axisResize scroll.axisScroll', function(){
			shadowTableUpdate($(this));
		})
		shadowTableUpdate($(this));
	}).addClass('has_shadow');
}
function shadowTableUpdate($ele){
	//기본변수
	var $table = $ele.find('table'),
	$eleWrap = $ele.parent('.table_scroll_wrap'),
	groupW = $ele.width(),
	tableW = $table.width(),
	scrollL = $ele.scrollLeft();

	//조건변수
	var isStarted = scrollL == 0,
	isEnded = (tableW - groupW - scrollL) == 0;
	// console.log(tableW - groupW - scrollL);
	isStarted ? $eleWrap.addClass('is_started') : $eleWrap.removeClass('is_started');
	isEnded ? $eleWrap.addClass('is_ended') : $eleWrap.removeClass('is_ended');
	setTimeout(function(){
		console.log(tableW, groupW, scrollL);
	}, 2000);
}

function allLectureSlideInit(){
	$('.ranking_wrap').not('.is_slicked').each(function(){
		if ($(this).find('.slide_item').length > 1 ){
			$(this).slick({
				infinite:true,
				arrows: true,
				slidesToShow: 1,
				slidesToScroll: 1,
				speed: 600,
				focusOnChange: true,
				accessibility: true,
				responsive: [
				  {
					breakpoint: breakPC,
					settings: {
					  slidesToShow: 1
					}
				  },
				  {
					breakpoint: breakTA,
					settings: {
					  slidesToShow: 1
					}
				  }
				]
			});
		}
	}).addClass('is_slicked');
}

// 데스크탑 미만 사이즈 슬라이더 토글 ()
function slider_under1024Init(){
	$('.slider_under1024 .slider').each(function () {
		//var notDesktop = false;
		var isTeachSlide = false;
		var $this = $(this);
		$(window).on('resizeEnd', function () {
			var $winWidth = $(this).width();
			if ($winWidth < 1024) {
				if (isTeachSlide == false) {
					$this.slick({
						infinite: true,
						speed: 600,
						slidesToShow: 2,
						slidesToScroll: 1,
						arrows: false,
						responsive: [{
							breakpoint: 376,
							settings: {
								slidesToShow: 1,
								slidesToScroll: 1
							}
						}]
					});
					isTeachSlide = true;
				}
			} else {
				if (isTeachSlide == true) {
					$this.slick('unslick');
					isTeachSlide = false;
				}
			}
		});
		$(window).trigger('resizeEnd');
	});
}

/* top버튼 */
$(function(){
	$(window).scroll(function () {
		if ($(this).scrollTop() > 50) {
			$('.top').fadeIn();
		} else {
			$('.top').fadeOut();
		}
	});
	$('.top').click(function () {
		$('body,html').animate({
			scrollTop: 0
		}, 500);
		return false;
	});

});

/* Tooltip */
function tooltipInit(){
	$(document).off('click.tooltipOpen').on('click.tooltipOpen', '.btn_tooltip', function(e){
		$(this).closest('.tooltip').addClass('on');
	})
	$(document).off('click.tooltipClose').on('click.tooltipClose', '.tooltip .btn_close', function(e){
		$(this).closest('.tooltip').removeClass('on');
	})
	$(document).off('click.tooltipDoc focusin.tooltipDoc').on('click.tooltipDoc focusin.tooltipDoc', function(e){
		if ($('.tooltip.on').has(e.target).length === 0){
			$('.tooltip.on').removeClass('on');
		}
	});
}
$.datepicker.setDefaults({
	dateFormat: 'yy-mm-dd',
	prevText: '이전 달',
	nextText: '다음 달',
	monthNames: ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월'],
	monthNamesShort: ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월'],
	dayNames: ['일', '월', '화', '수', '목', '금', '토'],
	dayNamesShort: ['일', '월', '화', '수', '목', '금', '토'],
	dayNamesMin: ['일', '월', '화', '수', '목', '금', '토'],
	showMonthAfterYear: true,
	yearSuffix: '년'
});
$( function() {
    $( '.datepicker').datepicker();
});

/* 인공지능 리포트 셀렉트 */
$( function() {
	$('.box-select-class .btn-select button').on('click',function(){
		if($(this).closest('.box-inner').hasClass('on') == 0){
			$('.box-select-class .box-inner').removeClass('on')
			$(this).closest('.box-inner').addClass('on')
		}else{
			$(this).closest('.box-inner').removeClass('on')
		}
	});
});


$(function(){
	set_UI();
	init_UI();
})