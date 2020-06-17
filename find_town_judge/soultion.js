/**
 * @param {number} N
 * @param {number[][]} trust
 * @return {number}
 */
var findJudge = function(N, trust) {
   if (trust.length === 0 && N === 1) return 1

   function node() {
      this.trusts = []
      this.trustedBy = []
   }
   let nodes = []

   trust.forEach(pair => {
      pair.forEach(element => {
         if (nodes[element] === undefined)
            nodes[element] = new node()
      })
      nodes[pair[0]].trusts.push(pair[1])
      nodes[pair[1]].trustedBy.push(pair[0])
   })

   for (const [index, person] of nodes.entries()){
      if (person !== undefined) {
         if (person.trusts.length == 0 && person.trustedBy.length == N - 1)
            return index
      }
   }
   return -1

};

findJudge(3, [[1,2],[3,2],[1,3]])

