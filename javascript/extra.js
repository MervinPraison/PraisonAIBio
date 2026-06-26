/* PraisonAIBio docs — layout helpers and theme-aware Mermaid */
document.addEventListener("DOMContentLoaded", function () {
  var path = document.location.pathname;
  if (path === "/" || path.endsWith("/index.html") || path.endsWith("/")) {
    document.body.classList.add("bio-home");
  }

  function mermaidTheme() {
    return document.body.dataset.mdColorScheme === "bio-dark" ? "dark" : "default";
  }

  if (typeof mermaid !== "undefined") {
    mermaid.initialize({
      startOnLoad: true,
      theme: mermaidTheme(),
      securityLevel: "loose",
    });
  }

  var observer = new MutationObserver(function () {
    if (typeof mermaid !== "undefined" && document.body.dataset.mdColorScheme) {
      mermaid.initialize({ theme: mermaidTheme() });
    }
  });
  observer.observe(document.body, { attributes: true, attributeFilter: ["data-md-color-scheme"] });
});
