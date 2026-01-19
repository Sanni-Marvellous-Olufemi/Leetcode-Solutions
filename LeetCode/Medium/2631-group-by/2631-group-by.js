/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    hashmap = {};
    
    for (i of this){
        key = fn(i);
        if (!(key in hashmap)){
            hashmap[key] = [];
        }
        hashmap[key].push(i);
    }

    return hashmap;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */