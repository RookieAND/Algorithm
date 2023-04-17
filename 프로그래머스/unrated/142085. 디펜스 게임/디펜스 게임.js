// 1. 무적권을 썼을 때와 안 썼을 때를 분기하여 백트래킹 진행
// 2. 만약 현재 보유 중인 병사의 수가 부족하다면 재귀 종료 후 대조

// function solution(n, k, enemy) {
//   let answer = 0;

//   function fightEnemy(leftArmy, leftShield, stage) {
//     // 더 이상 진행할 스테이지가 없을 경우 답이 나왔으므로 종료
//     if (stage === enemy.length) {
//       answer = stage;
//       return;
//     }

//     const curEnemyAmount = enemy[stage];
//     // 만약 현재 보유 중인 병사가 부족한 경우 재귀 종료.
//     if (!leftShield && leftArmy - curEnemyAmount < 0) {
//       answer = Math.max(answer, stage);
//       return;
//     }

//     // 그렇지 않은 경우 까방권을 쓴 케이스와 쓰지 않은 케이스로 분기
//     if (leftShield) {
//       fightEnemy(leftArmy, leftShield - 1, stage + 1);
//     }
//     // 만약 까방권이 없는 경우, 현재 스테이지를 넘길 수 있는지 체크해야 함
//     if (leftArmy - curEnemyAmount >= 0)
//       fightEnemy(leftArmy - curEnemyAmount, leftShield, stage + 1);
//   }

//   fightEnemy(n, k, 0);
//   return answer;
// }


// 정답 풀이 : 이진 탐색 (nlogn)
function solution(n, k, enemy) {
    let answer = 0;
    let start = 0, end = enemy.length;
    
    while(start <= end) {
        let mid = Math.floor((start + end) / 2);
        let arr = enemy.slice(0, mid).sort((a, b) => b - a);
        
        let canDefense = true;
        let temp = 0 ;
        for (let i = k ; i < arr.length; i++){
            temp += arr[i];
            if(temp > n) canDefense = false;
        }
        
        if (canDefense) {
            answer = mid;
            start = mid + 1; 
        }
        else end = mid - 1;
    }
    
    return answer;
}