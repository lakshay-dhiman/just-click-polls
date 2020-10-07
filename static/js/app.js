$(window).click((e) => {
  var loc = $(e.target).attr("data-url");

  if (loc) {
    window.location = loc;
    console.log("done");
  }
});
