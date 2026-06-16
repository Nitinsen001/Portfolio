(() => {
  const prefersReducedMotion = window.matchMedia?.("(prefers-reduced-motion: reduce)")?.matches;

  // Cursor spotlight (drives CSS --cursor-x/--cursor-y)
  if (!prefersReducedMotion) {
    let raf = 0;
    window.addEventListener(
      "mousemove",
      (e) => {
        if (raf) return;
        raf = window.requestAnimationFrame(() => {
          raf = 0;
          const x = `${e.clientX}px`;
          const y = `${e.clientY}px`;
          document.documentElement.style.setProperty("--cursor-x", x);
          document.documentElement.style.setProperty("--cursor-y", y);
        });
      },
      { passive: true }
    );
  }

  // Reveal-on-scroll (adds heavy but clean animation across existing "project items")
  const revealTargets = () => {
    const selector = [
      "section",
      ".hero-content",
      ".hero-image",
      ".about-container",
      ".skills-container",
      ".skill-category",
      ".projects-grid",
      ".project-card",
      ".contact-grid",
      ".contact-container",
      ".container",
      ".section",
    ].join(",");

    const nodes = Array.from(document.querySelectorAll(selector));
    // Deduplicate + keep only visible elements
    const unique = Array.from(new Set(nodes)).filter((el) => el instanceof HTMLElement);
    unique.forEach((el) => el.classList.add("dt-reveal"));
    return unique;
  };

  const targets = revealTargets();

  if (prefersReducedMotion || !("IntersectionObserver" in window)) {
    targets.forEach((el) => el.classList.add("is-visible"));
    return;
  }

  const observer = new IntersectionObserver(
    (entries) => {
      for (const entry of entries) {
        if (!entry.isIntersecting) continue;
        const el = entry.target;
        el.classList.add("is-visible");
        observer.unobserve(el);
      }
    },
    { root: null, rootMargin: "0px 0px -10% 0px", threshold: 0.08 }
  );

  targets.forEach((el) => observer.observe(el));
})();

