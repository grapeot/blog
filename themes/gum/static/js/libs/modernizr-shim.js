window.Modernizr = {
  touch: ('ontouchstart' in window) || (navigator.maxTouchPoints > 0),
  load: function(config) {
    if (config.complete) config.complete();
  }
};
