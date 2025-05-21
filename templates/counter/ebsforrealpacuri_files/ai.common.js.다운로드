
/* ai.common.js start */
$(document).ready(function(){
    uiBasic.init();
    uiDetectOS.init(); // Divice, Browser Check

    tempPublish.init(); // 임시 스크립트 (퍼블에서만 확인할 경우 여기서 실행)
});

/*///////////////////////////////////////////////////////////////*/
/* *** Common ************************************************** */
/*///////////////////////////////////////////////////////////////*/

var uiBasic = {
    init: function(){
        // console.log("uiBasic init");

        this.scrSet = this.screenSet();

        /* common */
        uiInput.init();
        uiTextarea.init();
        uiSelect.init();
        uiDoughnut.init();
        uiScroll.init();
        uiLayer.init();
        uiTooltip.init();
        uiHeader.init();
        uiEtc.init(); // keypad, tabResize

        /* page content */
        $(".container.main").length && uiConMain.init();
        // $(".ai_con_recom").length && uiConRecom.init();
        uiContent.init();
        num_toggle.init();//2023-11-15 수정
        omrbox_toggle.init();//2023-11-15 수정
        foot_toggle.init();//2023-11-15 수정
        correctSwitch.init();//2023-11-15 수정
    },
    screenSet: function(){
        var screenW = screen.width,
            screenH = screen.height,
            windowW = $(window).width(),
            windowH = $(window).height();

        $(window).resize(function(){
            screenW = screen.width,
            screenH = screen.height,
            windowW = $(window).width(),
            windowH = $(window).height();
        });

        return [screenW, screenH, windowW, windowH];
    },
}

var uiInput = {
    init: function(){
        $(".input_wrap").length && this.set();
        $(".input_check.lock").length && checkLock();
        $(".input_date").length && this.datepicker();

        function checkLock(){
            $(".input_check.lock").each(function(){
                $(this).find("input").click(function(){
                    $(this).prop("checked",true);
                });
            });
        }
    },
    set: function(){
        $(".input_wrap").each(function(){
            if($(this).find("input").val()){
                $(this).addClass("on");
            }else{
                $(this).removeClass("on");
            }

            if($(this).find(".placeholder").length > 0){
                $(this).addClass("type_pl");
            }

            if($(this).hasClass("type_file") == false){
                $(this).find(".placeholder").click(function(){
                    $(this).parents(".input_wrap").addClass("on");
                    $(this).parents(".input_wrap").find("input").focus();

                    uiSelect.close();
                    uiTooltip.close();
                });

                $(this).find("input").on("focus", function(){
                    $(this).parents(".input_wrap").addClass("on");

                    uiSelect.close();
                    uiTooltip.close();
                });

                $(this).find("input").on("blur", function(){
                    if($(this).val()){
                        $(this).parents(".input_wrap").addClass("on");
                    }else{
                        $(this).parents(".input_wrap").removeClass("on");
                    }
                });
            }else{
                var fileChangeFn = function(e){
                    var _this = $(e.target);
                    var fileName = $(_this).val();
                    try{
                        fileName = fileName.replace(/\\/g,'/');
                        fileName = fileName.split('/').reverse()[0];
                    }catch(e){console.error(e);}

                    if(fileName){
                        $(_this).parents(".input_wrap").find(".file_name").text(fileName);
                        $(_this).parents(".input_wrap").addClass("on");
                    }else{
                        $(_this).parents(".input_wrap").removeClass("on");
                    }
                }

                $(this).find("input[type='file']").off('change',fileChangeFn);
                $(this).find("input[type='file']").on('change',fileChangeFn);

                $(this).find(".file_del").off('click');
                $(this).find(".file_del").click(function(ec){
                    //이 함수는 개발소스에는 objectUtils로 구현되어있음, 퍼블 화면 동작을 위해 넣어둠
                    // var cfn = function(ele, evt){
                    //     try{
                    //         var newElement = $('<input />');
                    //         var attributes = Array.from($(ele)[0].attributes);

                    //         Object.keys(attributes).forEach((v,i)=>{
                    //             newElement.attr(attributes[v].name,attributes[v].value)
                    //         });

                    //         if(evt && evt.name){
                    //             newElement.on(evt.name, evt.evtFn);
                    //         }
                    //         return newElement;
                    //     }catch(ee){
                    //         console.log(ee);
                    //         return ele.clone();
                    //     }
                    // }
                    // var copyElementFn = typeof objectUtils === 'object' ? objectUtils.copyElement : cfn;

                    ec.preventDefault();
                    ec.stopPropagation();
                    var fileWrapRoot = $(this).parents(".input_wrap");
                    var fileElement = $(fileWrapRoot).find("input[type='file']");
                    var newFileElement = copyElementFn(fileElement, {name : 'change', evtFn : fileChangeFn});

                    $(fileWrapRoot).find(".file_name").empty();
                    $(fileWrapRoot).removeClass("on");
                    $(fileElement).after(newFileElement);
                    $(fileElement).remove();
                });
            }
        });
    },
    datepicker: function(){
        var dateOptions = {
		    dateFormat: 'yy-mm-dd',
		    // showOn: 'button',
		    // buttonImage: '../images/ai/ico',
		    // buttonImageOnly: true,
		    buttonText: '날짜 선택',
		    nextText: '다음 달',
		    prevText: '이전 달',
		    showMonthAfterYear: true,
		    dayNamesMin: ['일', '월', '화', '수', '목', '금', '토'],
		    monthNames: ['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월']
		};

        $( ".datepicker").each(function(){
            $(this).datepicker(dateOptions);
        });

        $(".ui-datepicker-trigger").click(function(){
            uiSelect.close();
            uiTooltip.close();
        });
    }
}

var uiTextarea = {
    init: function(){
        $(".textarea_wrap").length && this.set();
    },
    set: function(){
        $(".textarea_wrap").each(function(){
            if($(this).find("textarea").val()){
                $(this).addClass("on");
            }else{
                $(this).removeClass("on");
            }
        });

        $(".textarea_wrap .placeholder").click(function(){
            $(this).parents(".textarea_wrap").addClass("on");
            $(this).parents(".textarea_wrap").find("textarea").focus();
        });

        $(".textarea_wrap textarea").on("focus", function(){
            $(this).parents(".textarea_wrap").addClass("on");
        });

        $(".textarea_wrap textarea").on("blur", function(){
            if($(this).val()){
                $(this).parents(".textarea_wrap").addClass("on");
            }else{
                $(this).parents(".textarea_wrap").removeClass("on");
            }
        });
    },
}

var uiSelect = {
    init: function(){
        $("[class^='select_']").length && this.set();
    },
    set: function(){
        $("[class^='select_']").each(function(){
            if($(this).data("type") != "button" && $(this).data("type") != "dropdown"){
                var thisText = $(this).find(".sel_opt.on").text(),
                    thisIndex = $(this).find(".sel_opt.on").parent("li").index();

                if(thisText){
                    $(this).find(".sel_val").find("span").text(thisText);
                    $(this).find("select").find("option").eq(thisIndex).attr("selected","selected");
                }

                if($(this).data("type") == "expand"){
                    $(this).addClass("type_expand");
                }
            }
        });

        this.selOpen();
        this.selChange();
        this.close();
    },
    selOpen: function(){
        $("[class^='select_'] .sel_val").off("click");
        $("[class^='select_'] .sel_val").on("click",function(e){

            if($(this).parents("[class^='select_']").data("type") != "button" && $(this).parents("[class^='select_']").hasClass("lock") == false){
                var selSizeW = $(this).outerWidth(),
                    selSizeH = $(this).outerHeight(),
                    downSizeW = $(this).next(".sel_down").outerWidth();

                $("[class^='select_']").not($(this).parent()).removeClass("on");
                $(this).parents("[class^='select_']").toggleClass("on");

                if($(this).parents("[class^='select_']").hasClass("type_expand")){
                    if($(this).parents(".type_expand").hasClass("on")){
                        $(this).parents(".type_expand").css({
                            "width": selSizeW + "px",
                            "padding-top": selSizeH + "px"
                        });

                        $(this).parents(".expand_inner").css({
                            "width": downSizeW + "px",
                        });
                    }else{
                        $(this).parents(".type_expand").removeAttr("style");
                        $(this).removeAttr("style");

                        $(this).parents(".expand_inner").removeAttr("style");
                    }
                }
            }

            uiTooltip.close();
            uiHeader.lnb.close();

            e.preventDefault();
            e.stopPropagation();
        });

        $("[class^='select_'] select").on("click",function(){
            $(this).parents("[class^='select_']").toggleClass("on");
        });
    },
    selChange: function(){
        $("[class^='select_'] .sel_opt").on("click",function(){
            $(this).parents("[class^='select_']").removeClass("on");

            if($(this).parents("[class^='select_']").data("type") == "expand"){
                $(this).parents(".type_expand").removeAttr("style");
                $(this).parents(".type_expand").find(".sel_val").removeAttr("style");
                $(this).parents(".type_expand").find(".expand_inner").removeAttr("style");
            }else if($(this).parents("[class^='select_']").data("type") != "button" && $(this).parents("[class^='select_']").data("type") != "dropdown"){
                var thisText = $(this).text(),
                thisIndex = $(this).parents("li").index();

                $(this).parents(".sel_down").find(".sel_opt").removeClass("on");
                $(this).addClass("on");

                var value = $(this).data("value");
                if(value){
                    $(this).parents("[class^='select_']").find("select").val(value).trigger("change");
                }

                $(this).parents("[class^='select_']").find(".sel_val").find("span").text(thisText);
                $(this).parents("[class^='select_']").find("select").find("option").eq(thisIndex).prop("selected","selected");
            }
        });
    },
    close: function(){
        $("[class^='select_']").removeClass("on");

        $(document).click(function(e){
            if(!$("[class^='select_']").has(e.target).length){
                $("[class^='select_']").removeClass("on");
            }
        });

        $(window).on("scroll resize",function(){
            $("[class^='select_']").each(function(){
                if($(this).data("type") != "dropdown"){
                    $("[class^='select_']").removeClass("on");
                }
            });
        });
    }
}

var uiDoughnut = {
    init: function(){
        $(".doughtnut").length && this.setAni();
    },
    set: function(){
        $(".doughtnut").each(function(){
            var thisFull = $(this).data("full"),
                thisValue = $(this).data("value"),
                thisDeg = (thisValue / thisFull) * 360;

                // console.log(Number.isInteger(thisDeg));
                // console.log(thisFull);

            $(this).find(".bar").css({
                "transform": "rotate(" + thisDeg + "deg)"
            });
            $(this).find(".data").text(thisValue);

            if(thisDeg > 180){
                $(this).find(".circle_cap").addClass("over_half");
            }
        });
    },
    setAni: function(){
        var timer = 0, speed = 1;
        $(".doughtnut").each(function(){
            var thisFull = $(this).data("full"),
                thisValue = $(this).data("value"),
                thisDeg = (thisValue / thisFull) * 360;

            var $this = $(this);

            $({animatedValue:0}).delay(timer*1000).animate({animatedValue:thisDeg},{
                duration: speed*1000,
                step: function(){
                    $this.find(".bar").css({ "transform": "" });
                    $this.find(".circle_cap").removeClass("over_half");

                    $this.find(".bar").css({
                        "transform": "rotate(" + this.animatedValue + "deg)"
                    });

                    if(this.animatedValue > 180){
                        $this.find(".circle_cap").addClass("over_half");
                    }
                },
                complete: function() {
                    $this.find(".bar").css({
                        "transform": "rotate(" + this.animatedValue + "deg)"
                    });

                    if(this.animatedValue > 180){
                        $this.find(".circle_cap").addClass("over_half");
                    }
                }
            });
        });

        uiOdoCount.counting("data",timer,speed);
    }
}

var uiOdoCount = {
    // 숫자 카운팅 모션 'count_target' target에 이름 지정하여 사용
    counting: function(target, timer, speed){ // 카운팅 모션
        // var timer = 0, speed = 1;
        $('.count_'+target).each(function(){
            var $this = $(this),
                per = $this.data('per');
            $({animatedValue:0}).delay(timer*1000).animate({animatedValue:per},{
                duration: speed*1000,
                step: function(){
                    $this.text( String(Math.ceil(this.animatedValue)).replace(/\B(?=(\d{3})+(?!\d))/g, ",") );
                },
                complete: function() {
                    $this.text( String(Math.ceil(this.animatedValue)).replace(/\B(?=(\d{3})+(?!\d))/g, ",") );
                }
            });
        });
    },
}

var uiScroll = {
    init: function(){
        this.moveTop();
        this.posAdjust();
        // this.fadeAction();
        // this.mouseWheel();
    },
    moveTop : function(){
        $(document).off("click",".btn_top");
        $(document).on("click",".btn_top",function(){
            $("html,body").animate({scrollTop: 0}, 300);
            return false;
        });
    },
    posAdjust: function(){
        if(uiBasic.screenSet()[2] <= 1280){
            var adjValue = uiBasic.screenSet()[2] / 2 - 20;
            $(".fixed_area").css({
                "margin-right": (adjValue * -1) + "px"
            });
        }

        $(window).resize(function(){
            if(uiBasic.screenSet()[2] <= 1280){
                var adjValue = uiBasic.screenSet()[2] / 2 - 20;
                $(".fixed_area").css({
                    "margin-right": (adjValue * -1) + "px"
                });
            }else{
                $(".fixed_area").css({
                    "margin-right": ""
                });
            }
        });
    },
    // fadeAction: function(){
    //     $(window).scroll(function(){
    //         if ($(this).scrollTop() > 50) {
    //             $("body").addClass("scrollup");
    //             $(".fixed_area").fadeIn();
    //         } else {
    //             $("body").removeClass("scrollup");
    //             $(".fixed_area").fadeOut();
    //         }
    //     });
    // },
    // mouseWheel: function(){
    //     var wheelStat = null;

    //     $("html,body").on('mousewheel',function(e){
    //         var wheel = e.originalEvent.wheelDelta;

    //         // get scroll position
    //         if(wheel>0){
    //             // // when scroll up
    //             // console.log("up");
    //             wheelStat = false;
    //         } else {
    //             // // when scroll down
    //             // console.log("down");
    //             wheelStat = true;
    //         }
    //     });

    //     return wheelStat;
    // }
}

var uiLayerStatus = 0;
var uiLayerSet = {
    init: function(name, opt, opt2) {
        if(uiLayerStatus === 0){ // open
            uiLayerSet.scrollOff(opt2);
            $('#ly-'+name).addClass('open').attr({'tabindex':1,'aria-hidden':'false'}).focus();
            $('#content').attr({'aria-hidden':'true'});

            uiLayerStatus = 1;

            $('#ly-'+name).click(function(e){
                // Layer is not closed when click out of layer
                if(opt != 'fback'){
                    if(!$(this).has(e.target).length){
                        $('#ly-'+name).removeClass('open');
                        $('#ly-'+name).attr({'aria-hidden':'true'}).focus();
                        $('#ly-'+name).removeAttr('tabindex');
                        $('#content').attr({'aria-hidden':'false'});
                        uiLayerSet.scrollOn(opt2);
                        uiLayerStatus = 0;
                    }
                }
            });

        }else{ // close
            uiLayerSet.scrollOn(opt2);
            $('#ly-'+name).removeClass('open');
            $('#ly-'+name).attr({'aria-hidden':'true'}).focus();
            $('#ly-'+name).removeAttr('tabindex');
            $('#content').attr({'aria-hidden':'false'});
            uiLayerStatus = 0;
        }

        this.close();
    },
    scrollOff: function (opt2) {
        if(opt2 != 'fdim'){
            $('body').append('<div class="layer_dim"></div>');
        }

        $('body').css('overflow','hidden');
        var x=window.scrollX, y=window.scrollY;
        window.onscroll=function(){window.scrollTo(x, y)};
    },
    scrollOn: function (opt) {
        $('.layer_dim').remove();

        $('body').css('overflow','');
        window.onscroll=function(){};
    },
    close: function(){
        $(".layer_pop .btn_close").off("click");
        $(".layer_pop .btn_close").on("click",function(){
            var thisName = $(this).parents(".layer_pop").attr("id"),
                thisName = thisName.replace("ly-","");

            uiLayerSet.init(thisName);
        });
    }
}

var uiLayer = {
    init: function(){
        $(".layer_open").click(function(){
            var thisTarget = $(this).data("target");

            uiLayerSet.init(thisTarget);
        });
    }
}

var uiTooltip = {
    init: function(){
        if($(".tooltip").length > 0){
            this.tooltipSet();
            this.tooltipAct();
            this.close();
        }
    },
    tooltipSet: function(){
        var adjustL = null;

        if(uiBasic.screenSet()[2] <= 1023){
            $(".tooltip").each(function(index){
                var xPos = Math.floor($(this).offset().left);

                $(this).data("xpos",xPos);

                var xPosC =  $(this).find(".tooltip_con").offset().left,
                    thisW =  $(this).find(".tooltip_con").outerWidth(),
                    exOrdi = Math.floor(xPosC + thisW);

                if(xPosC > 0 && exOrdi > uiBasic.screenSet()[2]){
                    adjustL = (exOrdi - uiBasic.screenSet()[2] + 15) * -1;
                }else if(xPosC < 0){
                    adjustL = (xPosC - 15) * -1;
                }

                $(this).find(".tooltip_con").data("xposc",xPosC);
                $(this).find(".tooltip_con").data("width",thisW);
                $(this).find(".tooltip_con").data("adjust",adjustL);
            });
        }else{
            adjustL = 0;
        }
    },
    tooltipAct: function(){
        $(document).off("click",".tooltip_button");
        $(document).on("click",".tooltip_button",function(e){
            var thisAdjust = $(this).parent(".tooltip").find(".tooltip_con").data("adjust");

            $(".tooltip").not($(this).parent(".tooltip")).removeClass("on");
            $(this).parent(".tooltip").toggleClass("on").find(".tooltip_con").css({
                "margin-left": thisAdjust + "px"
            });

            uiSelect.close();
            uiHeader.lnb.close();
        });
    },
    close: function(){
        $(".tooltip").removeClass("on");

        $(document).click(function(e){
            if(!$(".tooltip_button").has(e.target).length){
                $(".tooltip").removeClass("on");
            }
        });

        $(window).on("scroll resize", function(){
            $(".tooltip").removeClass("on");
        });
    }
}

var uiHeader = {
    init: function(){
        $(".header").length && this.set();
    },
    set: function(){
        this.gnb.init();
        this.lnb.init();
        this.snb.init();
        this.theme();
    },
    gnb: {
        init: function(){
            if(uiBasic.screenSet()[2] > 1023){
                uiHeader.gnb.set();
            }else{
                uiHeader.gnb.set("mo");
            }

            $(window).resize(function(){
                if(uiBasic.screenSet()[2] > 1023){
                    uiHeader.gnb.set();
                }else{
                    uiHeader.gnb.set("mo");
                }
            });
        },
        set: function(mode){
            if(!mode || mode == "pc"){
                $(".gnb .depth1").mouseenter(function(){
                    $(this).parents(".gnb").addClass("on");

                    uiSelect.close();
                    uiTooltip.close();
                });
                $(".gnb .ai_inner").mouseleave(function(){
                    $(this).parents(".gnb").removeClass("on");
                });

                $(".gnb .depth1 > li").hover(function(){
                    $(this).addClass("on");
                }, function(){
                    $(this).removeClass("on");
                });
            }else{
                this.moSet();
            }
        },
        moSet: function(){
            $(".header .ham_button").click(function(){
                $(".mo_gnb .side_area").addClass("on");
                uiLayerSet.scrollOff("fdim");

                uiSelect.close();
                uiTooltip.close();
                uiHeader.lnb.close();

                var curPos = $(".mo_gnb .snb_depth1 li.on").index() * $(".mo_gnb .snb_depth1 li.on").outerHeight();
                $(".mo_gnb .snb_depth1").scrollTop(curPos);
            });

            $(".mo_gnb .side_area .side_close").click(function(){
                $(".mo_gnb .side_area").removeClass("on");
                uiLayerSet.scrollOn();
            });

            
            if($("body").is(".body_main")){
                var gnbSwiper = undefined;
    
                function initSwiper(){
                    var screenWidth = uiBasic.screenSet()[2];
    
                    if(screenWidth < 1023 && gnbSwiper == undefined) {
                        if(uiBasic.screenSet()[2] < 1023){
                            $(".gnb .depth .ai_inner").addClass("swiper-container");
                            $(".gnb .depth .ai_inner .depth1").addClass("swiper-wrapper");
                            $(".gnb .depth .ai_inner .depth1 > li").addClass("swiper-slide");
                        }
    
                        gnbSwiper = new Swiper(".gnb .depth .ai_inner", {
                            slidesPerView: "auto",
                            spaceBetween: 0,
                            freeMode: true,
                            // allowTouchMove:true,
                            // Responsive breakpoints
                            // breakpoints: {
                            //     // when window width is >= 320px
                            //     320: {
                            //         slidesPerView: 2.5,
                            //         spaceBetween: 0
                            //     },
                            //     // when window width is >= 480px
                            //     480: {
                            //         slidesPerView: 2.8,
                            //         spaceBetween: 0
                            //     },
                            //     // when window width is >= 640px
                            //     640: {
                            //         slidesPerView: 4.5,
                            //         spaceBetween: 0
                            //     },
                            // }
                        });

                        var curIndex = $(".gnb .depth .ai_inner .depth1 > li.active").index();
                        gnbSwiper.slideTo(curIndex);
                    } else if (screenWidth > 1023 && gnbSwiper != undefined) {
                        gnbSwiper.destroy();
                        gnbSwiper = undefined;
                        $(".gnb .depth .ai_inner").removeAttr('style');
                        $(".gnb .depth .ai_inner .depth1").removeAttr('style');
                        $(".gnb .depth .ai_inner .depth1 > li").removeAttr('style');
                    }
                }
    
                initSwiper();
                
                $(window).resize(function(){
                    initSwiper();
                });
            }


            $(window).resize(function(){
                if($(".mo_gnb .side_area").hasClass("on")){
                    uiHeader.gnb.moUnset();
                }
            });
        },
        moUnset: function(){
            $(".mo_gnb .side_area").css("transition","none").removeClass("on");
            uiLayerSet.scrollOn();
            setTimeout(function(){ $(".mo_gnb .side_area").removeAttr("style") },0);
        }
    },
    lnb: {
        init: function(){
            if($(".mo_gnb .lnb").length > 0){
                $(".mo_gnb .lnb .down_trigger").click(function(){
                    $(this).parent(".lnb").toggleClass("on");
                });

                $(window).scroll(function(){
                    uiHeader.lnb.close();
                });
            }
        },
        close: function(){
            if(uiBasic.screenSet()[2] > 1023){

            }else{
                $(".mo_gnb .lnb").removeClass("on");
            }
        }
    },
    snb: {
        init: function(){
            if($(".mo_gnb .snb").length > 0){
                // var curPos = $(".mo_gnb .snb_depth1 li.on").index() * $(".mo_gnb .snb_depth1 li.on").outerHeight();
                // $(".mo_gnb .snb_depth1").scrollTop(curPos);
                $(".mo_gnb .snb_depth2").removeClass("on");
                $(".mo_gnb .snb_depth2[data-label=" + $(".mo_gnb .snb_depth1 li.on .depth_item").data("control") + "]").addClass("on");

                $(".mo_gnb .snb .depth_item").click(function(){
                    $(".mo_gnb .snb_depth1 li").removeClass("on");
                    $(".mo_gnb .snb_depth2").removeClass("on");

                    $(".mo_gnb .snb_depth2[data-label=" + $(this).data("control") + "]").addClass("on");
                    
                    var curPos = $(this).parent("li").addClass("on").index() * $(this).outerHeight();
                    $(".mo_gnb .snb_depth1").scrollTop(curPos);
                });

                $(window).scroll(function(){
                    uiHeader.lnb.close();
                });
            }
        },
    },
    theme: function(){
        $(".header .theme_button").click(function(){
            $(this).toggleClass("on");
        });
    }
}

var uiEtc = {
    init: function(){
        $(".ui_keypad").length && this.keypad();
        $("[class^='menu_round']").length && this.tabResize();
    },
    keypad: function(){
        $(".ui_keypad").find(".pad_opener").click(function(){
            if($(this).parent(".ui_keypad").is(".opened")){
                $(this).parent(".ui_keypad").removeClass("opened").addClass("closed");
                $(this).find(".stat_txt").text("열기");

                $(this).closest(".solve_keypad").removeClass("on");
            }else{
                $(this).parent(".ui_keypad").removeClass("closed").addClass("opened");
                $(this).find(".stat_txt").text("닫기");

                $(this).closest(".solve_keypad").addClass("on");
            }
        });

        $(".keypad_tab").find(".tab_button").click(function(){
            $(".keypad_tab .tab_item").removeClass("on");
            $(this).parent(".tab_item").addClass("on");
        });
    },
    tabResize: function(){
        menuResize();

        $(window).resize(function(){
            menuResize();
        });
        
        function menuResize(){
            $("[class^='menu_round']").each(function(){
                var totalW = 0;
                var wrapW = $(this).width();

                $(this).find(".menu_item").each(function(){
                    var thisW = $(this).width();

                    totalW = totalW + thisW;          
                });

                if(wrapW < totalW){
                    $(this).addClass("loose");
                }else{
                    $(this).removeClass("loose");
                }

                if($(this).find(".menu_item.on").index() > 3){
                    $(this).scrollLeft(totalW);
                }
            });
        }
    }
}

var uiDetectOS = {
    init: function(){
        var OSName, classOS, usrAg = navigator.userAgent, usrAppv = navigator.appVersion;

        if(this.isMobile() == true){
            if( usrAg.match(/iPad/i) || usrAg.match(/iPod/i) || usrAg.match(/iPhone/i) ){
                if( usrAg.indexOf("OS") > -1 ){
                    OSName = "ios";
                    classOS = "mos_ios";
                }
            }else if( usrAg.match(/Android/i) ){
                if( usrAg.indexOf("Android") > -1 ){
                    OSName = "android";
                    classOS = "mos_android";
                }
            }
            else{
                OSName = 'unknown';
                classOS = 'mos_unknown';
            }

            $("body").addClass(classOS).addClass(classBrw);
        }else{
            if(usrAppv.indexOf("Win")!=-1){
                OSName="Windows";
                classOS = "os_win";
            }else if(usrAppv.indexOf("Mac")!=-1){
                OSName="MacOS";
                classOS = "os_mac";
            }else if(usrAppv.indexOf("X11")!=-1){
                OSName="UNIX";
                classOS = "os_unix";
            }else if(usrAppv.indexOf("Linux")!=-1){
                OSName="Linux";
                classOS = "os_linux";
            }
            else{
                OSName = "unknown OS";
                classOS = "os_unknown";
            }
        }

        var sBrowser, classBrw;
        // The order matters here, and this may report false positives for unlisted browsers.
        if(usrAg.indexOf("Firefox") > -1) {
            sBrowser = "Mozilla Firefox";
            classBrw = "b_firefox";
            // "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0"
        }else if(usrAg.indexOf("SamsungBrowser") > -1) {
            sBrowser = "Samsung Internet";
            classBrw = "b_si";
            // "Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G955F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.4 Chrome/67.0.3396.87 Mobile Safari/537.36
        }else if(usrAg.indexOf("Opera") > -1 || usrAg.indexOf("OPR") > -1) {
            sBrowser = "Opera";
            classBrw = "b_opera";
            // "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 OPR/57.0.3098.106"
        }else if(usrAg.indexOf("Trident") > -1) {
            sBrowser = "Microsoft Internet Explorer";
            classBrw = "b_ie";
            // "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; Zoom 3.6.0; wbx 1.0.0; rv:11.0) like Gecko"
        }else if(usrAg.indexOf("Edge") > -1) {
            sBrowser = "Microsoft Edge";
            classBrw = "b_edge";
            // "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"
        }else if(usrAg.indexOf("Chrome") > -1) {
            sBrowser = "Google Chrome or Chromium";
            classBrw = "b_chrome";
            // "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.181 Chrome/66.0.3359.181 Safari/537.36"
        }else if(usrAg.indexOf("Safari") > -1) {
            sBrowser = "Apple Safari";
            classBrw = "b_safari";
            // "Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.0 Mobile/15E148 Safari/604.1 980x1306"
        }
        else {
            sBrowser = "unknown Broswer";
            classBrw = "b_unknown";
        }

        $("body").addClass(classOS).addClass(classBrw);

        return [this.isMobile(), OSName, sBrowser];
    },
    isMobile: function(){
        var UserAgent = navigator.userAgent;

        if( UserAgent.match(/iPhone|iPod|Android|Windows CE|BlackBerry|Symbian|Windows Phone|webOS|Opera Mini|Opera Mobi|POLARIS|IEMobile|lgtelecom|nokia|SonyEricsson/i) != null || UserAgent.match(/LG|SAMSUNG|Samsung/) != null ){
            return true;
        }else{
            return false;
        }
    }
}


/*///////////////////////////////////////////////////////////////*/
/* *** Content ************************************************* */
/*///////////////////////////////////////////////////////////////*/

var uiConMain = {
    init: function(){
        if($(".container.main").length > 0){
            this.visualHover();
            $(".main_sld").length && this.swiper1();
            $(".main_sbj_sld").length && this.swiper2(4);
        }
    },
    visualHover: function(){
        $(".cont_list_link li").hover(function(){
            $(this).siblings("li").removeClass("on");
            $(this).addClass("on");
        });
    },
    swiper1: function(){

        var main_sld = new Swiper(".main_sld", {
            pagination: {
                el: ".main_sld_pager",
                clickable: true,
                // renderBullet: function (index, className) {
                //     var menu = [];
                //     $(".vertical_swiper > .swiper-wrapper > .swiper-slide").each(function(i) {
                //         menu.push($(this).data("name"));
                //     });

                //     return '<span class="' + className + '"><em class="name_tag">' + (menu[index]) + '</em></span>';
                // },
            },
            breakpoints: {
                // when window width is >= 640px
                640: {
                    // slidesPerView: 1,
                    // spaceBetween: 0,
                    // freeMode: false,
                },
            },
            on: {
                beforeResize: function(){
                    // console.log($(window).width());
                },
                resize: function(){
                    // console.log($(window).width());
                }
            },
        });
    },
    swiper2 : function(){
        var main_sbj_sld = new Swiper(".main_sbj_sld", {
            slidesPerView: 4,
            spaceBetween: 28,
            navigation: {
                nextEl: ".button_next",
                prevEl: ".button_prev",
            },
            on: {
                init: function(){
                    // console.log(this.slides.length);
                    // $(".button_prev").click(function(){
                    //     // console.log(main_sbj_sld.realIndex);
                    //     if(main_sbj_sld.realIndex == 0){
                    //         setTimeout(function(){ alert("처음 과목입니다"); },300);
                    //     }
                    // });

                    // $(".button_next").click(function(){
                    //     console.log(main_sbj_sld.realIndex);
                    //     if(main_sbj_sld.realIndex >= 1){
                    //         setTimeout(function(){ alert("마지막 과목입니다"); },300);
                    //     }
                    // });
                },
                slideCahnge: function(){

                },
                reachBeginning: function () {
                    setTimeout(function(){ alert("처음 과목입니다"); },500);
                },
                reachEnd: function () {
                    if(this.slides.length > 4){
                        setTimeout(function(){ alert("마지막 과목입니다"); },500);
                    }
                }
            },
            // Responsive breakpoints
            breakpoints: {
                // when window width is >= 320px
                // 320: {
                //     slidesPerView: 1,
                //     spaceBetween: 10
                // },
                // when window width is >= 480px
                480: {
                    slidesPerView: 1,
                    spaceBetween: 16
                },
                // when window width is >= 640px
                640: {
                    slidesPerView: 2,
                    spaceBetween: 10
                },
                // when window width is >= 1023px
                1023: {
                    slidesPerView: 3,
                    spaceBetween: 10
                }
            }
        });
    }
}

var uiConRecom = {
    init: function(){
        $(".weak_card .card_list").length && this.weakCardSet();
    },
    weakCardSet: function(){
        $(".weak_card").addClass("swiper-container");
        $(".weak_card .card_list").addClass("swiper-wrapper");
        $(".weak_card .card_list li").addClass("swiper-slide");

        this.weakCardSwiper();
    },
    weakCardSwiper: function(){
        var weakcardSwiper = undefined;

        function initSwiper(){
            var screenWidth = uiBasic.screenSet()[2];

            if(screenWidth < 1023 && weakcardSwiper == undefined) {
                weakcardSwiper = new Swiper(".weak_card", {
                    slidesPerView: 5,
                    spaceBetween: 15,
                    freeMode: true,
                    // Responsive breakpoints
                    breakpoints: {
                        // when window width is >= 320px
                        320: {
                            slidesPerView: 2.2,
                            spaceBetween: 15
                        },
                        // when window width is >= 480px
                        480: {
                            slidesPerView: 2.2,
                            spaceBetween: 15
                        },
                        // when window width is >= 640px
                        640: {
                            slidesPerView: 4.5,
                            spaceBetween: 15
                        },
                    }
                });
            } else if (screenWidth > 1023 && weakcardSwiper != undefined) {
                weakcardSwiper.destroy();
                weakcardSwiper = undefined;
                $('.weak_card .card_list').removeAttr('style');
                $('.weak_card .card_list li').removeAttr('style');
            }
        }

        initSwiper();

        $(window).resize(function(){
            initSwiper();
        });
    },
}

var uiContent = {
    init: function(){
        $(".bbs_type2").length && this.boxLayer();
        $(".contain_top .btn_drop").length && this.boxHead();
        $(".ai_con_lect .lect_recom .rank_list").length && this.lecList();
        $(".ai_con_recom.type_jhs").length && this.conRecomJhs();
    },
    boxLayer: function(){
        // UI-PRI-CR-5401
        $(document).off('click','.box-layer .btn_add');
        $(document).on('click','.box-layer .btn_add',function(){
            if($(this).next().hasClass('on') == 0){
                $('.layer_add').removeClass('on')
                $(this).next().addClass('on')
            }else{
                $(this).next().removeClass('on')
            }
        });

        $(document).off('click','.box-layer .btn_close');
        $(document).on('click','.box-layer .btn_close',function(){
            $('.layer_add').removeClass('on');
        });
    },
    boxHead: function(){
        // UI-PRI-CR-5401
        $(document).off('click','.contain_top .btn_drop');
        $(document).on('click','.contain_top .btn_drop',function(){
            if($(this).closest('.contain_top').hasClass('on') == 0){
                $(this).addClass('on').closest('.contain_top').addClass('on');
                $(this).text('열기');
            }else{
                $(this).removeClass('on').closest('.contain_top').removeClass('on');
                $(this).text('접기');
            }
        });
    },
    lecList: function(){
        // UI-PRI-CR-3001
        $(".round_box.lect_recom .btn_more").click(function(){
            $(".round_box.lect_recom").toggleClass("more");

            if($(".round_box.lect_recom").hasClass("more")){
                $(this).find("span").text("더보기 닫기");
            }else{
                $(this).find("span").text("더보기");
            }
        });
    },
    conRecomJhs: function(){
        // UI-JHS-CR-2001
        if($(".status_steps").length && $(".status_steps").is(".current3, .current4")){
            $(".status_steps .step").scrollLeft(405);
        }
    },
}

var num_toggle = {
    init: function(){
        var mun_wrap = $(".top_num_list");
        var mun_list_wrap = $(".top_num_list ul");
        var mun_list = $(".top_num_list ul li");
        var btn_mun = $(".top_num_list ul li button");
        var target = $(".top_num_list ul li").find(".focus");
        $(btn_mun).click(function(){
            $(mun_list).removeClass("focus");
            $(this).parent().addClass("focus");

            //$(mun_list_wrap).scrollLeft(target);
        });
        $(mun_list_wrap).each(function (){
            var _width = $(mun_list_wrap).width(),
                _width2 = $(mun_list).width(), 
                _length = $(mun_list).length,
                //_width3 = _width2 * _length,
                _index = $(this).find(".focus").index(),
                _index4 = _width2 * _index;
            //var test = _index4;
                      
            $(this).scrollLeft(_index4);
            //console.log(_index4);
        });
    }
}

var omrbox_toggle = {
    init: function(){
        $(".btn_omr_auto").click(function(){
            $("body").toggleClass("active");
            
            if($(".omrbox_wrap").hasClass("active") === true) {
                $(".omrbox_wrap").removeClass("active");
            }else{
                $(".omrbox_wrap").addClass("active");
            }
        });
    }
}

var foot_toggle = {
    init: function(){
        $(".btn_foot_toggle").click(function(){            
            if($(".foot_fixed").hasClass("active") === true) {
                $(".foot_fixed").removeClass("active");
                $(".btn_foot_toggle").removeClass("on");
            }else{
                $(".foot_fixed").addClass("active");
                $(".btn_foot_toggle").addClass("on");
            }
        });
    }
}

var correctSwitch = {
    init: function(){
        $('.correctbox .switch_box').click(function () {
            var orderChk = $('.correctSwitch').is(':checked');
            var correct = $('.correctbox .boardcorrect');
            if(!!orderChk){
                $(correct).addClass('chk_active');
            }else{
                $(correct).removeClass('chk_active');
            }
        });
    }
}

/*///////////////////////////////////////////////////////////////*/
/* *** 임시 스크립트 (퍼블에서만 확인할 경우 여기서 실행) ********** */
/*///////////////////////////////////////////////////////////////*/
var tempPublish = {
    init: function(){

        if(getExtensionOfFilename(window.location.href) == ".html"){
            // 퍼블에서만 확인할 경우 여기서 실행
            uiTheme.init(); // 테마

            $(".sort_view .check_imp").click(function(){
                $(this).toggleClass("on");
            });
        }

        function getExtensionOfFilename(filename) {

            var _fileLen = filename.length;
            var _lastDot = filename.lastIndexOf('.');
            var _fileExt = filename.substring(_lastDot, _fileLen).toLowerCase();

            return _fileExt;
        }
    }
}
var uiTheme = {
    init: function(){
        var agent = navigator.userAgent.toLowerCase();
        if ( (navigator.appName == 'Netscape' && navigator.userAgent.search('Trident') != -1) || (agent.indexOf("msie") != -1) ) {
            // console.log("Internet Explorer");
            // $(".btn_theme").parents(".btn_setting").hide();
        }else {
            // console.log("Not Internet Explorer");

            // Put this Code on the last : IE file:// protocol issue
            this.setTheme();
        }
    },
    setTheme: function(){
        var themeName = localStorage.getItem("guidetheme");

        if(themeName == "white"){
            $("body").addClass("theme_white");
        }
        if(themeName == "dark"){
            $("body").removeClass("theme_white");
        }
    }
}


/*///////////////////////////////////////////////////////////////*/
/* *** 추가 스크립트 (확인필요) ********** */
/*///////////////////////////////////////////////////////////////*/
// $(function(){
//     if($(window).width() < 1023){
//         $('.menu_item.on').on('click',function(e){
//             e.preventDefault();
//             if($('.menu_base.unit_response').hasClass('on') == 0){
//                 console.log('test');
//                 $('.menu_base.unit_response .menu_item').css({'height':'auto'});
//                 $('.menu_base.unit_response').addClass('on')
//             }else{
//                 $('.menu_base.unit_response .menu_item').not($('.menu_base.unit_response .menu_item.on')).css({'height':0});
//                 $('.menu_base.unit_response').removeClass('on')
//             }


//         });
//     }

// })
