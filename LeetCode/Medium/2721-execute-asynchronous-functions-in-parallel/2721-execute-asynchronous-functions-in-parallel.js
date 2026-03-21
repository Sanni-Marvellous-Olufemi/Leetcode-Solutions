/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    const arr = functions.map((fn) => fn());
    let count;
    let curr = 0;

    const ans = new Promise((resolve, reject) => {
        arr.forEach((fn, i) => {
            fn.then((val) => {
                functions[i] = val;
                curr += 1
                if (curr == functions.length){
                    resolve(functions)
                }
                
            }).catch((err) => {
                // if (!count){
                    reject(err);
                //     count = 1;
                // }
            })
        })
        
    })
    
    return ans
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */