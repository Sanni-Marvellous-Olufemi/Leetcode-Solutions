/**
 * @param {number[][]} mat
 * @return {number}
 */
var numSpecial = function(mat) {
    let row = {}, col = {}, ans = 0;

    for (let i = 0; i < mat.length; i++){
        for (let j = 0; j < mat[0].length; j++){
            if (mat[i][j] == 1){
                row[i] = (row[i] || 0) + 1;
                col[j] = (col[j] || 0) + 1;
            }
        }
    }

    for (let i = 0; i < mat.length; i++){
        for (let j = 0; j < mat[0].length; j++){
            if (mat[i][j] == 1 && row[i] == 1 && col[j] == 1){
                ans++;
            }
        }
    }

    return ans;
};