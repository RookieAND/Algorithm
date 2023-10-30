const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((row) => row.split(" ").map(Number));

let [N, M, R] = input[0];
let matrix = input.slice(1, N + 1);
const operations = input.at(-1);

function first(arr) {
  arr = arr.reverse();
  return arr;
}

function second(arr) {
  for (let i = 0; i < arr.length; i++) {
    arr[i] = arr[i].reverse();
  }
  return arr;
}

function third(arr) {
  const [N, M] = [arr.length, arr[0].length];
  let temp = Array.from({ length: M }, () => Array(N).fill(0));

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      temp[j][N - (i + 1)] = arr[i][j];
    }
  }
  return temp;
}

function fourth(arr) {
  const [N, M] = [arr.length, arr[0].length];
  let temp = Array.from({ length: M }, () => Array(N).fill(0));

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      temp[M - (j + 1)][i] = arr[i][j];
    }
  }
  return temp;
}

function fifth(arr) {
  const [N, M] = [arr.length, arr[0].length];
  const temp = arr.map((value) => [...value]);

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      temp[i][j] = arr[i][j];
    }
  }

  for (let i = 0; i < parseInt(N / 2); i++) {
    for (let j = 0; j < parseInt(M / 2); j++) {
      temp[i][j + Math.ceil(M / 2)] = arr[i][j];
    }
  }
  for (let i = 0; i < parseInt(N / 2); i++) {
    for (let j = Math.ceil(M / 2); j < M; j++) {
      temp[i + Math.ceil(N / 2)][j] = arr[i][j];
    }
  }
  for (let i = Math.ceil(N / 2); i < N; i++) {
    for (let j = Math.ceil(M / 2); j < M; j++) {
      temp[i][j - Math.ceil(M / 2)] = arr[i][j];
    }
  }
  for (let i = Math.ceil(N / 2); i < N; i++) {
    for (let j = 0; j < Math.ceil(M / 2); j++) {
      temp[i - Math.ceil(N / 2)][j] = arr[i][j];
    }
  }
  return temp;
}

function sixth(arr) {
  const [N, M] = [arr.length, arr[0].length];
  const temp = arr.map((value) => [...value]);

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      temp[i][j] = arr[i][j];
    }
  }

  for (let i = 0; i < Math.ceil(N / 2); i++) {
    for (let j = 0; j < Math.ceil(M / 2); j++) {
      temp[i + Math.ceil(N / 2)][j] = arr[i][j];
    }
  }

  for (let i = Math.ceil(N / 2); i < N; i++) {
    for (let j = 0; j < Math.ceil(M / 2); j++) {
      temp[i][j + Math.ceil(M / 2)] = arr[i][j];
    }
  }

  for (let i = Math.ceil(N / 2); i < N; i++) {
    for (let j = Math.ceil(M / 2); j < M; j++) {
      temp[i - Math.ceil(N / 2)][j] = arr[i][j];
    }
  }

  for (let i = 0; i < Math.ceil(N / 2); i++) {
    for (let j = Math.ceil(M / 2); j < M; j++) {
      temp[i][j - Math.ceil(M / 2)] = arr[i][j];
    }
  }

  return temp;
}

const calculate = [first, second, third, fourth, fifth, sixth];

operations.map((operation) => (matrix = calculate[operation - 1](matrix)));
console.log(matrix.map((v) => v.join(" ")).join("\n"));
