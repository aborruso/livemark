document.addEventListener("DOMContentLoaded", function () {
  function makeIds() {
    var content = document.querySelector(".markdown-body");
    var headings = content.querySelectorAll("h1, h2, h3, h4, h5, h6, h7");
    var headingMap = {};

    Array.prototype.forEach.call(headings, function (heading) {
      var id = heading.id
        ? heading.id
        : heading.textContent
            .trim()
            .toLowerCase()
            .split(" ")
            .join("-")
            .replace(/[!@#$%^&*():]/gi, "")
            .replace(/\//gi, "-");
      headingMap[id] = !isNaN(headingMap[id]) ? ++headingMap[id] : 0;
      if (headingMap[id]) {
        heading.id = id + "-" + headingMap[id];
      } else {
        heading.id = id;
      }
    });
  }
  makeIds();
  tocbot.init({
    // Where to render the table of contents.
    tocSelector: "#livemark-sidebar",
    // Where to grab the headings to build the table of contents.
    contentSelector: ".markdown-body",
    // Which headings to grab inside of the contentSelector element.
    headingSelector: "h1, h2, h3",
    // For headings inside relative or absolute positioned containers within content.
    hasInnerContainers: true,
  });
});
