/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    arr1.sort((a,b) => a.id - b.id);
    arr2.sort((a,b) => a.id - b.id);
    let ans = [];

    while ((arr1.length > 0) || (arr2.length > 0)) {

        if ((arr1.length > 0) && (arr2.length > 0)) {
            if (arr1[0].id < arr2[0].id) {
                ans.push(arr1.shift());
            }
            else if (arr1[0].id == arr2[0].id) {
                ans.push({...arr1.shift(), ...arr2.shift()});
            }
            else {
                ans.push(arr2.shift());
            }
        }
        else if (arr1.length > 0){
            ans.push(arr1.shift());
        }
        else {
            ans.push(arr2.shift());
        }
    }

    return ans;
};