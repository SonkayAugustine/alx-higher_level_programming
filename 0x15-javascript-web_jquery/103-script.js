const query_url ="https://fourtonfish.com/hellosalut/?lang=fr";
document.addEventListener("DOMContentLoaded", function () {
    $("INPUT#btn_translate").click(function () {
    $.get(url + $("INPUT#language_code").val(), function (data, status) {
	if (status === "success") {
	    $("DIV#hello").text(data.hello);
	}
    });
 });
 $("INPUT#language_code").focus(function () {
    $("INPUT#language_code").keydown(function (beep) {
	if (beep.KeyCode === 13) {
	    $.get(url + $("INPUTlanguage_code").val(), function (data, status) {
		if (status === "success") {
		    $("DIV#hello").text(data.hello);
		}
	    });
	}
    });
 });
});
