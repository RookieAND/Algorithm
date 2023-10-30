function solution(N, road, K) {
  const dp = Array(N + 1).fill(Infinity);
  const graph = Array.from({ length: N + 1 }, () => []);

  road.forEach(([a, b, c]) => {
    graph[a].push([b, c]);
    graph[b].push([a, c]);
  });

  dp[1] = 0;

  let queue = [[1, 0]];
  while (queue.length) {
    let [destination] = queue.pop();

    // 경로 탐색을 진행하면서 현재 값보다 더 작은 케이스 탐색.
    graph[destination].map(([nextDestination, nextDistance]) => {
      if (dp[nextDestination] > dp[destination] + nextDistance) {
        dp[nextDestination] = dp[destination] + nextDistance;
        queue.push([nextDestination, nextDistance]);
      }
    });
  }

  return dp.filter((distance) => distance <= K).length;
}
