/********************************************************************************
Auth : 김영우
Desc : 시험지관련 프로그램
================================================================================
Date					Desc								Auth 
2021. 09. 07			최초작성							김영우 
********************************************************************************/
var EBS_CONTEXTROOT = '/';
var MNGT_POPS = new Array();
var contextPath = function(to){
	to = to || 2;
	try{
		return location.pathname.split('/').slice(0,to).join('/'); 
	}catch(e){
		return '/';
	}
};

var resourcesContextPath = function(){
	return contextPath(1)+'/cmm_resource/';
};

(function($){	
	var xipObj = null;
	var mathJaxRoot = 'xip/mathJax/';
	var defaults = {
		root : null,
		print : null,
		resourcesRoot 		: contextPath()+'_resource/',
		cmmResourcesRoot 	: resourcesContextPath()+'js/',
	};
	var EBS_XIP_INIT = {
		libs : {
			root : defaults.cmmResourcesRoot+'xip/',
			list : [
				{id : 'commonEbsXip', 	url : 'common.ebs.xip.v2', 					external : false},
				{id : 'uiEbsXip', 		url : 'ui.ebs.xip.v2', 						external : false},
				{id : 'ebsXipReport', 	url : 'report.ebs.xip.v2', 					external : false},
				{id : 'ifEbsXip',		url : 'if.ebs.xip.v2', 						external : false},
				{id : 'base64', 		url : 'base64', 							external : true},
				{id : 'mathJax', 		url : mathJaxRoot+'MathJax', 				external : true, 'init' : 'mathJaxInit'},
				{id : 'mathJaxConfig', 	url : mathJaxRoot+'config/TeX-MML-AM_CHTML',external : true},
			],
			Import : function(){
				var _this = this;
				_this.mathJaxConfig()
				var _arr = $.map(_this.list, function(lib){
					var rootUri = lib.external ? defaults.cmmResourcesRoot : _this.root;
					
					var src = rootUri+[lib.url,'js'].join('\.');
					if(stringUtils.isNotEmpty(lib.params)){
						src += ('?'+lib.params)
					}
					
					if(stringUtils.isEmpty(window['loaded'+lib.id])){
						return $.getScript(src,function(){
							try{
								
								if(lib.id === 'commonEbsXip'){
									window['xipConstans'] 		= $.xipCommon.Constans;
									window['xipCommonUtils'] 	= $.xipCommon.FN;
									window['xipCommonUI'] 		= $.xipCommon.UI;									
								}
								
								if(lib.init){
									if(typeof lib.init === 'string'){
										_this[lib.init]();
									}else{
										lib.init();
									}
								}
								window['loaded'+lib.id] = 'loaded';
							}catch(e){
								console.error('======================= loaded'+lib.id);
								console.error(e)
							}
						})						
					}else{return '';}
				});
				
				_arr.push($.Deferred(function(deferred){
					$(deferred.resolve);
				}));
				
				return $.when.apply($, _arr);
			},
			mathJaxInit : function(){
				//메뉴 한글로 변환
				MathJax.Localization.locale = 'ko';
				//MathJax Root 경로 설정
				MathJax.Ajax.config.root= defaults.cmmResourcesRoot + mathJaxRoot;
			},
			mathJaxConfig : function(){
				try{
					//MathJax Config설정
					if(!objectUtils.isElement($('#mathJaxTextConfig'))){
						var config = 'MathJax.Hub.Config({messageStyle: "simple","HTML-CSS": {noReflows: false,showMathMenu: false,linebreaks: { automatic: true, width: "430px"},tooltip: {delayPost: 600,delayClear: 600,offsetY: -10},scale: 110}});\n';
						config += 'MathJax.Hub.Config({tex2jax: {inlineMath: [[\'$\', \'$\'],[\'[!\', \'!]\']]}});';
						$('head').append($('<script />',{'id' : 'mathJaxTextConfig','type':'text/x-mathjax-config'}).append(config));						
					}					
				}catch(mje){
					console.error(mje)
				}
			}
		},
		Init : function(opts){
			var defaultOpts = {
				isRemove : false
			};
			$.extend(defaultOpts, opts);
			
			var $selector = $(defaults.root);
			var _this = this;
			
			return new Promise(function(resolve, reject){
				if(objectUtils.isElement($selector)){
					_this.libs.Import()
					.done(function(){
						if(xipCommonUtils.siteInfo.isRealSrv()){
							var fn = function(){};
							window.console = {log:fn,info:fn,debug:fn,error:fn,warn:fn,time:fn,timeEnd:fn};
						}
						if(defaultOpts.isRemove){
							$($selector).find('*').remove();
						}
						resolve()							
					})
					.fail(function(error){
						console.error(error);
						reject()
					});
				}else{
					reject();
				}			
			})
		}
	};
	
	var XIP = {
		Init : function(opts){
			return new Promise(function(resolve){
				EBS_XIP_INIT.Init(opts)
				.then(function(){
					resolve();
				}).catch(function(){
					resolve();
				});				
			});
		},
		Preview : function(opts){
			opts = $.extend({
				itemId : ''
				,itemIdList : []
				,isPopExplanInput : true //#20230105 #미리보기인풋
			},opts);			
			
			this.Init()
			.then(function(){
				$(defaults.root).xipUI().Paper.preview(opts);
			});
		},
		StudyMode : {
			wrongNote : function(request){
				request = $.extend({
					isStudyMode : true
					,isMyWrongNote : true
					,isStudyAllMode : false
					,isShowCorrect	: true
				},request);
				XIP.SolvePaper.open(request)
			},
			explanation : function(request){
				request = $.extend({
					isStudyMode : true
					,isMyWrongNote : false
					,isStudyAllMode : true
					,isShowCorrect	: true
				},request);				
				XIP.SolvePaper.open(request)
			}
		},
		SolveSingle : {
			open : function(opts){
				var _super = XIP;
				var initOpts = $.extend({
					itemId 		: ''
					,cate_cd_1 	: ''
					,cate_cd_2 	: ''
					,cate_cd_3 	: ''
					,cate_cd_4 	: ''
					,cate_cd_5 	: ''
					,score		: '5'
					,nextItems	: new Array()
					,isContinue : false
					,isRetry 	: false
					,selectedCate : {}
					,justOne	: false
					,isPopularity : false
					,siteId : ''
				},opts);
				
				_super.Init()
				.then(function(){
					initOpts.itemId = stringUtils.nvl(initOpts.itemId);
					initOpts.score 	= stringUtils.nvl(String(parseInt(initOpts.score)),'5');
					var requiredKeys = ['itemId','cate_cd_1'];
					
					if(!xipCommonUtils.checkRequired.all(requiredKeys, initOpts)){
						alert(xipConstans.MSG.badRequest);
						return;
					}
					var page = 'solveSingle';
					if(initOpts.isRetry){
						page = 'retry'+page;
					}
					if(initOpts.isContinue){
						page += 'continue';
					}
					
					if(contextPath().includes('onestop') && (opts.siteId.toLowerCase().includes('jhs'))) {
						url = contextPath()+'/xip/mid/'+page+'.ebs';
					}else if(contextPath().includes('onestop') && (opts.siteId.toLowerCase().includes('hsc'))) {
						url = contextPath()+'/xip/hsc/'+page+'.ebs';					
					}else if(contextPath().includes('classical') && (opts.siteId.toLowerCase().includes('hsc'))) {
						url = contextPath()+'/xip/hsc/'+page+'.ebs';
					}else if(contextPath().includes('single') && (opts.siteId.toLowerCase().includes('jhs'))) {
						url = contextPath()+'/xip/mid/'+page+'.ebs';
					}else if(contextPath().includes('single') && (opts.siteId.toLowerCase().includes('hsc'))) {
						url = contextPath()+'/xip/hsc/'+page+'.ebs';					
					}else {
						url = contextPath()+'/xip/'+page+'.ebs';
					}				
					
					var submitForm = $('<form />', {
						action : url
						,method : 'POST'
					})
					.css({'display':'none'})
					.appendTo($('body'))
					
					try{
						Object.keys(initOpts).forEach(function(k){
							var _this_value = stringUtils.nvl(initOpts[k]);
							if(typeof _this_value != 'string'){
								initOpts[k] = stringUtils.convert.toStringParams(_this_value);
								_this_value = initOpts[k];
							}
							submitForm.append($('<input />',{'type' : 'hidden', 'name' : k, 'value' : _this_value}));
						});
						submitForm.append($('<input />',{'type' : 'hidden', 'name' : 'suffixSite', 'value' : xipCommonUtils.siteInfo.getSuffixSite()}));
						submitForm.append($('<input />',{'type' : 'hidden', 'name' : 'site', 'value' : xipCommonUtils.siteInfo.getCodeUpper()}));
					}catch(e){
						console.debug(e);
					}
					
					submitForm.submit();					
					submitForm.remove();
					
				});				
				
			},
			render : function(opts, success, fail){
				var _super = XIP;
				
				_super.Init()
				.then(function(){
					$(defaults.root).xipUI().Paper.solve(opts);
				})
				.then(function(){
					$.xipIf.rcmdEval.retrieve(opts.itemId)
					.then(function(point){
						if(success){
							success(point)
						}					
					})
					.catch(function(ee2){
						console.error(ee2);
					});
					
					$('button#btnSkipPrbm').show();
					
					if(stringUtils.isEmpty(window.connectSessionInterval)){
						window.connectSessionInterval = setInterval(function(){
							$.xipIf.Prbm.connectSession()	
						},xipConstans.keepSessionInterval);						
					}
				})
				.catch(function(ee3){
					console.error(ee3);
					if(fail){
						fail();
					}
				});
			}
		},
		SolvePaper : {
			open : function(request){
				var _super = XIP;
				_super.Init()
				.then(function(){
					var requiredKeys = ['paperId','title'];
					if(!xipCommonUtils.checkRequired.all(requiredKeys, request, true)){
						alert(xipConstans.MSG.badRequest);
						return;
					}
					
					try{
						if(stringUtils.isNotEmpty(MNGT_POPS)){
							MNGT_POPS.forEach(function(v){
								if(v.self){
									if(!v.self.closed) v.self.close();
								}								
							});
						}
					}catch(pe){
						console.debug(pe);
					}
					
					var popName = 'examAiPaper';
					var paperPop = null;
					var currentPage = false;
					
					try{
						if('Y'.equals(xipCommonUtils.siteInfo.isInSite())){
							if(!window.opener){
								throw '';
							}else{
								paperPop = window;
								currentPage = true;
							}
						}else if(request.fixDeviceMode){
							paperPop = window;
							currentPage = true;
						}else{
							throw '';
						}
					}catch(ee33){
						var thisAppType = '';
						var broswerInfo = navigator.userAgent;
		
						if(broswerInfo != null && (broswerInfo.indexOf("app-name/ebsprimary")>-1 || broswerInfo.indexOf("app-name/ebs-primary")>-1)){
							thisAppType = 'primary';
						}else if(broswerInfo != null && broswerInfo.indexOf("app-name/ebs-middle")>-1){
							thisAppType = 'mid';
						}
					
						if(thisAppType == 'primary' || thisAppType == 'mid'){
							paperPop = true;
						} else {
							paperPop = xipCommonUtils.pop.full({
								popName : popName
							});
						}
					}
					
					MNGT_POPS.push(paperPop);
					if(paperPop){
						var isMobile = false;
						
						if(request.hasOwnProperty('isMobile')){
							isMobile = request.isMobile;
						}else{
							isMobile = xipCommonUtils.isMobile();
							//#20221018 #모바일환경 width 768px 이상에서 PC 모드 #해설보기 기존유지
							var widthVal = window.outerWidth;
							if(isMobile && widthVal >= 744 && !request.isStudyMode){ //#모바일 시험지개편 768에서 744변경 고교 개편앱
								isMobile = false;
								request = $.extend({
									isOneColumnMode	: true
								}, request);
							} 
						}
						
						var url = contextPath()+'/xip/solvePaper.ebs';
						if(isMobile){
							$.extend(request,{'isMobile' : "true", 'isMobile2' : "true"})//#모바일 시험지개편 적용 #20240223
						}else{
							url = contextPath()+'/xip/solvePaper.ebs';
						}
						if(request.datas.fmySiteDsCd == "JHS"){
							url = url.replace("onestop", "mid");
						} else {
							url = url.replace("onestop", "hsc");
						}
						var submitForm = $('<form />', {
							action : url
							,method : 'POST'
							,target : currentPage ? '' : popName
						})
						.css({'display':'none'})
						.appendTo($('body'))
						
						try{
							
							request = $.extend({
								isStudyMode	: false
								,pMode : false
								,childrenUserId : ''
							}, request);
							
							//자녀 아이디가 없을경우 학부모 모드를 제거한다.
							if(stringUtils.isEmpty(request.childrenUserId)){
								request.pMode = false;
							}
							
							Object.keys(request).forEach(function(k){
								var _this_value = stringUtils.nvl(request[k]);
								if(typeof _this_value != 'string' || k == 'title'){
									request[k] = stringUtils.convert.toStringParams(_this_value);
								}
								
								submitForm.append($('<input />',{'type' : 'hidden', 'name' : k, 'value' : request[k]}));
							});
							submitForm.append($('<input />',{'type' : 'hidden', 'name' : 'suffixSite', 'value' : xipCommonUtils.siteInfo.getSuffixSite()}));
							submitForm.append($('<input />',{'type' : 'hidden', 'name' : 'site', 'value' : xipCommonUtils.siteInfo.getCodeUpper()}));
							submitForm.append($('<input />',{'type' : 'hidden', 'name' : 'requestOpts', 'value' :  stringUtils.convert.toStringParams(request)}));
						}catch(e){
							console.debug(e);
						}
						submitForm.submit();
						
						if (parseInt(navigator.appVersion) >= 4) {
							paperPop.window.focus(); 
						};
						
						submitForm.remove();
					}
				});
			},
			mobileToPc : function(requestOpts){
				var _this = this;
				if(stringUtils.isNotEmpty(requestOpts)){
					try{
						var requestOpts = stringUtils.convert.toObjectParams(requestOpts);
						requestOpts.isMobile = false;
						requestOpts.isMobile2 = false;	//#모바일 시험지개편 적용 #20240223
						requestOpts['fixDeviceMode'] = true;
					}catch(ce){
						console.error('=================================== change error ');
						console.error(ce)
					}
					
					var w = window.outerWidth;
					var h = window.outerHeight;
							
					if ( window.screen ) {
						w = screen.availWidth;
						h = screen.availHeight;
					};
					
					xipCommonUI.Progress.open({
						msg : 'PC버전으로 전환 합니다.'
						,css : {
						    'width'				: '630px'
					        ,'border' 			: '2px solid #000000'
							,'backgroundColor' 	: '#ffffff'
							,'font-size'		: '2rem'
							,'left'				: 'calc(50% - 315px)'
						}
						, blockcb : function(){
							window.resizeBy(w,h);
							_this.open(requestOpts);
						}
					});	
					
					
				}else{
					alert(xipConstans.MSG.badRequest);
				}
			},
			pcToMobile : function(requestOpts){
				var _this = this;
				if(stringUtils.isNotEmpty(requestOpts)){
					try{
						var requestOpts = stringUtils.convert.toObjectParams(requestOpts);
						requestOpts.isMobile = true;
						requestOpts.isMobile2 = true;	//#모바일 시험지개편 적용 #20240223
						requestOpts.pcToMobile = true;	//20220426
					}catch(ce){
						console.error('=================================== change error ');
						console.error(ce)
					}
					
					xipCommonUI.Progress.open({
						msg : '모바일 버전으로 전환 합니다.'
						,css : {
						    'width'				: '630px'
					        ,'border' 			: '2px solid #000000'
							,'backgroundColor' 	: '#ffffff'
							,'font-size'		: '2rem'
							,'left'				: 'calc(50% - 315px)'
						}
						, blockcb : function(){
							_this.open(requestOpts);
						}
					});	
				}else{
					alert(xipConstans.MSG.badRequest);
				}
			},
			render : function(request){
				var _this = this;	
				var _super = XIP;
				return new Promise(function(resolve){
					
					if(request.isStudyMode){
						$('ul.viewModeTabs > li.studyTabs').removeClass('on');
						if(request.isMyWrongNote){
							$('ul.viewModeTabs > li.myWrongTab').addClass('on');
						}else if(request.isStudyAllMode){
							$('ul.viewModeTabs > li.explainTab').addClass('on')
						}
					};
					
					_super.Init()
					.then(function(){
						_this.pagination.common(request)
						.then(function(res){
							var opts = $.extend({
								itemId 			: ''
								,paperId 		: ''
								,paperType 		: xipConstans.PaperDisplayType.justOnePrbm
								,isPrint 		: false
								,isCorrectRate 	: false
								,renderXipInfo	: true
								,isMoc			: '1'
								,isStudyMode	: false
								,solveYn		: false
								,isMobile		: false
								,isReadonly		: false
								,pMode			: false
								,childrenUserId	: ''								
							},res);
							
							if(!opts.isMobile && opts.isStudyMode){
								opts.divItemPoolName = 'studyScrollBox';
							}
							
							if(opts.isStudyMode){
								opts.isShowCorrect	= true;
							}
							
							$(defaults.root).xipUI().Paper.solve(opts);
							resolve();							
						})
						.catch(function(err2){
							console.error(err2);
						});
						
						if(stringUtils.isEmpty(window.connectSessionInterval)){
							window.connectSessionInterval = setInterval(function(){
								$.xipIf.Prbm.connectSession()	
							},xipConstans.keepSessionInterval);						
						}						
					})
					.then(function(){
						if(opener){
							var c = setInterval(function(){
								try{
									if(opener.location.href.indexOf('/sso/logout?') != -1){
										clearInterval(c)
										window.self.close();
									}
								}catch(ive){
									clearInterval(c)
								}
							},xipConstans.popChkInteval)
						}
					})					
					.catch(function(err){
						console.error('==================== render lib error ==================')
						console.error(err)
					})								
				});
			},
			pagination : {
				common : function(request){
					return new Promise(function(resolve){
						var opts = $.extend({
							isPrint : false
						},request,{divItemPoolName : 'contents'});
						if(!opts.isPrint){
							var scrollTarget = $('div.scrollbox:not(div.omrbox > div.scrollbox):visible');
							if(objectUtils.isElement(scrollTarget)){
								$(scrollTarget).animate({scrollTop:0},300, function(){
									resolve(opts)
								});							
							}else{
								resolve(opts);
							}
						}else{
							resolve(opts)							
						}
					});
				},
				next : function(request){
					request.pageNo = 1;
					this.move(request);
				},
				prev : function(request){
					request.pageNo = -1;
					this.move(request);
				},
				move : function(request){
					
					request = $.extend({
						paperType : xipConstans.PaperDisplayType.oneColumn
					}, request);
					
					if(request.paperType.pageRender && request.paperType.isPaging){
						this.common(request)
						.then(function(res){
							$(defaults.root).xipUI().Paper.refreshPaper(res);					
						})
						.then(function(){
							$('img').map(function(i,v){
								if(objectUtils.isElement(v)){
									//#20221215 #시험지 로고 인벤트 유지
									if(v.getAttribute('id') !== 'danchooLogo'){
										$(v).off('click');
										$(v).on('click', function(){
											xipCommonUI.ImgModal.open($(this).clone());
										})
									}
								}
							});
							$('#explanationArea, #paperArea').scrollTop(0); //#20250319 문한이동 스크롤
						})
						.catch(function(err){
							console.error(err);
						})				
					}else{
						var pn = Number(stringUtils.nvl(request.setPage, request.pageNo));
						$('dd.itemlist[isquestion=true]:eq('+(pn-1)+')')[0].scrollIntoView({behavior:'smooth'})
					}
				},
				moveItmeSet : function(request){//#20230613 #2단보기페이징
					
					request = $.extend({
						paperType : xipConstans.PaperDisplayType.oneColumn
					}, request);
					
					if(request.paperType.pageRender && request.paperType.isPaging){
						this.common(request)
						.then(function(res){
							$(defaults.root).xipUI().Paper.refreshPaper(res);					
						})
						.then(function(){
							$('img').map(function(i,v){
								if(objectUtils.isElement(v)){
									//#20221215 #시험지 로고 인벤트 유지
									if(v.getAttribute('id') !== 'danchooLogo'){
										$(v).off('click');
										$(v).on('click', function(){
											xipCommonUI.ImgModal.open($(this).clone());
										})
									}
								}
							});
						})
						.catch(function(err){
							console.error(err);
						})				
					}else{
						var pn = Number(stringUtils.nvl(request.setPage, request.pageNo));
						$('dd.itemlist[isquestion=true]:eq('+(pn-1)+')')[0].scrollIntoView({behavior:'smooth'})
					}
				}
			},
			isFinish : function(){
				return $(defaults.root).xipUI().Paper.solveCheck.isFinish();
			},
			answerResult : function(){
				return $(defaults.root).xipUI().Paper.solveCheck.answerResult();
			},
			saveTempAnswer : function(params){
				try{
					var paperDatas = $.getPaperDatas();
					
					params = $.extend({
						paperId 	: paperDatas.paperId
						, answer 	: stringUtils.convert.toStringParams($.userAnswerData())
						, isMoc		: stringUtils.nvl(paperDatas.requestOpts.isMoc,'1')
					}, params);
					
					if(stringUtils.isNotEmpty(params)){
						var confirmTxt = xipConstans.MSG.confirmSaveTempAnswer;
						
						//#미니모의고사 #20230912
						if(paperDatas.requestOpts.isMoc == '6'){
							confirmTxt = '임시저장 하시겠습니까?\r\n임시저장을 하면 시험지 재응시 시\r\n기존에 선택한 정답 정보를 불러올 수 있습니다.';
						}
						
						if(confirm(confirmTxt)){
							$.xipIf.Solve.userAnswerTemp.insert(params)
							.then(function(result){
								try{
									if(result.inserted === 1){
										var successMsg = xipConstans.MSG.successSaveTempAnswer;
										if(xipConstans.SiteType.HSC.code.equals($thisSite)){
											successMsg = xipConstans.MSG.successSaveTempAnswerHSC;
											if(paperDatas.requestOpts.isMoc == '6'){
												successMsg = '임시저장 하였습니다.'
											}
										}
										if(paperDatas.requestOpts.isMoc === '3'){
											successMsg = successMsg.split('\r\n')[0];
										}
										if(paperDatas.requestOpts.isMoc === '4'){
											successMsg = successMsg.split('\r\n')[0];
										}
										if(paperDatas.requestOpts.isMoc === '5'){	//#20230718 #수해력
											successMsg = successMsg.split('\r\n')[0];
										}
										alert(successMsg);
									}else{
										throw '';
									}
								}catch(e){
									alert(xipConstans.AjaxState.FAIL.msg)
								}
							})
							.catch(function(ee3){
								console.debug(ee3);
							})
						}
					}else{
						throw 'empty parameter';
					}
				}catch(tae){
					console.error(tae)
					alert(xipConstans.MSG.badRequest);
				}
			},
			allClose : function(){
				if(stringUtils.isNotEmpty(MNGT_POPS) && MNGT_POPS.length > 0){
					MNGT_POPS.forEach(function(v){
						if(v.self){
							if(!v.self.closed) v.self.close();
						}								
					});					
				}
			},
			hscAppVodPlay : function(itemId){//#모바일 시험지개편 #20231203
				$.xipIf.ML.explanationVod({
					'item_id' : itemId
				}).then(function(vodInfo){
					var vodData = vodInfo.item[0];
					var broswerInfo = navigator.userAgent;
					var appHscType = '';
					
					if(broswerInfo != null && broswerInfo.indexOf("EbsiVersion")>-1){
						appHscType = 'android'; 
					}
					
					if(broswerInfo != null && broswerInfo.indexOf("EbsiAppVersion")>-1){
						appHscType = 'ios'; 
					}
					
					$.xipUI().UI.module.vod.hscAppVod(vodData, appHscType);
				})
				.catch(function(cee){
					alert('해설강의를 제공하지 않는 문제입니다.');
					console.error(cee);
				})
			},
			finishTestVodPlay : function(itemId){//#모바일 시험지개편 #20231203
				$.xipIf.ML.explanationVod({
					'item_id' : itemId
				}).then(function(vodInfo){
					$.xipUI().UI.module.vod.finishTestVod(vodInfo);
				})
				.catch(function(cee){
					alert('해설강의를 제공하지 않는 문제입니다.');
					console.error(cee);
				})
			}
		},		
		SolveSingleResult : function(answerInfo){
			try{
				if(answerInfo.isContinue != 'continue'){
					//선택체크 이벤트 제거 //#20221028 #보기본문클릭
					$('div.numbering, div.listNumText').off('click');
					
					//정답 여부확인해서 마킹 이미지 처리
					var answerCorrect = stringUtils.nvl(answerInfo.correctAnswer,'0').split(',');
					
					//해당 문제의 정/오답 채첨 UI 이미지 경로
					var questionCheck = xipConstans.IMG_SRC.question.wrong;
					
					answerCorrect.forEach(function(n){
						var no = Number(stringUtils.nvl(n,'0'));
						
						if(answerInfo.isCorrect === 'Y'){
							$('div#numbering_'+no+' img.mychecking').attr('src',defaults.resourcesRoot+xipConstans.IMG_SRC.answerCheck.correct);
							questionCheck = xipConstans.IMG_SRC.question.correct;
						}else{
							var wrongCheckImg = $('<img />',{
								'class' : 'mychecking'
								, 'src' : defaults.resourcesRoot+xipConstans.IMG_SRC.answerCheck.wrong
								, 'style' : 'position:absolute; z-index: 99;'
							});
							$('div#numbering_'+no).prepend(wrongCheckImg)
						}
					});
					
					//문제에 정/오답 채첨 UI 이미지 객체 생성
					var questionChkImg = $('<img />',{
						'class' : 'qchecking'
						, 'src' : defaults.resourcesRoot+questionCheck
						, 'style' : 'position:absolute;opacity:0.7;'
						, 'onclick' : 'javascript:$(this).hide();'
					});				
					
					//해당 문제에 정/오답 채점 UI 객체 출력
					$('#prbm'+answerInfo.itemId).prepend(questionChkImg);
					
					$('button#btnSkipPrbm').hide();
				}
				this.Init()
				.then(function(){
					$.xipUI().UI.result.single(answerInfo)
					.then(function(){
						if(typeof sendItemSolveData === 'function'){
							try{
								var isCorrect	= answerInfo.isCorrect;
								var itemGrade	= answerInfo.itemGrade
								var userId 		= answerInfo.userId;
								var userIp 		= answerInfo.userIp;
								var dateTime	= moment().format('YYYY-MM-DD HH:mm:ss')
								var solveTime	= answerInfo.solveTime;
								var itemNo		= answerInfo.itemId;
								var cateCd1		= answerInfo.cateCd1;
								var cateCd2		= answerInfo.cateCd2;
								var cateCd3		= answerInfo.cateCd3;
								var cateCd4		= answerInfo.cateCd4;
								var cateCd5		= answerInfo.cateCd5;
								var cateNm1		= answerInfo.cateNm1;
								var cateNm2		= answerInfo.cateNm2;
								var cateNm3		= answerInfo.cateNm3;
								var cateNm4		= answerInfo.cateNm4;
								var cateNm5		= answerInfo.cateNm5;
								
								var targetCd		= answerInfo.targetCd; //#20220401 #아이브릭스 요청 (초중 학년+학기 정보)
								sendItemSolveData(userId,userIp,dateTime,solveTime,isCorrect,itemNo,itemGrade,cateCd1,cateCd2,cateCd3,cateCd4,cateCd5, cateNm1, cateNm2, cateNm3, cateNm4, cateNm5, targetCd);								
							}catch(ie){
								console.debug(ie);
							}
						}
					})
				});
								
			}catch(e){
				console.error(e);
			}
		},
		SolvePaperResult : function(request){
			var _this = this;
			return new Promise(function(resolve, reject){
				var requiredKeys = ['duration'];
				var domParser = new DOMParser();
				try{
					
					if(xipCommonUtils.checkRequired.all(requiredKeys, request)){
						var answerResult = _this.SolvePaper.answerResult();
						var correctInfo = {
							score : 0
							,cnt : 0
						}
						
						var requestXML 		= domParser.parseFromString('<Answer></Answer>','text/xml');
						var xmlDom 			= requestXML.documentElement;
						var answerDetails 	= domParser.parseFromString('<AnswerDetails></AnswerDetails>','text/xml');
						var detailsDom 		= answerDetails.documentElement;
						var duration		= stringUtils.nvl(request.duration,'0')
						xmlDom.setAttribute("ID", stringUtils.nvl(answerResult.answerInfo.id,'0'));
						xmlDom.setAttribute("PaperID", answerResult.answerInfo.paperid);
						xmlDom.setAttribute("UserID", answerResult.answerInfo.userid);
						xmlDom.setAttribute("TestTime", duration);
						xmlDom.setAttribute("TestDate",moment().format('YYYY-MM-DD HH:mm:ss'));
						xmlDom.setAttribute("Score", correctInfo.score);
						xmlDom.setAttribute("IsTemp", "false");
						xmlDom.setAttribute("IsMoc", answerResult.answerInfo.ismoc);
						xmlDom.setAttribute("CorrerctCount", correctInfo.cnt);
						
						var avgSolveTime = 0; 
						try{
							if(Number(duration) > 0){
								var avgTime = Number(duration) / answerResult.items.length;
								if(avgTime > 0){
									avgSolveTime = Math.ceil(avgTime);
								}else{
									avgSolveTime = Math.round(avgTime);
								}
							}else{
								avgSolveTime = 1;
							}
						}catch(e4){
							console.debug(e4);
						}
						
						$.extend(request.opts,{avgItemSolveTime : avgSolveTime});						
						
						try{
							answerResult.items.forEach(function(v,i){
								var isCorrect = false;
								var currentScore = 0;
								var isChoice = true;
								
								var usrCorrect = stringUtils.nvl(answerResult.userAnswer[v.itemId]);//#20220512 #주관식답
								
								try{
									//var usrCorrect = stringUtils.nvl(answerResult.userAnswer[v.itemId]);//#20220512 #주관식답
									var answerInfo = $.answerCheck({itemId : v.itemId ,correct : usrCorrect});
									
									isCorrect = stringUtils.toLowerCase(answerInfo.isCorrect) == 'y';
									currentScore = v.score;
									isChoice = v.typeId == xipConstans.TypeId.type21.code
								
									//#20220228 score 필드 수정 : 시험지의 모든 문항 총점 > 맞은 문제 총점 (고교 기출 요청)
									//correctInfo.score += currentScore;
									if(isCorrect) correctInfo.score += currentScore;
									correctInfo.cnt += isCorrect ? 1 : 0;
									
								}catch(ee0){
									console.debug(ee0);
								}
								
								//#20220512 #주관식답 /*#20231117 #주관식추가(순서대로)*/
								if(v.typeId == xipConstans.TypeId.type31.code || v.typeId == xipConstans.TypeId.type32.code 
									|| v.typeId == xipConstans.TypeId.type35.code || v.typeId == xipConstans.TypeId.type36.code || v.typeId == xipConstans.TypeId.type37.code){
									usrCorrect = $.xipCommon.ReplaceAll(usrCorrect,xipConstans.delimiterText,',');
								}
								
								var answerDetail = domParser.parseFromString('<AnswerDetail></AnswerDetail>','text/xml');
								var detailDom = answerDetail.documentElement;
								
								detailDom.setAttribute("ID", 0);
								detailDom.setAttribute("PaperDetailID", v.paperDetail);
								detailDom.setAttribute("ItemID", v.itemId);
								detailDom.setAttribute("IsCorrect", stringUtils.nvl(String(isCorrect),'false'));
								detailDom.setAttribute("Score",stringUtils.nvl(String(currentScore),'0'));
								detailDom.setAttribute("IsChoice", stringUtils.nvl(String(isChoice),'false'));
								//detailDom.setAttribute("Answer", stringUtils.nvl(answerResult.userAnswer[v.itemId]));
								detailDom.setAttribute("Answer", usrCorrect);//#20220512 #주관식답
								detailDom.setAttribute("OddAnswer", "");
	
								detailsDom.appendChild(detailDom);
								v['checked'] = isCorrect
							});
							
							xmlDom.setAttribute("Score", correctInfo.score);
							xmlDom.setAttribute("CorrerctCount", correctInfo.cnt);						
							xmlDom.appendChild(detailsDom)
							var xmltoString =  (new XMLSerializer()).serializeToString(requestXML);
							
							$.xipIf.Solve.paper({
								requestXml : xmltoString
								,datas : request.datas
								,opts : request.opts
							})
							.then(function(data){
								
								//선택체크 이벤트 제거 #20221028 #보기본문클릭
								$('div.numbering, div.listNumText, span.omr_answer').off('click');
								//입력창 입력 비활성화
								$('input[type=text].answerObject').prop('readonly', true);
														
								return new Promise(function(resolve2){
									var params = {
										paperId : answerResult.answerInfo.paperid
									};
									$.xipIf.Solve.userAnswerTemp.delete(params)
									.then(resolve2)
									.catch(resolve2)
								});
							})
							.then(function(){
								return new Promise(function(resolve2){
									try{
										//기출시험지 채점일 경우 풀서비스 성적 반영 여부(고교만 해당)
										if(xipConstans.SiteType.HSC.code.equals($thisSite)){
											var paperDatas = $.getPaperDatas();
											var iRecord = stringUtils.nvl(paperDatas.iRecord);
											var iRecordYear = parseInt(stringUtils.rpad(paperDatas.iRecord,4,'0').substr(0,4));
											//#20220302 고교기출 저장 수정
											if(paperDatas.isMoc){
												$.xipIf.Prbm.retrieveAnswerMocPreparation({
													paperId 	: paperDatas.paperId
													,irecord 	: iRecord
													,subjectId 	: paperDatas.subjectID
												})
												.then(function(result){
													var res = result.data || {};													
									    			if ('success'.equals(res.result)){
														alert(xipConstans.MSG.successSaveScoreMessage);
														resolve2();
									    			}else if('not exists'.equals(res.result)){
														console.error('fullservice 시험지 정보가 존재하지 않음.');
														resolve2();
													}else {
														alert(stringUtils.nvl(res.result, xipConstans.AjaxState.FAIL.msg));
														resolve2();
									    			}
												})
												.catch(function(err2){
													console.error(err2);
													resolve2()
												})
											}else{
												throw '';
											}
										}else{
											throw '';
										}
									}catch(he){
										resolve2();
									}
								});								
							})
							.then(function(res){
								$.xipUI().UI.result.paper();
								$.initModuleActivity()
							})
							.then(resolve)	
							.catch(function(err00){
								console.error(err00);
								if(err00 != xipConstans.AjaxState.NOTLOGIN.code){
									alert(xipConstans.AjaxState.FAIL.msg)
								}
								reject();
							});
						}catch(e){
							console.error(e);
							reject()
						}
					}else{
						throw '요청 필수항목 누락 : [' + JSON.stringify(request) + ']';
					}
				}catch(e){
					console.error(e);
					reject();
				}				
			});
		},
		SolveLitPaperResult : function(request){
			var _this = this;
			return new Promise(function(resolve, reject){
				var requiredKeys = ['duration'];
				var domParser = new DOMParser();
				var litAsmtResultNo = '';
				try{
					
					if(xipCommonUtils.checkRequired.all(requiredKeys, request)){
						var answerResult = _this.SolvePaper.answerResult();
						var correctInfo = {
							score : 0
							,cnt : 0
						}
						
						var requestXML 		= domParser.parseFromString('<Answer></Answer>','text/xml');
						var xmlDom 			= requestXML.documentElement;
						var answerDetails 	= domParser.parseFromString('<AnswerDetails></AnswerDetails>','text/xml');
						var detailsDom 		= answerDetails.documentElement;
						var duration		= stringUtils.nvl(request.duration,'0')
						xmlDom.setAttribute("ID", stringUtils.nvl(answerResult.answerInfo.id,'0'));
						xmlDom.setAttribute("PaperID", answerResult.answerInfo.paperid);
						xmlDom.setAttribute("UserID", answerResult.answerInfo.userid);
						xmlDom.setAttribute("TestTime", duration);
						xmlDom.setAttribute("TestDate",moment().format('YYYY-MM-DD HH:mm:ss'));
						xmlDom.setAttribute("Score", correctInfo.score);
						xmlDom.setAttribute("IsTemp", "false");
						xmlDom.setAttribute("IsMoc", answerResult.answerInfo.ismoc);
						xmlDom.setAttribute("CorrerctCount", correctInfo.cnt);
						
						var avgSolveTime = 0; 
						try{
							if(Number(duration) > 0){
								var avgTime = Number(duration) / answerResult.items.length;
								if(avgTime > 0){
									avgSolveTime = Math.ceil(avgTime);
								}else{
									avgSolveTime = Math.round(avgTime);
								}
							}else{
								avgSolveTime = 1;
							}
						}catch(e4){
							console.debug(e4);
						}
						
						$.extend(request.opts,{avgItemSolveTime : avgSolveTime});						
						
						try{
							answerResult.items.forEach(function(v,i){
								var isCorrect = false;
								var currentScore = 0;
								var isChoice = true;
								
								var usrCorrect = stringUtils.nvl(answerResult.userAnswer[v.itemId]);//#20220512 #주관식답
								
								try{
									//var usrCorrect = stringUtils.nvl(answerResult.userAnswer[v.itemId]);//#20220512 #주관식답
									var answerInfo = $.answerCheck({itemId : v.itemId ,correct : usrCorrect});
									
									isCorrect = stringUtils.toLowerCase(answerInfo.isCorrect) == 'y';
									currentScore = v.score;
									isChoice = v.typeId == xipConstans.TypeId.type21.code
								
									//#20220228 score 필드 수정 : 시험지의 모든 문항 총점 > 맞은 문제 총점 (고교 기출 요청)
									//correctInfo.score += currentScore;
									if(isCorrect) correctInfo.score += currentScore;
									correctInfo.cnt += isCorrect ? 1 : 0;
									
								}catch(ee0){
									console.debug(ee0);
								}
								
								//#20220512 #주관식답 /*#20231117 #주관식추가(순서대로)*/
								if(v.typeId == xipConstans.TypeId.type31.code || v.typeId == xipConstans.TypeId.type32.code 
									|| v.typeId == xipConstans.TypeId.type35.code || v.typeId == xipConstans.TypeId.type36.code || v.typeId == xipConstans.TypeId.type37.code){
									usrCorrect = $.xipCommon.ReplaceAll(usrCorrect,xipConstans.delimiterText,',');
								}
								
								var answerDetail = domParser.parseFromString('<AnswerDetail></AnswerDetail>','text/xml');
								var detailDom = answerDetail.documentElement;
								
								detailDom.setAttribute("ID", 0);
								detailDom.setAttribute("PaperDetailID", v.paperDetail);
								detailDom.setAttribute("ItemID", v.itemId);
								detailDom.setAttribute("IsCorrect", stringUtils.nvl(String(isCorrect),'false'));
								detailDom.setAttribute("Score",stringUtils.nvl(String(currentScore),'0'));
								detailDom.setAttribute("IsChoice", stringUtils.nvl(String(isChoice),'false'));
								//detailDom.setAttribute("Answer", stringUtils.nvl(answerResult.userAnswer[v.itemId]));
								detailDom.setAttribute("Answer", usrCorrect);//#20220512 #주관식답
								detailDom.setAttribute("OddAnswer", "");
	
								detailsDom.appendChild(detailDom);
								v['checked'] = isCorrect
							});
							
							xmlDom.setAttribute("Score", correctInfo.score);
							xmlDom.setAttribute("CorrerctCount", correctInfo.cnt);						
							xmlDom.appendChild(detailsDom)
							var xmltoString =  (new XMLSerializer()).serializeToString(requestXML);
							
							$.xipIf.Solve.paper({
								requestXml : xmltoString
								,datas : request.datas
								,opts : request.opts
							})
							.then(function(data){
								//#문해력테스트 #LIT #220711
								//선택체크 이벤트 제거
								
								litAsmtResultNo = data;
								$('div.numbering, span.omr_answer').off('click');
								//입력창 입력 비활성화
								$('input[type=text].answerObject').prop('readonly', true);
														
								return new Promise(function(resolve2){
									var params = {
										paperId : answerResult.answerInfo.paperid
									};
									$.xipIf.Solve.userAnswerTemp.delete(params)
									.then(resolve2)
									.catch(resolve2)
								});
							})
							.then(function(res){
								$.xipUI().UI.result.paper();
								$.initModuleActivity()
								resolve(litAsmtResultNo);
							})
							.catch(function(err00){
								console.error(err00);
								if(err00 != xipConstans.AjaxState.NOTLOGIN.code){
									alert(xipConstans.AjaxState.FAIL.msg)
								}
								reject();
							});
						}catch(e){
							console.error(e);
							reject()
						}
					}else{
						throw '요청 필수항목 누락 : [' + JSON.stringify(request) + ']';
					}
				}catch(e){
					console.error(e);
					reject();
				}				
			});
		},
		SolveNumPaperResult : function(request){	//#20230718 #수해력
			var _this = this;
			return new Promise(function(resolve, reject){
				var requiredKeys = ['duration'];
				var domParser = new DOMParser();
				var numAsmtResultNo = '';
				try{
					
					if(xipCommonUtils.checkRequired.all(requiredKeys, request)){
						var answerResult = _this.SolvePaper.answerResult();
						var correctInfo = {
							score : 0
							,cnt : 0
						}
						
						var requestXML 		= domParser.parseFromString('<Answer></Answer>','text/xml');
						var xmlDom 			= requestXML.documentElement;
						var answerDetails 	= domParser.parseFromString('<AnswerDetails></AnswerDetails>','text/xml');
						var detailsDom 		= answerDetails.documentElement;
						var duration		= stringUtils.nvl(request.duration,'0')
						xmlDom.setAttribute("ID", stringUtils.nvl(answerResult.answerInfo.id,'0'));
						xmlDom.setAttribute("PaperID", answerResult.answerInfo.paperid);
						xmlDom.setAttribute("UserID", answerResult.answerInfo.userid);
						xmlDom.setAttribute("TestTime", duration);
						xmlDom.setAttribute("TestDate",moment().format('YYYY-MM-DD HH:mm:ss'));
						xmlDom.setAttribute("Score", correctInfo.score);
						xmlDom.setAttribute("IsTemp", "false");
						xmlDom.setAttribute("IsMoc", answerResult.answerInfo.ismoc);
						xmlDom.setAttribute("CorrerctCount", correctInfo.cnt);
						
						var avgSolveTime = 0; 
						try{
							if(Number(duration) > 0){
								var avgTime = Number(duration) / answerResult.items.length;
								if(avgTime > 0){
									avgSolveTime = Math.ceil(avgTime);
								}else{
									avgSolveTime = Math.round(avgTime);
								}
							}else{
								avgSolveTime = 1;
							}
						}catch(e4){
							console.debug(e4);
						}
						
						$.extend(request.opts,{avgItemSolveTime : avgSolveTime});						
						
						try{
							answerResult.items.forEach(function(v,i){
								var isCorrect = false;
								var currentScore = 0;
								var isChoice = true;
								
								var usrCorrect = stringUtils.nvl(answerResult.userAnswer[v.itemId]);//#20220512 #주관식답
								
								try{
									//var usrCorrect = stringUtils.nvl(answerResult.userAnswer[v.itemId]);//#20220512 #주관식답
									var answerInfo = $.answerCheck({itemId : v.itemId ,correct : usrCorrect});
									
									isCorrect = stringUtils.toLowerCase(answerInfo.isCorrect) == 'y';
									currentScore = v.score;
									isChoice = v.typeId == xipConstans.TypeId.type21.code
								
									//#20220228 score 필드 수정 : 시험지의 모든 문항 총점 > 맞은 문제 총점 (고교 기출 요청)
									//correctInfo.score += currentScore;
									if(isCorrect) correctInfo.score += currentScore;
									correctInfo.cnt += isCorrect ? 1 : 0;
									
								}catch(ee0){
									console.debug(ee0);
								}
								
								//#20220512 #주관식답 /*#20231117 #주관식추가(순서대로)*/
								if(v.typeId == xipConstans.TypeId.type31.code || v.typeId == xipConstans.TypeId.type32.code 
									|| 	v.typeId == xipConstans.TypeId.type35.code || v.typeId == xipConstans.TypeId.type36.code || v.typeId == xipConstans.TypeId.type37.code){
									usrCorrect = $.xipCommon.ReplaceAll(usrCorrect,xipConstans.delimiterText,',');
								}
								
								var answerDetail = domParser.parseFromString('<AnswerDetail></AnswerDetail>','text/xml');
								var detailDom = answerDetail.documentElement;
								
								detailDom.setAttribute("ID", 0);
								detailDom.setAttribute("PaperDetailID", v.paperDetail);
								detailDom.setAttribute("ItemID", v.itemId);
								detailDom.setAttribute("IsCorrect", stringUtils.nvl(String(isCorrect),'false'));
								detailDom.setAttribute("Score",stringUtils.nvl(String(currentScore),'0'));
								detailDom.setAttribute("IsChoice", stringUtils.nvl(String(isChoice),'false'));
								//detailDom.setAttribute("Answer", stringUtils.nvl(answerResult.userAnswer[v.itemId]));
								detailDom.setAttribute("Answer", usrCorrect);//#20220512 #주관식답
								detailDom.setAttribute("OddAnswer", "");
	
								detailsDom.appendChild(detailDom);
								v['checked'] = isCorrect
							});
							
							xmlDom.setAttribute("Score", correctInfo.score);
							xmlDom.setAttribute("CorrerctCount", correctInfo.cnt);						
							xmlDom.appendChild(detailsDom)
							var xmltoString =  (new XMLSerializer()).serializeToString(requestXML);
							
							$.xipIf.Solve.paper({
								requestXml : xmltoString
								,datas : request.datas
								,opts : request.opts
							})
							.then(function(data){
								//#문해력테스트 #LIT #220711
								//선택체크 이벤트 제거
								
								numAsmtResultNo = data;
								//litAsmtResultNo = data;
								$('div.numbering, span.omr_answer').off('click');
								//입력창 입력 비활성화
								$('input[type=text].answerObject').prop('readonly', true);
														
								return new Promise(function(resolve2){
									var params = {
										paperId : answerResult.answerInfo.paperid
									};
									$.xipIf.Solve.userAnswerTemp.delete(params)
									.then(resolve2)
									.catch(resolve2)
								});
							})
							.then(function(res){
								$.xipUI().UI.result.paper();
								$.initModuleActivity()
								resolve(numAsmtResultNo);
							})
							.catch(function(err00){
								console.error(err00);
								if(err00 != xipConstans.AjaxState.NOTLOGIN.code){
									alert(xipConstans.AjaxState.FAIL.msg)
								}
								reject();
							});
						}catch(e){
							console.error(e);
							reject()
						}
					}else{
						throw '요청 필수항목 누락 : [' + JSON.stringify(request) + ']';
					}
				}catch(e){
					console.error(e);
					reject();
				}				
			});
		},
		SolvePaperResultCheckOnly : function(request){
			var _this = this;
			return new Promise(function(resolve, reject){
				var requiredKeys = ['duration'];
				var domParser = new DOMParser();
				try{
					
					if(xipCommonUtils.checkRequired.all(requiredKeys, request)){
						var answerResult = _this.SolvePaper.answerResult();
						var correctInfo = {
							score : 0
							,cnt : 0
						}
						
						var requestXML 		= domParser.parseFromString('<Answer></Answer>','text/xml');
						var xmlDom 			= requestXML.documentElement;
						var answerDetails 	= domParser.parseFromString('<AnswerDetails></AnswerDetails>','text/xml');
						var detailsDom 		= answerDetails.documentElement;
						var duration		= stringUtils.nvl(request.duration,'0')
						xmlDom.setAttribute("ID", stringUtils.nvl(answerResult.answerInfo.id,'0'));
						xmlDom.setAttribute("PaperID", answerResult.answerInfo.paperid);
						xmlDom.setAttribute("UserID", answerResult.answerInfo.userid);
						xmlDom.setAttribute("TestTime", duration);
						xmlDom.setAttribute("TestDate",moment().format('YYYY-MM-DD HH:mm:ss'));
						xmlDom.setAttribute("Score", correctInfo.score);
						xmlDom.setAttribute("IsTemp", "false");
						xmlDom.setAttribute("IsMoc", answerResult.answerInfo.ismoc);
						xmlDom.setAttribute("CorrerctCount", correctInfo.cnt);
						
						var avgSolveTime = 0; 
						try{
							if(Number(duration) > 0){
								var avgTime = Number(duration) / answerResult.items.length;
								if(avgTime > 0){
									avgSolveTime = Math.ceil(avgTime);
								}else{
									avgSolveTime = Math.round(avgTime);
								}
							}else{
								avgSolveTime = 1;
							}
						}catch(e4){
							console.debug(e4);
						}
						
						$.extend(request.opts,{avgItemSolveTime : avgSolveTime});						
						
						try{
							answerResult.items.forEach(function(v,i){
								var isCorrect = false;
								var currentScore = 0;
								var isChoice = true;
								
								var usrCorrect = stringUtils.nvl(answerResult.userAnswer[v.itemId]);//#20220512 #주관식답
								
								try{
									//var usrCorrect = stringUtils.nvl(answerResult.userAnswer[v.itemId]);//#20220512 #주관식답
									var answerInfo = $.answerCheck({itemId : v.itemId ,correct : usrCorrect});
									
									isCorrect = stringUtils.toLowerCase(answerInfo.isCorrect) == 'y';
									currentScore = v.score;
									isChoice = v.typeId == xipConstans.TypeId.type21.code
								
									//#20220228 score 필드 수정 : 시험지의 모든 문항 총점 > 맞은 문제 총점 (고교 기출 요청)
									//correctInfo.score += currentScore;
									if(isCorrect) correctInfo.score += currentScore;
									correctInfo.cnt += isCorrect ? 1 : 0;
									
								}catch(ee0){
									console.debug(ee0);
								}
								
								//#20220512 #주관식답 /*#20231117 #주관식추가(순서대로)*/
								if(v.typeId == xipConstans.TypeId.type31.code || v.typeId == xipConstans.TypeId.type32.code 
									|| v.typeId == xipConstans.TypeId.type35.code || v.typeId == xipConstans.TypeId.type36.code || v.typeId == xipConstans.TypeId.type37.code){
									usrCorrect = $.xipCommon.ReplaceAll(usrCorrect,xipConstans.delimiterText,',');
								}
								
								var answerDetail = domParser.parseFromString('<AnswerDetail></AnswerDetail>','text/xml');
								var detailDom = answerDetail.documentElement;
								
								detailDom.setAttribute("ID", 0);
								detailDom.setAttribute("PaperDetailID", v.paperDetail);
								detailDom.setAttribute("ItemID", v.itemId);
								detailDom.setAttribute("IsCorrect", stringUtils.nvl(String(isCorrect),'false'));
								detailDom.setAttribute("Score",stringUtils.nvl(String(currentScore),'0'));
								detailDom.setAttribute("IsChoice", stringUtils.nvl(String(isChoice),'false'));
								//detailDom.setAttribute("Answer", stringUtils.nvl(answerResult.userAnswer[v.itemId]));
								detailDom.setAttribute("Answer", usrCorrect);//#20220512 #주관식답
								detailDom.setAttribute("OddAnswer", "");
	
								detailsDom.appendChild(detailDom);
								v['checked'] = isCorrect
							});
							
							xmlDom.setAttribute("Score", correctInfo.score);
							xmlDom.setAttribute("CorrerctCount", correctInfo.cnt);						
							xmlDom.appendChild(detailsDom)
							var xmltoString =  (new XMLSerializer()).serializeToString(requestXML);
							
							return new Promise(function(resolve2){
								try{
									throw '';
								}catch(he){
									resolve2();
								}
							})
							.then(function(res){
								
								//선택체크 이벤트 제거 #20221028 #보기본문클릭
								$('div.numbering, div.listNumText, span.omr_answer').off('click');
								//입력창 입력 비활성화
								$('input[type=text].answerObject').prop('readonly', true);
								
								$.xipUI().UI.result.paper();
								$.initModuleActivity()
							})
							.then(resolve)	
							.catch(function(err00){
								console.error(err00);
								if(err00 != xipConstans.AjaxState.NOTLOGIN.code){
									alert(xipConstans.AjaxState.FAIL.msg)
								}
								reject();
							});
						}catch(e){
							console.error(e);
							reject()
						}
					}else{
						throw '요청 필수항목 누락 : [' + JSON.stringify(request) + ']';
					}
				}catch(e){
					console.error(e);
					reject();
				}				
			});
		},
		SolvePaperResultLayer : function(opts){//#20220816 #시험결과레이어
			var _this = this;
			this.Init()
			.then(function(){
				if(stringUtils.isNotEmpty(opts.type) && opts.type == 'dgnsPrv'){	
					$(defaults.root).xipUI().Paper.paperPrvResultView(opts);
				}else{
					$(defaults.root).xipUI().Paper.paperResultView(opts);
				}
			});
		},		
		Explanation : function(opts){
			this.Init()
			.then(function(){
				opts = $.extend(opts, {
					isShowCorrect	: true
				});
				$(defaults.root).xipUI().Paper.explanation(opts);
			});
		},
		ExplanationPaper : function(opts){//#20220816 #시험결과레이어
			this.Init()
			.then(function(){
				opts = $.extend(opts, {
					isShowCorrect	: true
				});
				$(defaults.root).xipUI().Paper.explanationPaper(opts);
			});
		},
		PopExplanation : function(opts){
			opts = $.extend({
				itemId : ''
				,isLanding : false
				,isShowCorrect	: true
				,isChatbotYn : '' //#20220523 #푸리봇해설보기
				,isLearned : false  //#20220517 
				,isPaper : false //#20220816 #시험결과레이어
				,isDefaultsRoot : defaults.root //#20220816 #시험결과레이어
				,isPopExplanInput : true //#20230105 #미리보기인풋
			},opts);
			
			var _this = this;
			_this.Init()
			.then(function(){
				var openProp = {
					id 			: xipConstans.POP.EXPLAIN.id,
					name 		: xipConstans.POP.EXPLAIN.name,
					addClass 	: 'flexcont', 
					title 		: '해설보기'
				};
				
				if(opts.isLanding){
					openProp['closeTrigerEvt'] = function(){
						var appType = $.trim(stringUtils.nvl($('input[name=xipSolveAppType]').val()));
						if(['ebsiApp','ebsiNewApp'].includes(appType)){
							window.location.href = "cnebsiapp://?type=webview_close";
						}else{
							self.close();
						}
					}
				}
				
				//#20220517 
				if(opts.isLearned){
					openProp['closeTrigerEvt'] = function(){
						$('#'+openProp.id).remove();
					}
				}
				
				var dim = xipCommonUI.modal.open(openProp);
				
				//컨텐츠 랩핑영역
				var contentsWrapper = dim.find('div.layer_content')
				var printWrapper	= $('<div />',{'class' : 'solve_explain'});
				var solCont			= $('<div />',{'class' : 'sol_cont'});					
				
				printWrapper
				.append(solCont)

				contentsWrapper.prepend(printWrapper)
				
				//#20220523 #푸리봇해설보기
				if(opts.isChatbotYn == 'Y'){
					dim.find('.layer_tit').hide();
					dim.find('.btnCloseExec').hide();
					dim.find('.layer_content').addClass('chatbot_opt').css({'height':'100%'});
					$('body').css({'background':'#f0f0dd'});
				}
				
				$(defaults.root).append(dim);
				if(opts.isPaper){//#20220816 #시험결과레이어
					$(solCont).xipUI().Paper.explanationPaper(opts);
				}else{
					$(solCont).xipUI().Paper.explanation(opts);
				}				
			});			
		},		
		LearnedPop : function(opts){
			this.Init()
			.then(function(){
				$(defaults.root).xipUI().UI.learned(opts);
			});
		},
		ErrorReport : function(opts){
			this.Init()
			.then(function(){
				$.xipReport(opts)
			});
		},
		VOD : function(opts){
			this.Init()
			.then(function(){
				if(stringUtils.isEmpty(opts.url)){
					alert(xipConstans.MSG.notFoundPlayInfo);
				}else{
					$.xipUI().UI.module.vod.pop(opts);
				}
			});			
		}
	}

	$.fn.Print = function(opts){
		defaults.print = $(this);
		return XIP.Print;			
	}

	$.fn.EbsXip = function(opts){
		defaults.root = $(this);	
		if(!xipObj){
			if(stringUtils.isNotEmpty(opts)){
				$.extend(defaults, opts);
			}
			xipObj = XIP		
		}
		
		$(this).css({
			'user-select': 'none'
		});
		
		window.oncontextmenu = function(){return false;};
		$(document).keyup(function(e){if(e.keyCode == 123) return false;});
		return xipObj;
	};	
	$.EbsXip = function(opts){
		return $('body').EbsXip(opts);
	};
	
	$.EbsXipInit = function(){
		return new Promise(function(resolve){
			defaults.root = $('<temp />');
			XIP.Init()
			.then(function(){
				resolve()
			})
			.catch(function(initE){
				console.error(initE);
			});
		});
	};	
})(jQuery);