function solution(N, left, right) {
  let answer = [];

  for (let num = left; num <= right; num++) {
    answer.push(Math.max(Math.floor(num / N), num % N) + 1)
  }
  return answer;
}
