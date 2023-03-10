$(document).ready(function() {
	gsap.from(".line-one", {
	    scrollTrigger: {
	      trigger: ".line-one",
	      toggleActions: "play reverse play reverse",
	      scrub: 1,
	    },
	    x: -300,
	    duration: 2
	  });
  gsap.from(".computer-desk", {
    scrollTrigger: {
      trigger: ".computer-desk",
      toggleActions: "play reverse play reverse",
      scrub: 1,
    },
    x: -300,
    duration: 2
  });
  gsap.from(".line-two", {
	    scrollTrigger: {
	      trigger: ".line-two",
	      toggleActions: "play reverse play reverse",
	      scrub: 1,
	    },
	    x: -300,
	    duration: 2
	  });
  gsap.from(".line-three", {
    scrollTrigger: {
      trigger: ".line-three",
      toggleActions: "play reverse play reverse",
      scrub: 1,
    },
    x: +300,
    duration: 2
  });
  gsap.from(".section-1", {
    scrollTrigger: {
      trigger: ".section-1",
      toggleActions: "play reverse play reverse",
    },
    opacity: 0,
    duration: 1
  });
  gsap.from(".section-2", {
    scrollTrigger: {
      trigger: ".section-2",
      toggleActions: "play reverse play reverse",
    },
    opacity: 0,
    duration: 1
  });
  gsap.from(".section-3", {
    scrollTrigger: {
      trigger: ".section-3",
      toggleActions: "play reverse play reverse",
    },
    opacity: 0,
    duration: 1
  });
  gsap.from(".section-4", {
    scrollTrigger: {
      trigger: ".section-4",
      toggleActions: "play reverse play reverse",
    },
    opacity: 0,
    duration: 1
  });
  gsap.from(".section-5", {
    scrollTrigger: {
      trigger: ".section-5",
      toggleActions: "play reverse play reverse",
    },
    opacity: 0,
    duration: 1
  });
  gsap.from(".section-6", {
    scrollTrigger: {
      trigger: ".section-6",
      toggleActions: "play reverse play reverse",
    },
    opacity: 0,
    duration: 1
  });
  gsap.from(".footer-section", {
    scrollTrigger: {
      trigger: ".footer-section",
      toggleActions: "play reverse play reverse",
    },
    opacity: 0,
    duration: 1

  });
})(jQuery);
