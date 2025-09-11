// Last updated: 9/11/2025, 12:30:35 PM
/**
 * @return {Function}
 */
var createHelloWorld = function() {
    return function(...args) {
        return "Hello World"
    }
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */