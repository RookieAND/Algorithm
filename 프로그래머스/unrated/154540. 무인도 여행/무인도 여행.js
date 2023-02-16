function solution(maps) {
	let answer = [];
	let visited = Array.from(Array(maps.length), () =>
		Array(maps[0].length).fill(false)
	);
	for (let i = 0; i < maps.length; i++) {
		for (let j = 0; j < maps[0].length; j++) {
			if (maps[i][j] != "X" && !visited[i][j]) {
				visited[i][j] = true;
				answer.push(findLand(i, j, maps, visited));
			}
		}
	}
	answer.sort((a, b) => a - b);
	return answer.length > 0 ? answer : [-1];
}

function findLand(y, x, maps, visited) {
	const direction = [
		[1, 0],
		[0, 1],
		[-1, 0],
		[0, -1],
	];
	const [maxY, maxX] = [maps.length, maps[0].length];

	let queue = [[y, x]];
	let landSize = 0;

	while (queue.length > 0) {
		const [ny, nx] = queue.shift();
		landSize += Number(maps[ny][nx]);
		for (const [dy, dx] of direction) {
			const [my, mx] = [ny + dy, nx + dx];
			if (my >= 0 && mx >= 0 && my < maxY && mx < maxX) {
				if (maps[my][mx] != "X" && !visited[my][mx]) {
					queue.push([my, mx]);
					visited[my][mx] = true;
				}
			}
		}
	}
	return landSize;
}
