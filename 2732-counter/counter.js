/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    let val = n
    return function() {
        val += 1
        return val - 1
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */