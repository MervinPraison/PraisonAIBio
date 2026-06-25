/* PraisonAIBio docs — Mermaid dark theme + subtle UX polish */

document.addEventListener("DOMContentLoaded", function () {
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
