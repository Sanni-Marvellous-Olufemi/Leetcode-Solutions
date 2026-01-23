/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {

    function walk(obj) {

        if (Array.isArray(obj)) {
            let ans = [];
            for (const i of obj) {
                if (!i) {
                    continue;
                }
                if (typeof i == "object"){
                    ans.push(walk(i));
                }  else {
                    ans.push(i);
                }
            }
            return ans;
        }

        else {
            for (const i in obj) {
                if (!obj[i]) {
                    delete obj[i];
                    continue;
                }
                if (typeof obj[i] == "object"){
                    obj[i] = walk(obj[i]);
                }
            }
            return obj;
        }
    }
    return walk(obj);
};