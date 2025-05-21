var objectUtils = {
	copyElement : function(ele, evt){
		try{
			var $ele = $(ele).clone();
			var tagName = $ele.prop('localName');
			var newElement = $('<'+tagName+'/>');
			var attributes = Array.from($ele[0].attributes);
			
			Object.keys(attributes).forEach(function(v,i){
				newElement.attr(attributes[v].name,attributes[v].value) 
			});
			
			if(evt && stringUtils.isNotEmpty(evt.name)){
				newElement.on(evt.name, evt.evtFn);
			}
			return newElement;
		}catch(e){
			return ele;			
		}
	},
	isElement : function(ele){
		try{
			var element = ele;
			if(Array.isArray(ele)){
				element = ele[0];
			}
			return stringUtils.isNotEmpty($(element)[0].nodeName);
		}catch(e){
			return false;
		}
	}
}