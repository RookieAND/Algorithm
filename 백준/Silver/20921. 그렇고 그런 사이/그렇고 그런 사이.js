// 먼저 N, K를 입력 받는다.
let [N, K] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trimEnd()
  .split(" ")
  .map(Number);

let numbers = [...new Array(N + 1).keys()].slice(1);

let count = 0;

// (N - 1) / 2 만큼의 반복을 계속해서 진행한다. K번째 순서에서 멈춘다.
for (let i = 1; i < N; i++) {
  for (let movedIndex = N - 1; movedIndex > i - 1; movedIndex--) {
    if (count >= K) break;
    let temp = numbers[movedIndex];
    numbers[movedIndex] = numbers[movedIndex - 1];
    numbers[movedIndex - 1] = temp;
    count++;
  }
  if (count >= K) break;
}

console.log(numbers.join(" "));
