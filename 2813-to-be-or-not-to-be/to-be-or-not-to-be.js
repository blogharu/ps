/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    let expected = val
    return {
        toBe: (val) => {
            if (expected !== val) 
                throw new Error('Not Equal');
            return true
        },
        notToBe: (val) => {
            if (expected === val) 
                throw new Error('Equal');
            return true
        }
    }
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */