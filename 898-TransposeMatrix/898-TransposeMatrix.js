// Last updated: 9/11/2025, 12:31:29 PM
/**
 * @param {number[][]} matrix
 * @return {number[][]}
 */
var transpose = function(matrix) {
    // swapping them
    var cols = matrix[0].length;
    var rows = matrix.length;
    var newMat = Array.from({length: cols}, () => Array(rows).fill(0));
    for (let i = 0; i < matrix.length; i++){
        for (let j = 0; j < matrix[0].length; j++){
        newMat[j][i] = matrix[i][j]
    }
    }
    return newMat
};