function debounce(fn, delay = 1000, immediate) {
    let timer = null
    return function (args) {

        if (immediate) {
            if (!timer) {
                fn.apply(this, args)

            }
            clearTimeout(timer)
            timer = setTimeout(() => {
                timer = null
            }, delay)
        }
        else {
            if (timer) {
                clearTimeout(timer)
            }

            timer = setTimeout(() => {
                fn.apply(this, args)
                timer = null
            }, delay)
        }

    }
}
function throttling(fn, dely=1000, immediate) {
    let timer = null
    return function (args) {

        if (immediate) {
            if (!timer) {
                fn.apply(this, args)
                timer = setTimeout(() => {
                    timer = null
                }, dely)
            }
        }
        else {
            if (!timer) {
                timer = setTimeout(() => {
                    fn.apply(this, args)
                    timer = null
                }, dely);
            }
        }

    }
}
let leading_input = debounce(() => {
    console.log("防抖-前缘")
}, 1000, true)
let delay_input = debounce(() => {
    console.log("防抖-延迟")
}, 1000, false)
let leading_button = throttling(() => {
    console.log("节流-前缘")
}, 1000, true)
let delay_button = throttling(() => {
    console.log("节流-延迟")
}, 1000, false)