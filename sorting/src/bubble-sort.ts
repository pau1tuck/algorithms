/*
Begin iterating through the array, compare 2 elements at a time, swap them if they're not in the correct order.
After the first pass, ignore the final index of the second pass.
Continue passing until the final index matches the first index.
*/
function bubbleSort(arr: Array<number>) {
  let i: number, j: number;
  let isSwapped = false;

  for (i = 0; i < arr.length; i++) {
    isSwapped = false;
    for (j = 0; j < arr.length; j++) {
      if (arr[j] > arr[j + 1]) {
        let tmp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = tmp;
        isSwapped = true;
      }
    }
    if (!isSwapped) {
      break;
    }
  }

  // Print the array
  console.log(arr);
}

let testData = [234, 43, 55, 63, 5, 6, 235, 547];
bubbleSort(testData);
