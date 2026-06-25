/* Add home-page class for full-width layout */
document.addEventListener("DOMContentLoaded", function () {
  if (document.location.pathname === "/" || document.location.pathname.endsWith("/index.html")) {
    document.body.classList.add("bio-home");
  }

  if (typeof mermaid !== "undefined") {
    mermaid.initialize({
      startOnLoad: true,
      theme: document.body.dataset.mdColorScheme === "mint-dark" ? "dark" : "default",
      securityLevel: "loose",
    });
  }

  var observer = new MutationObserver(function () {
    var scheme = document.body.dataset.mdColorScheme;
    if (typeof mermaid !== "undefined" && scheme) {
      mermaid.initialize({
        theme: scheme === "mint-dark" ? "dark" : "default",
      });
    }
  });
  observer.observe(document.body, { attributes: true, attributeFilter: ["data-md-color-scheme"] });
});
