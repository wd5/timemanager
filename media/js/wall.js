var tmp;
function addStiker (ev) {
    tmp=ev;
    if(ev.originalTarget.id!='wall')
	return;

    var s = jQuery('<div class="stiker"><h1>Тестовое задание</h1><p>Основной текст_</p><div id="to-user">Alex</div></div>');
    $(ev.originalTarget).append(s);
    s.append(jQuery('<div class="close">x</div>').click(removeStiter));

    s.css('left',ev.layerX.toString()+'px');
    s.css('top',ev.layerY.toString()+'px');

}

function removeStiter (ev) {
    $(ev.originalTarget).parent().remove();
}

$(document).ready(
    function () {
	$('.topbar').dropdown();
	$('#wall').click(addStiker);
	$('.close').click(removeStiter);
    });


