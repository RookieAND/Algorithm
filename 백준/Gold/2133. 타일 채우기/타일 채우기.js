const fs = require('fs');
let N = Number(fs.readFileSync('/dev/stdin').toString().trim());

const dp = Array(N + 1).fill(0);

dp[0] = 1;
dp[2] = 3;

for (let i = 4; i <= N; i += 2) {
    // 좌우로 너비가 2일 때 나올 수 있는 케이스를 이어 붙일 수 있다.
    dp[i] += dp[i - 2] * dp[2];
    for (let j = 4; j <= i; j += 2) {
      dp[i] += dp[i - j] * 2;
    }
}
console.log(dp[N]);