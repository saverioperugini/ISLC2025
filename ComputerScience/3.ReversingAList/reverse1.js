function reverse1(L) {
    var revL = new Array;
    for(var i = L.length-1; i >= 0; i--) {
        revL.push(L[i]);
    }
    return revL;
}

var l = [3,5,7,8]
var rl = reverse1(l);

function reverse2(L) {
    if (L.length == 0) {
       return L;
    } else {
         return reverse2(L.slice(1)).concat([L[0]]);
      }
}
