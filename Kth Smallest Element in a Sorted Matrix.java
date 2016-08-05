public class Solution {
    public int kthSmallest(int[][] matrix, int k) {
		PriorityQueue<Integer> heap = new PriorityQueue<Integer>(new Comparator<Integer>() {
			public int compare(Integer a0, Integer a1) {
				if(a0>a1){
					return -1;
				}else if(a0<a1){
					return 1;
				}
				return 0;
			}
		});// ×î´ó¶Ñ
		for (int i = 0; i < matrix.length; i++) {
			for (int j = 0; j < matrix.length; j++) {
				if (i * matrix.length + j + 1 > k) {
					if (matrix[i][j] < heap.peek()) {
						heap.poll();
						heap.offer(matrix[i][j]);
					}
				} else {
					heap.offer(matrix[i][j]);
				}
			}

		}

		return heap.peek();
	}
}