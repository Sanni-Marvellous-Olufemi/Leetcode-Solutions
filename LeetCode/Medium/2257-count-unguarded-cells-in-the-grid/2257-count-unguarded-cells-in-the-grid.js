/**
 * @param {number} m
 * @param {number} n
 * @param {number[][]} guards
 * @param {number[][]} walls
 * @return {number}
 */
var countUnguarded = function(m, n, guards, walls) {
    let mat = new Array(m);
    let set = new Set();
    let count = 0;

    for (let i = 0; i < m; i++) {
        mat[i] = new Array(n);
    }

    for (let i = 0; i < walls.length; i++) {
        let key = JSON.stringify(walls[i]);
        set.add(key);
    }

    for (let i = 0; i < guards.length; i++) {
        let [r,c] = guards[i];
        while (c < n) {
            if (set.has(JSON.stringify([r,c]))) {
                break;
            }
            mat[r][c] = "g";
            c++;
        }
        c = guards[i][1];
        while (c >= 0) {
            if (set.has(JSON.stringify([r,c]))) {
                break;
            }
            mat[r][c] = "g";
            c--;
        }
        c = guards[i][1];
        while (r < m) {
            if (set.has(JSON.stringify([r,c]))) {
                break;
            }
            mat[r][c] = "g";
            r++;
        }
        r = guards[i][0];
        while (r >= 0) {
            if (set.has(JSON.stringify([r,c]))) {
                break;
            }
            mat[r][c] = "g";
            r--;
        }
    }
    for (let i = 0; i < m; i++){
        for (let j = 0; j < n; j++) {
            if (!mat[i][j] && !set.has(JSON.stringify([i,j]))) {
                count ++;
            }
        }
    }
    return count;
};