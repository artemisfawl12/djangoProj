String.prototype.Equals=function(strValue)
{
    return strValue==this;
}
String.prototype.trim = function ()
{
	var objRegExp = /^(\s*[?]*[ ]*)$/;
	if(objRegExp.test(this))
	{
		var strValue = this.replace(objRegExp,'');
		if( strValue.length == 0 ) return strValue;
	}

	objRegExp = /^(\s*[?]*[ ]*)([\w\W]*)(\b\s*[?]*[ ]*$)/;
	if(objRegExp.test(this))
	{
		return this.replace(objRegExp,'$2');
	}

	return this;
}

String.prototype.replaceText=function(strOld,strNew)
{
	if(typeof strOld !== "string") return; 
	
	var strList = this.split(strOld);
	var strValue ="";
	for(var i=0;i<strList.length;i++)
	{
		if(i>0)
			strValue+=strNew;
		strValue+=strList[i];
	}
	return strValue;
}
String.prototype.getByteLength=function()
{
	if (typeof this !== "string") {
        return;
    }
	
	var nByteLength=0;
	for (var i=0; i<this.length; i++)
	{
		nByteLength++;
		if(this.charCodeAt(i)>255)
			nByteLength++;
	}
	return nByteLength;
}
String.prototype.getByteIndex=function(nIndex)
{
	if (typeof this !== "string") {
        return;
    }
	
	var nByteLength=0;
	for (var i=0; i<this.length; i++)
	{
		nByteLength++;
		if(this.charCodeAt(i)>255)
			nByteLength++;
		if(nByteLength>=nIndex)
			return i;
	}
	return nByteLength;
}
Boolean.prototype.Validate = function(value) 
{
    value = value.toString().toLowerCase();
    return value.Equals("true") || value.Equals("false");

}
Boolean.Validate = function(value) 
{
    value = value.toString().toLowerCase();
    return value.Equals("true") || value.Equals("false");

}
Boolean.prototype.Parse = function(value) 
{
    if (!Boolean.prototype.Validate(value))
        throw new Error("error");
    value = value.toString().toLowerCase();
    return value.Equals("true") ? true : false;

}
Boolean.Parse = function(value)
{
    if (!Boolean.Validate(value))
        throw new Error("error");
    value = value.toString().toLowerCase();
    return value.Equals("true") ? true : false;

}
function Utility()
{
	this.GetNumberString =function(nNumber,nSize)
	{
		try
		{
			var strNumber = this.ParseInt(nNumber.toString()).toString();
			while(strNumber.length < nSize)
			{
				strNumber = "0"+strNumber; 
			}
			return strNumber;
			
		}
		catch (e)
		{
			return "0";
		}
		
	};
	this.CheckObject=function(obj)
	{
		if(obj==null||typeof(obj)=="undefined")
			return false;
		else
			return true;
	};
	this.GetXMLHttpObject=function()
	{
		var obj = (window.ActiveXObject) ? new ActiveXObject("Microsoft.XMLHTTP") : new XMLHttpRequest();
		return obj;
	};
	this.GetFileName = function(strURL)
	{
		var nIndex = strURL.lastIndexOf("/");
		if(nIndex<0)
			return strURL;
		else
			return strURL.substring(nIndex);
				
	};
	this.GetWeb=function(strURL,strParam)
	{
		try
	    {
	        if (!this.CheckObject(strParam))
	            strParam = "";
			var objXMLHttp=this.GetXMLHttpObject();
			var strText = "";
			var strMethod=strParam.length>0?"POST":"GET";
			if (objXMLHttp)
			{
				objXMLHttp.open(strMethod, strURL, false);
				objXMLHttp.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded;charset=UTF-8');
				objXMLHttp.setRequestHeader("Content-length", strParam.length); 
				objXMLHttp.send(strParam);
				strText=objXMLHttp.responseText;
				strText=strText.trim();
			}		
			return strText+"";
		}
		catch(e)
		{
			console.log('error : ' + e.message);
		}
		return "";
	};
	this.SendWeb=function(strURL,strParam,objCallback)
	{
		try
	    {
	        if (!this.CheckObject(strParam))
	            strParam = "";
			var objXMLHttp=this.GetXMLHttpObject();
			var strMethod=strParam.length>0?"POST":"GET";
			if (objXMLHttp)
			{
				objXMLHttp.open(strMethod, strURL, true);
				objXMLHttp.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded;charset=UTF-8');
				objXMLHttp.setRequestHeader("Content-length", strParam.length);
				objXMLHttp.onreadystatechange=objCallback;
				objXMLHttp.send(strParam);
			}		
			return objXMLHttp;
		}
		catch(e)
		{
			console.log('error : ' + e.message);
		}
		return "";
	};
	this.NullCheck = function(strValue)
	{
	    if (this.CheckObject(strValue))
	        return strValue;
	    return "";
	};
	this.ParseInt = function(strNumber)
	{
	    if (!this.CheckObject(strNumber))
	        return 0;
	    strNumber = strNumber + "";
	    strNumber = strNumber.trim();
	    try
	    {
	        var nNumber = parseInt(Number(strNumber));
	        if (nNumber.toString() == "NaN")
	            nNumber = 0;
	        return nNumber;
	    }
	    catch (e)
	    {
	        return 0;
	    }
	};
	this.ParseUINT = function(strNumber)
	{
	    return this.ParseInt(strNumber);
	};
	this.ParseDouble = function(strNumber)
	{
	    if (!this.CheckObject(strNumber))
	        return 0;
	    strNumber = strNumber + "";
	    strNumber = strNumber.trim();
	    try
	    {
	        var dbNumber = parseFloat(strNumber);
	        return dbNumber;
	    }
	    catch (e)
	    {
	        return 0.0;
	    }
	};
	this.ParseNumber=function(strNumber)
	{
	    if (typeof (strNumber) == "undefined" || strNumber == null)
	        return 0;
	    strNumber = strNumber + "";

	    strNumber = strNumber.trim();
	    try
	    {
	        var dbNumber = parseFloat(strNumber);
	        var nNumber = parseInt(Number(strNumber));
	        if (dbNumber.toString() == "NaN")
	            dbNumber = 0;
	        if (nNumber.toString() == "NaN")
	            nNumber = 0;
	        if (dbNumber - nNumber == 0)
	            return nNumber;
	        else
	            return dbNumber;
	    }
	    catch (e)
	    {
	        return 0;
	    }
	};
	this.ParseBoolean = function(strBool)
	{
	    try
	    {
	        return Boolean.Parse(strBool);
	    }
	    catch (e)
	    {
	        return false;
	    }
	};
	this.LoadXMLString = function(strXML)
	{
	    try
	    {
			var nIndex = strXML.indexOf("<");
			if(nIndex>0)
				strXML = strXML.substring(nIndex);
	        var xmlDom = this.GetXMLDom();
	        if (xmlDom.loadXML(strXML) == false)
	            return null;

	        return xmlDom.documentElement;
	    }
	    catch (e)
	        {
	        this.Trace(e);
	        return null;
	    }
	};
	this.TraceWarning=function (obj)
	{
		
	};
	this.Trace = function(obj)
	{
	    
	};
	this.GetFileExt=function(strFileName)
	{
		var nIndex = strFileName.lastIndexOf(".");
		if(nIndex<0)
			return "";
		return strFileName.substring(nIndex+1);
	};

	this.GetText = function(xElement)
	{
		try
		{

		    if (g_bExplorer)
		        return xElement.text;
		    else
		    {
		    	if(xElement.firstChild)
		    		return xElement.firstChild.nodeValue;
		    	else 
		    		return xElement.nodeValue;
		    }
		}
		catch(e)
		{
			return "";
		}
	};
	this.AppendXMLElement = function(strTagName, strText, xDoc, xElement) 
	{
	    var newNode = xDoc.createNode(1, strTagName, "");
	    setXMLTextValue(newNode, strText);
		xElement.appendChild(newNode);
		return newNode;
	};
	this.GetXMLDom=function()
	{
		var xmlDom;
		try
		{
			if(window.ActiveXObject) 
			{
				xmlDom=new ActiveXObject("MSXML2.DOMDocument");
				xmlDom.async = false;
				xmlDom.validateOnParse = false;
				return xmlDom;
			}
			else
			{
					xmlDom = new Object();//new DOMParser();
					xmlDom.dom = null;
					xmlDom.documentElement = null;
					xmlDom.document = null;
					xmlDom.createNode=function(strType,strTagName,strBaseURL)
					{
						if(this.document==null)
							return null;
						var objElement = this.document.createElement(strTagName);
						return objElement;
					};
					xmlDom.parser = new DOMParser();
					xmlDom.loadXML=function(strXML)
					{
						if(strXML=="")
							return  null;
						this.dom=this.parser.parseFromString(strXML,"text/xml");
						this.documentElement=this.dom.documentElement;
						if(this.documentElement)
							this.document=this.documentElement.ownerDocument;
					};
					xmlDom.load=function(strURL)
					{
						var strText = getWeb(strURL,"");
						return this.loadXML(strText);
					};
					xmlDom.getXML=function()
					{
						var s = new XMLSerializer();
						return s.serializeToString(this.dom);
					};
					return xmlDom;
			}
		}
		catch(e)
		{
			this.Trace(e.message);
			return null;
		}
		return null;
	};
	this.GetXMLDocument=function(strURL,strParam)
	{
		var strXMLBody=this.GetWeb(strURL,strParam);
		var nIndex = strXMLBody.indexOf("<");
		if(nIndex<0)
			return null;
		var strReplace = strXMLBody.substr(0,nIndex);
		strXMLBody=strXMLBody.replace(strReplace,"");
		if(strXMLBody.length==0)
			return null;
		var xmlDom = getXMLDom();
		var strXML="<?xml version=\"1.0\" encoding=\"euc-kr\"?>";
		strXML+=strXMLBody;
		//document.write(strXML);
		if(xmlDom.loadXML(strXML)==false)
			return null;
		return xmlDom.documentElement;

	};
	this.GetXMLHeader=function()
	{
	    return "<?xml version=\"1.0\" encoding=\"euc-kr\"?>";
	};
	this.GetXmlTagDocument=function(strTag)
	{
	    var xmlDom = this.GetXMLDom();
	    var strXML = this.GetXMLHeader() + "<" + strTag + "/>";
		if(xmlDom.loadXML(strXML)==false)
		    return null;
		return xmlDom;
	};
	this.GetXMLRootDocument=function (strURL)
	{
		try
		{
			var xmlDom = this.GetXMLDom();
		//	var strXML = getWeb(strURL,"");
			if(xmlDom.load(strURL)==false)
				return null;
			return xmlDom.documentElement;
		}
		catch(e)
		{
			return null;
		}

	};
	this.GetStringRootDocument=function (strXML)
	{
		try
		{
			
			var xmlDom = this.GetXMLDom();
			if(xmlDom.loadXML(strXML)==false)
				return null;

			return xmlDom.documentElement;
		}
		catch(e)
		{
			this.Trace(e.message);
			return null;
		}
	};

	this.GetCenterLeft=function(nWidth)
	{
		var nAvail= this.GetMaxWidth()-nWidth;
		if(nAvail<=0)
			return 0;
		return  this.ParseInt(Number(nAvail/2));

	};

	this.GetCenterTop=function(nHeight)
	{
		var nAvail= this.GetMaxHeight()-nHeight;
		if(nAvail<=0)
			return 0;
		return this.ParseInt(Number(nAvail/2));

	};
	this.GetMaxWidth=function()
	{
		return screen.availWidth;
	};
	this.GetMaxHeight=function()
	{
		return screen.availHeight-55;
	};
	this.OpenPopUp=function(strURL, strName, nWidth, nHeight, nScrollbars)
	{
		var strMsg="can't open popup window";
		var strFeatures="";
		
		var nTop=this.GetCenterTop(nHeight);
		var nLeft = this.GetCenterLeft(nWidth);
		var nToolbar=0;
		var nDirectory=0;
		var nFullscreen=0;
		var nLocation=0;
		var nMenubar =0;
		var nResizable =1;
		if (!this.CheckObject(nScrollbars))
		    nScrollbars = 1;

		nHeight = this.GetMaxHeight() < nHeight ? this.GetMaxHeight() : nHeight;
		nWidth = this.GetMaxWidth() < nWidth ? this.GetMaxWidth() : nWidth;
		var nStatus  = 0;
		var nTitlebar = 1;
		strFeatures="top=" + nTop;
		strFeatures+=",left=" + nLeft;
		strFeatures+=",width=" + nWidth;
		strFeatures+=",height=" + nHeight;
		strFeatures+=",toolbar=" + nToolbar;
		strFeatures+=",directory=" + nDirectory;
		strFeatures+=",fullscreen=" + nFullscreen;
		strFeatures+=",location=" + nLocation;
		strFeatures+=",menubar=" + nMenubar;
		strFeatures+=",resizable=" + nResizable;
		strFeatures+=",scrollbars =" + nScrollbars;
		strFeatures+=",status=" + nStatus;
		strFeatures+=",titlebar=" + nTitlebar;
		try
		{
			
			var popWnd=window.open(strURL,strName,strFeatures);
		
			if(popWnd==null)
			{
				alert(strMsg);
				return null;
			}
			popWnd.focus();
			return popWnd;
		}
		catch (e)
		{
			alert(e.message);
			return null;
		}
		

	};

}
var Utilities = new Utility();
