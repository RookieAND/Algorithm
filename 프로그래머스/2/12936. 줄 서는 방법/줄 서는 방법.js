function solution(n, k) {
  const answer = [];
  const dp = Array.from({ length: n }, (_, i) => i + 1);
  let factorial = dp.reduce((ac, v) => ac * v, 1);

  while (answer.length < n) {
    factorial = factorial / dp.length;
    answer.push(...dp.splice(Math.floor((k - 1) / factorial), 1));
    k = k % factorial;
  }

  return answer;
}
