;(function($) {
    $.fn.swipe = function(f) {
        var g = {
            DECAY: 0.9,
            MOUSEDOWN_DECAY: 0.5,
            SPEED_SPRING: 0.5,
            BOUNCE_SPRING: 0.08,
            HORIZ: true,
            TYPE: 'mouseSwipe',
            SNAPDISTANCE: 20,
            DURATION: 250,
            EASING: 'swing',
            ARROWS: false,
            FADEARROWS: false,
            SLIDESHOWTIME: 4000,
            AUTOSTART: 0,
            PAUSEONHOVER: false,
            PAGENUM: '#pagenum',
            DISABLELINKS: true
        };
        var btn;
        var o = $.extend(g, f);
        var h = this;
        var i = document.getElementById(h.attr('id'));
        var j = h.children(".panel");
        var k = parseInt(h.parents('div').css('width'), 10);
        var l = parseInt(h.parents('div').css('height'), 10);
        var m = 0,
            bouncing = 0,
            _mouseDownLT, _mouseDownXY, _lastMouseDownXY, panelnum = 1;
        var n, sliderLT, sliderLen, _mouseDown = false,
            ie = false,
            hasTouch = false,
            VIEWPORT, len;
        var p = false,
            slideInterval = null;
        if (o.HORIZ == true) {
            var q = parseInt(j.css('width'), 10) * j.length;
            VIEWPORT = k;
            n = 'left';
            j.css('float', 'left');
            h.css('width', q);
            sliderLen = q;
            h.after("<div class='navLeft'></div><div class='navRight'></div>")
        } else {
            var r = parseInt(j.css('height'), 10) * j.length;
            VIEWPORT = l;
            n = 'top';
            j.css('float', 'none');
            h.css('height', r);
            sliderLen = r;
            h.after("<div class='navTop'></div><div class='navBottom'></div>")
        }
        h.css(n, 0);
        var s = $(this).next('.navTop,.navLeft');
        var t = s.next('.navBottom,.navRight');
        s.bind('mouseup', function(e) {
            panelnum--;
            w($(this).attr('class'));
            return false
        });
        t.bind('mouseup', function(e) {
            panelnum++;
            w($(this).attr('class'));
            return false
        });
        if (o.ARROWS == false) {
            $(s).css('display', 'none');
            $(t).css('display', 'none')
        }
        var u = function(a) {
            if (_mouseDown) {
                m *= o.MOUSEDOWN_DECAY
            } else {
                m *= o.DECAY
            }
            if (!_mouseDown) {
                if (a > 0) {
                    bouncing = -a * o.BOUNCE_SPRING
                } else if (a + sliderLen < VIEWPORT) {
                    bouncing = (VIEWPORT - sliderLen - a) * o.BOUNCE_SPRING
                } else {
                    bouncing = 0
                }
                if (_lastMouseDownXY - _mouseDownXY < 0) {
                    h.css(n, a + Math.ceil(m + bouncing))
                } else {
                    h.css(n, a + Math.floor(m + bouncing))
                }
            }
        };
        var v = function(b) {
            if (o.HORIZ == true) {
                len = k;
                a = 'left'
            } else {
                a = 'top';
                len = l
            }
            panelnum = Math.ceil(Math.abs((b / j.length) / (len / j.length)));
            if (_lastMouseDownXY - _mouseDownXY <= -(o.SNAPDISTANCE)) {
                if (panelnum >= j.length) {
                    panelnum = j.length - 1
                }
                x(a, -len * panelnum, len)
            } else if (_lastMouseDownXY - _mouseDownXY >= o.SNAPDISTANCE) {
                x(a, (panelnum * -len) + len, len)
            }
        };
        var w = function(c) {
            if (c == 'navTop') {
                len = l;
                a = 'top';
                b = -r + len;
                d = parseInt(h.css(a)) + len
            } else if (c == 'navBottom') {
                len = l;
                a = 'top';
                b = -r + len;
                d = parseInt(h.css(a)) - len
            } else if (c == 'navLeft') {
                len = k;
                a = 'left';
                b = -q + len;
                d = parseInt(h.css(a)) + len
            } else {
                len = k;
                a = 'left';
                b = -q + len;
                d = parseInt(h.css(a)) - len
            }
            if (panelnum > j.length) {
                panelnum = 1;
                x(a, 0, len);
                return
            }
            if (panelnum < 1) {
                panelnum = j.length;
                x(a, b, len);
                return
            }
            x(a, d, len)
        };
        var x = function(a, b, c) {
            var d = {};
            d[a] = b;
            h.stop(true, true).animate(d, {
                duration: o.DURATION,
                easing: o.EASING,
                complete: function() {
                    y(c)
                }
            })
        };
        var y = function(a) {
            sliderLT = parseInt(h.css(n), 10);
            panelnum = Math.ceil(Math.abs((sliderLT / j.length) / (a / j.length)) + 1);
            $(o.PAGENUM).html(panelnum);
            btn = o.HORIZ == true ? '.navRight' : '.navTop';
            if (o.ARROWS == true) {
                if (o.FADEARROWS == true && panelnum == j.length) {
                    $(t, btn).fadeOut('fast')
                } else {
                    $(t, btn).fadeIn('fast')
                }
                if (o.FADEARROWS == true && panelnum == 1) {
                    $(s, btn).fadeOut('fast')
                } else {
                    $(s, btn).fadeIn('fast')
                }
            }
        };
        var z = function(e) {
            clearInterval(slideInterval);
            slideInterval = null
        };
        var A = function(e) {
            clearInterval(slideInterval);
            slideInterval = null;
            slideInterval = setInterval(function() {
                panelnum++;
                w(t.attr('class'))
            }, o.SLIDESHOWTIME)
        };
        window.requestAnimFrame = function() {
            return (window.requestAnimationFrame || window.webkitRequestAnimationFrame || window.mozRequestAnimationFrame || window.oRequestAnimationFrame || window.msRequestAnimationFrame ||
            function(a) {
                window.setTimeout(a, 1000 / 60)
            })
        }();

        function frame() {
            u(parseInt(h.css(n), 10));
            if (p == true) {
                requestAnimFrame(frame)
            }
        };
        var B = function() {
            $('a', h).each(function() {
                $(this).click(function() {
                    if (Math.abs(_lastMouseDownXY - _mouseDownXY) >= o.SNAPDISTANCE) {
                        return false
                    }
                })
            })
        };
        var C = function(e) {
            h.stop(true, false);
            if (o.ARROWS == true) {
                $(s, btn).css('display', 'none');
                $(t, btn).css('display', 'none')
            }
            if (!_mouseDown) {
                if (hasTouch) {
                    e.preventDefault();
                    e = event.touches[0]
                } else {
                    if (!e) e = window.event
                }
                if (i.setCapture) {
                    i.setCapture()
                } else {
                    window.addEventListener('mousemove', D, false);
                    window.addEventListener('mouseup', E, false)
                }
                if (o.HORIZ == true) {
                    _mouseDownXY = _lastMouseDownXY = ie == true ? e.clientX : e.pageX;
                    _mouseDownLT = document.getElementById(h.attr('id')).offsetLeft
                } else {
                    _mouseDownXY = _lastMouseDownXY = ie == true ? e.clientY : e.pageY;
                    _mouseDownLT = document.getElementById(h.attr('id')).offsetTop
                }
                _mouseDown = true;
                if (o.TYPE == 'mouseSwipe' && p == false) {
                    p = true;
                    requestAnimFrame(frame)
                }
            }
        };
        var D = function(e) {
            if (_mouseDown) {
                if (hasTouch) {
                    e.preventDefault();
                    e = event.touches[0]
                } else {
                    if (!e) e = window.event
                }
                if (ie == true) {
                    var a = n == 'left' ? e.clientX : e.clientY
                } else {
                    var a = n == 'left' ? e.pageX : e.pageY
                }
                h.css(n, _mouseDownLT + (a - _mouseDownXY));
                m += ((a - _lastMouseDownXY) * o.SPEED_SPRING);
                _lastMouseDownXY = a
            }
        };
        var E = function(e) {
            if (_mouseDown) {
                _mouseDown = false;
                B();
                if (i.setCapture) {
                    i.releaseCapture()
                } else {
                    window.removeEventListener('mousemove', D, false);
                    window.removeEventListener('mouseup', E, false)
                }
                if (o.TYPE == 'panelSwipe') {
                    v(parseInt(h.css(n), 10))
                }
            }
        };
        hasTouch = 'ontouchstart' in window;
        h.bind('mousedown touchstart', function(a) {
            C(a)
        });
        h.bind('mousemove touchmove', function(a) {
            D(a)
        });
        h.bind('mouseup touchend', function(a) {
            E(a)
        });
        var F = o.PAUSEONHOVER == true && o.TYPE == 'panelSwipe';
        if (F) {
            h.bind('mouseenter', function(a) {
                z(a)
            })
        }
        if (F) {
            h.bind('mouseleave', function(a) {
                A(a)
            })
        }
        if (o.FADEARROWS == true) {
            btn = o.HORIZ == true ? '.navRight' : '.navTop';
            $(s, btn).css('display', 'none')
        }
        if (o.AUTOSTART > 0) {
            setTimeout(A, o.AUTOSTART)
        }
    }
})(jQuery);
