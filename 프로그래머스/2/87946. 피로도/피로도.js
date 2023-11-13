function solution(k, dungeons) {
  let answer = 0;

  const visited = new Array(dungeons.length).fill(false);

  // 각 던전 별 피로도를 깎으며 순회하는 함수 dfs
  function dfs(fatigue, stage) {
    for (let i = 0; i < dungeons.length; i++) {
      // 아직 방문하지 않았고 다음 던전 탐사에 필요한 피로도가 현재 피로도보다 작으면..
      if (!visited[i] && dungeons[i][0] <= fatigue) {
        visited[i] = true;
        dfs(fatigue - dungeons[i][1], stage + 1);
        visited[i] = false;
      } 
    }

    answer = Math.max(answer, stage);
  }

  dfs(k, 0);

  return answer;
}