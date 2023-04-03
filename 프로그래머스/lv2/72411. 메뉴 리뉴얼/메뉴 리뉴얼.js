function solution(orders, course) {
  // 조합을 생성하는 함수 getCombinations
  const getCombinations = function (foods, amount) {
    const results = [];
    // 선택할 숫자가 하나라면, 그냥 각각의 요소를 배열에 넣어서 전달해주면 된다.
    if (amount === 1) return foods.map((value) => [value]);

    // 가장 앞에서부터 순차적으로 나머지를 자르고, 이를 재귀함수로 넘겨 나머지 파트에 대한 조합을 생성한다.
    foods.forEach((current, idx, origin) => {
      const rest = origin.slice(idx + 1);
      const combinations = getCombinations(rest, amount - 1);
      const result = combinations.map((comb) => [current, ...comb]);
      results.push(...result);
    });

    return results;
  };

  const answer = [];
  for (const courseAmount of course) {
    const result = new Map();
    let maximumAmount = 0;
    orders.forEach((order) => {
      const possibleCourses = getCombinations(order.split(""), courseAmount);
      if (possibleCourses.length > 0) {
        for (const possibleCourse of possibleCourses) {
          const courseStr = possibleCourse.sort().join("");
          result.set(courseStr, (result.get(courseStr) || 0) + 1);
          maximumAmount = Math.max(maximumAmount, result.get(courseStr));
        }
      }
    });

    // 한 개의 메뉴 조합이라도 2명 이상의 손님이 주문했다면, 정답을 고려해야 함.
    if (maximumAmount >= 2) {
      for (const [possibleCourse, amount] of result.entries()) {
        if (amount === maximumAmount) answer.push(possibleCourse);
      }
    }
  }

  return answer.sort();
}