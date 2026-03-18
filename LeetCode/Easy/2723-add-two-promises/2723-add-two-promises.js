/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
    let curr = 0;

    return promise1.then((data) => {
        curr += data;
        return promise2 
    }).then((data1) => {
        curr += data1;
        return curr;
    });
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */