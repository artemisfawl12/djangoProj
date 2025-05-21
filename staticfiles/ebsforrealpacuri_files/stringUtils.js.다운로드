var stringUtils = {
	EMPTY : '',
	isEmpty : function(str){
		try{
			if(typeof str === "number") str = String(str);
			if(typeof str === "boolean") str = String(str);
			
			var deniedStrReg = /(null)|(undefined)|(NaN)|(\[)|(\])/gi;
			
			if(typeof str === 'object'){
				str = JSON.stringify(Object.keys(str));	
			}
			str = str.replace(deniedStrReg, '');
			return str === undefined || str.trim().length < 1;
		}catch(e){
			return true;
		}
	},
	isNotEmpty : function(str){
		return !this.isEmpty(str);
	},
	nvl : function(str, def){
		def = this.isEmpty(def) ? this.EMPTY : def;
		if(this.isEmpty(str)){
			return String(def);
		}else{
			if(typeof str === 'object'){
				return str;
			}else{
				return String(str);
			}
		}
	},
	lpad : function(str, digit, char){
		return this.pad(str, digit, char,'left');
	},
	rpad : function(str, digit, char){
		return this.pad(str, digit, char,'right');
	},
	pad : function(str, digit, char, pos){
		digit 	= digit || 2;
		char 	= char || '0';
		pos 	= pos || 'left';
		
		var s = this.nvl(String(str));
		if(s.length < digit){
			for(var i=s.length; i<digit; i++){
				switch(pos){
					case 'right' : s += char; break;
					case 'left' : s = char + s; break;
				}
			}
		}
		return s;
	},
	toLowerCase : function(str){
		try{
			return this.nvl(str).toLowerCase()
		}catch(e){
			return str;
		}
	},
	randomCode : function(len, prefix){
		len = Number(this.nvl(len, 10));
		prefix = this.nvl(prefix, 'EBS_RC');
		
		var str = prefix+Math.floor(Math.random()*1000000)+'_'+new Date().getTime();
		return str.substr(0,len);
	},
	convert : {
		toStringParams : function(param){
			var _this = this;
			try{
				param = stringUtils.nvl(param,'{}')
				if(typeof param !== 'string'){
					param = JSON.stringify(param);
				}
				if(param.startsWith('encoed')){
					return param;
				}else{
					var encoded = _this.uri.encode(param);
					return 'encoed'+encoded;		
				}
			}catch(e){
				return 'encoed'+_this.uri.encode('{}');
			}
		},
		toObjectParams : function(param){
			try{
				return JSON.parse(this.toObjectStringParams(param));
			}catch(e){
				return {};				
			}
		},
		toObjectStringParams : function(param){
			var _this = this;
			try{
				param = stringUtils.nvl(param).replace(/^encoed/gi,'');
				var str = _this.uri.decode(param);
				return str;
			}catch(e){
				return '{}';				
			}
		},
		queryString2Json : function(str){
			var _this = this;
			var result = {};
			try{
				stringUtils.nvl(str).split('&').forEach(function(k){				
					var d = stringUtils.nvl(k).split('=');
					result[_this.uri.decode(d[0])] = _this.uri.decode(d[1]);					
				});				
			}catch(e){
				console.debug(e);
			}
			return result
		},
		uri : {
			encode : function(str){
				try{
					return encodeURIComponent(escape(str));					
				}catch(e){
					console.error(e)
				}
			},
			decode : function(str){
				try{
					return unescape(decodeURIComponent(str.replace(/\+/g, " ")));					
				}catch(e){
					console.error(e)
				}
			}
		}
	},
	regEx : {
		onlyNumber : function(str, defaultStr){
			defaultStr = stringUtils.nvl(defaultStr, '');
			return stringUtils.nvl(str, defaultStr).replace(/[^0-9]/gi,'');
		},
		removeSpace : function(str, defaultStr){
			defaultStr = stringUtils.nvl(defaultStr, '');
			return stringUtils.nvl(str, defaultStr).replace(/\s/gi,'');
		},
		onlyNumberNAlpha : function(str, defaultStr){
			defaultStr = stringUtils.nvl(defaultStr, '');
			return stringUtils.nvl(str, defaultStr).replace(/[^a-zA-Z0-9]/gi,'');
		},
		onlyNumberDecimal : function(str, defaultStr){
			defaultStr = stringUtils.nvl(defaultStr, '');
			return stringUtils.nvl(str, defaultStr).replace(/[^0-9.]/gi,'');
		},
		numberComma : function(str, defaultStr){
			defaultStr = stringUtils.nvl(defaultStr, '');
			return stringUtils.nvl(str, defaultStr).replace(/\B(?=(\d{3})+(?!\d))/g,',');
		},
	},
	sort : {
		all : function(str, sep){
			var _this = this;
			var sepSort = _this.separator(str,sep);
			if(stringUtils.isNotEmpty(sepSort)){
				var result = new Array();
				sepSort.split(',').forEach(function(k){
					result.push(_this.separator(k,''))	
				});
				sepSort = result.join(sep);
			}
			return sepSort;
		},
		separator : function(str, sep){
			try{
				sep = sep == null || typeof sep == 'undefined'  ? ',' : sep;
				
				if(stringUtils.isNotEmpty(str)){
					return stringUtils.nvl(str).split(sep).sort().join(sep);
				}else{
					throw '';
				}			
			}catch(ee){
				return stringUtils.EMPTY
			}
		}
	},
	//#20220304
	catNmNvl : function(str){
		if(typeof str == "undefined" || str == "" || str == null){
			return "";
		}else{
			return " > "+str;
		}
	}
	
}

String.prototype.equals = function(str, isIgnoreCase){
	if(typeof isIgnoreCase != 'boolean') isIgnoreCase = true;
	
	var source = stringUtils.nvl(String(this));
	var target = stringUtils.nvl(str);
   	
	if(isIgnoreCase){
		source = stringUtils.toLowerCase(source);
		target = stringUtils.toLowerCase(target);
	}

	return source === target;
}
